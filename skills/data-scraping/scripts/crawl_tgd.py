#!/usr/bin/env python3
"""
Crawl TheGioiDong.com - Thu thập thông tin sản phẩm
"""
import asyncio
import json
import os
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

OUTPUT_DIR = "/home/openclaw/.openclaw/skills/data-scraping/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Schema trích xuất sản phẩm từ trang danh mục
PRODUCT_SCHEMA = {
    "name": "Products",
    "baseSelector": "li.product-item, div.product-item, .product",
    "fields": [
        {"name": "title", "selector": "h3, .product-title, .product-name", "type": "text"},
        {"name": "price", "selector": ".price, .product-price, strong", "type": "text"},
        {"name": "old_price", "selector": ".old-price, .price-old, del", "type": "text"},
        {"name": "promotion", "selector": ".promotion, .sale-off, .discount", "type": "text"},
        {"name": "rating", "selector": ".rating, .stars, .review", "type": "text"},
        {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"},
        {"name": "image", "selector": "img", "type": "attribute", "attribute": "data-src"},
    ]
}

async def crawl_category(url, category_name):
    """Crawl một trang danh mục sản phẩm."""
    print(f"\n🔍 Crawling {category_name}: {url}")
    
    async with AsyncWebCrawler() as crawler:
        strategy = JsonCssExtractionStrategy(PRODUCT_SCHEMA)
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            extraction_strategy=strategy,
            page_timeout=45000,
            wait_for="css:.product-item, css:.product",
        )
        
        result = await crawler.arun(url=url, config=config)
        
        if not result.success:
            print(f"❌ Failed: {result.error_message}")
            return []
        
        if result.extracted_content:
            products = json.loads(result.extracted_content)
            print(f"✅ Found {len(products)} products")
            return products
        return []


async def crawl_homepage():
    """Crawl trang chủ để lấy danh mục."""
    print("\n🏠 Crawling homepage...")
    
    async with AsyncWebCrawler() as crawler:
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            page_timeout=30000,
        )
        
        result = await crawler.arun(url="https://www.thegioididong.com", config=config)
        
        if not result.success:
            print(f"❌ Homepage failed: {result.error_message}")
            return {}
        
        # Lấy các link danh mục từ trang chủ
        categories = {}
        if result.links:
            internal_links = result.links.get("internal", [])
            # Lọc các link danh mục chính
            for link in internal_links[:50]:
                if any(x in link for x in ['/dien-thoai', '/laptop', '/tablet', '/dong-ho', '/phu-kien']):
                    categories[link.split('/')[-1]] = link
        
        return categories


async def main():
    print("=" * 60)
    print("🕷️ CRAWL THEGIOIDIDONG.COM")
    print("=" * 60)
    
    # Các trang danh mục chính
    categories = {
        "dien-thoai": "https://www.thegioididong.com/dien-thoai",
        "laptop": "https://www.thegioididong.com/laptop",
        "tablet": "https://www.thegioididong.com/may-tinh-bang",
        "dong-ho": "https://www.thegioididong.com/dong-ho-thong-minh",
    }
    
    all_results = {}
    
    for cat_name, cat_url in categories.items():
        products = await crawl_category(cat_url, cat_name)
        all_results[cat_name] = products
        await asyncio.sleep(2)  # Rate limiting
    
    # Lưu kết quả
    output_file = os.path.join(OUTPUT_DIR, "thegioididong_products.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Saved: {output_file}")
    
    # Tóm tắt
    print("\n📊 SUMMARY:")
    for cat, products in all_results.items():
        print(f"  - {cat}: {len(products)} products")
    
    # Xuất mẫu vài sản phẩm
    print("\n📋 SAMPLE PRODUCTS:")
    for cat, products in all_results.items():
        if products:
            print(f"\n  [{cat}]")
            for p in products[:3]:
                print(f"    • {p.get('title', 'N/A')} - {p.get('price', 'N/A')}")
    
    return all_results


if __name__ == "__main__":
    asyncio.run(main())
