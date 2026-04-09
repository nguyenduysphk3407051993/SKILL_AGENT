#!/usr/bin/env python3
"""Crawl 8 bài KHTN 6 - Tách chất ra khỏi hỗn hợp từ loigiaihay.com"""
import asyncio
import os
import re
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig

OUTPUT_DIR = "/home/openclaw/.openclaw/skills/data-scraping/output/khtn6-tach-chat"
os.makedirs(OUTPUT_DIR, exist_ok=True)

URLS = [
    ("01_tach-chat-kntt", "https://loigiaihay.com/tach-chat-ra-hon-hop-khtn-6-ket-noi-tri-thuc-a90893.html"),
    ("02_cau-hoi-muc-I-trang-60-kntt", "https://loigiaihay.com/tra-loi-cau-hoi-muc-i-trang-60-sgk-khtn-6-ket-noi-tri-thuc-a90895.html"),
    ("03_cau-hoi-muc-II-trang-63-kntt", "https://loigiaihay.com/tra-loi-cau-hoi-muc-ii-trang-63-sgk-khtn-6-ket-noi-tri-thuc-a91492.html"),
    ("04_tach-chat-canh-dieu", "https://loigiaihay.com/tach-chat-ra-khoi-hon-hop-khtn-6-canh-dieu-a90840.html"),
    ("05_phuong-phap-tach-chat-ctst", "https://loigiaihay.com/mot-so-phuong-phap-tach-chat-ra-khoi-hon-hop-khtn-6-chan-troi-sang-tao-a91039.html"),
    ("06_thao-luan-trang-82-ctst", "https://loigiaihay.com/tra-loi-cau-hoi-thao-luan-2-trang-82-sgk-khtn-6-chan-troi-sang-tao-a91044.html"),
    ("07_ly-thuyet-hon-hop-tach-chat", "https://loigiaihay.com/ly-thuyet-ve-hon-hop-va-tach-chat-ra-khoi-hon-hop-e34238.html"),
    ("08_chuong-IV-sbt", "https://loigiaihay.com/chuong-iv-hon-hop-tach-chat-khoi-hon-hop-sbt-e22716.html"),
]

async def main():
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        page_timeout=30000,
        css_selector="div.box-content, div.detail_new",
    )
    
    results_summary = []
    
    async with AsyncWebCrawler() as crawler:
        for filename, url in URLS:
            print(f"\n🔍 Crawling: {filename}")
            try:
                result = await crawler.arun(url=url, config=config)
                if result.success:
                    content = result.markdown.raw_markdown
                    title = result.metadata.get("title", filename) if result.metadata else filename
                    
                    filepath = os.path.join(OUTPUT_DIR, f"{filename}.md")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(f"# {title}\n\n")
                        f.write(f"Source: {url}\n\n---\n\n")
                        f.write(content)
                    
                    results_summary.append((filename, len(content), "✅"))
                    print(f"  ✅ {len(content)} chars → {filepath}")
                else:
                    results_summary.append((filename, 0, "❌"))
                    print(f"  ❌ Error: {result.error_message}")
            except Exception as e:
                results_summary.append((filename, 0, f"❌ {e}"))
                print(f"  ❌ Exception: {e}")
    
    print("\n" + "="*60)
    print("📊 TÓM TẮT KẾT QUẢ")
    print("="*60)
    total = 0
    for name, chars, status in results_summary:
        print(f"  {status} {name}.md — {chars:,} chars")
        total += chars
    print(f"\n  📦 Tổng: {len(results_summary)} bài | {total:,} ký tự")
    print(f"  📁 Thư mục: {OUTPUT_DIR}")

asyncio.run(main())
