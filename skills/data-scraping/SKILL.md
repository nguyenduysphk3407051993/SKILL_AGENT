---
name: data-scraping
description: "Skill crawl và scrape dữ liệu web sử dụng Crawl4AI (v0.8.6). Dùng khi cần thu thập nội dung từ website, trích xuất dữ liệu có cấu trúc, crawl nhiều trang, hoặc chuyển đổi nội dung web sang markdown/JSON."
allowed-tools: Read, Write, Exec, Process, WebFetch, WebSearch
argument-hint: "[url hoặc danh sách urls] [định dạng output: markdown|json|csv] [tùy chọn: css_selector, wait_for, extract_schema]"
---

# Skill: Data Scraping với Crawl4AI

## Description
Skill này sử dụng thư viện **Crawl4AI v0.8.6** (cài từ source `/opt/crawl4ai`) để crawl và scrape dữ liệu từ web. Hỗ trợ crawl đơn trang, đa trang, trích xuất dữ liệu có cấu trúc bằng CSS selector / LLM extraction, và xuất kết quả ra markdown, JSON hoặc CSV.

## Môi trường

- **Python venv:** `/home/openclaw/.venvs/crawl4ai`
- **Activate:** `. /home/openclaw/.venvs/crawl4ai/bin/activate`
- **Python path:** `/home/openclaw/.venvs/crawl4ai/bin/python`
- **Crawl4AI version:** 0.8.6
- **Browser:** Playwright Chromium (headless)
- **Output mặc định:** `/home/openclaw/.openclaw/skills/data-scraping/output/`

## Quy trình khi người dùng yêu cầu crawl

**QUAN TRỌNG:** Khi người dùng yêu cầu crawl/scrape bất kỳ trang nào, PHẢI hỏi tùy chọn trước khi thực hiện. Trình bày các lựa chọn rõ ràng:

---

📥 **Bạn muốn cào dữ liệu theo cách nào?**

**1️⃣ Nội dung cơ bản** — Lấy toàn bộ nội dung trang dạng markdown sạch
**2️⃣ Dữ liệu có cấu trúc** — Trích xuất theo CSS selector (bảng, danh sách, tiêu đề...)
**3️⃣ Crawl nhiều trang** — Crawl hàng loạt nhiều URL cùng lúc
**4️⃣ Crawl toàn site** — Tự động theo link và crawl nhiều trang của cùng domain
**5️⃣ Lấy link** — Chỉ lấy danh sách tất cả link trên trang
**6️⃣ Screenshot** — Chụp ảnh màn hình trang web
**7️⃣ Xuất file** — Lưu kết quả ra file (markdown / JSON / CSV)

Sau khi người dùng chọn, hỏi thêm:
- **Output muốn làm gì?** (đọc tại đây / lưu file / upload Drive / xử lý tiếp)
- **Có cần lọc nội dung không?** (chỉ lấy bài viết, bỏ menu/quảng cáo...)

---

## Khi nào dùng
- Người dùng yêu cầu crawl/scrape nội dung từ 1 hoặc nhiều URL
- Cần trích xuất dữ liệu có cấu trúc từ web (bảng, danh sách, sản phẩm...)
- Cần chuyển nội dung web sang markdown sạch để xử lý tiếp
- Cần crawl hàng loạt (batch crawl) nhiều trang cùng domain
- Cần screenshot trang web

## Khi không dùng
- Chỉ cần tìm kiếm nhanh thông tin → dùng `web_search`
- Chỉ cần đọc nội dung đơn giản 1 trang → dùng `web_fetch`
- Trang web không cần JavaScript rendering

## Instruction

### 1. Crawl đơn trang (Basic)

```python
#!/usr/bin/env python3
"""Crawl một trang web và lấy markdown."""
import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode

async def crawl_single(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
            cache_mode=CacheMode.BYPASS
        )
        if result.success:
            return result.markdown.raw_markdown
        else:
            return f"Error: {result.error_message}"

url = "https://example.com"
content = asyncio.run(crawl_single(url))
print(content)
```

### 2. Crawl với CSS Selector (Chọn vùng cụ thể)

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig

async def crawl_with_selector(url, css_selector):
    config = CrawlerRunConfig(
        css_selector=css_selector,
        cache_mode=CacheMode.BYPASS
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, config=config)
        if result.success:
            return result.markdown.raw_markdown
        else:
            return f"Error: {result.error_message}"

content = asyncio.run(crawl_with_selector(
    "https://example.com",
    "article.main-content"
))
print(content)
```

### 3. Crawl nhiều trang (Batch)

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig

async def crawl_batch(urls):
    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun_many(
            urls=urls,
            config=config
        )
        return {r.url: r.markdown.raw_markdown for r in results if r.success}

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
]
all_content = asyncio.run(crawl_batch(urls))
for url, content in all_content.items():
    print(f"=== {url} ===")
    print(content[:500])
```

### 4. Trích xuất dữ liệu có cấu trúc (JSON Schema)

```python
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def extract_structured(url, schema):
    strategy = JsonCssExtractionStrategy(schema)
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=strategy
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, config=config)
        if result.success:
            return json.loads(result.extracted_content)
        return None

# Ví dụ schema trích xuất danh sách sản phẩm
schema = {
    "name": "Products",
    "baseSelector": "div.product-item",
    "fields": [
        {"name": "title", "selector": "h2.product-title", "type": "text"},
        {"name": "price", "selector": "span.price", "type": "text"},
        {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"},
    ]
}

data = asyncio.run(extract_structured("https://example.com/products", schema))
print(json.dumps(data, indent=2, ensure_ascii=False))
```

### 5. Crawl trang cần chờ JavaScript render

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig

async def crawl_js_heavy(url, wait_for_selector=None):
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        wait_for=f"css:{wait_for_selector}" if wait_for_selector else None,
        page_timeout=30000,
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, config=config)
        if result.success:
            return result.markdown.raw_markdown
        return f"Error: {result.error_message}"

content = asyncio.run(crawl_js_heavy(
    "https://example.com/spa",
    wait_for_selector="div.content-loaded"
))
print(content)
```

### 6. Chụp screenshot

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig

async def screenshot(url, output_path):
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        screenshot=True
    )
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, config=config)
        if result.success and result.screenshot:
            import base64
            img_data = base64.b64decode(result.screenshot)
            with open(output_path, 'wb') as f:
                f.write(img_data)
            return f"Screenshot saved: {output_path}"
        return "Failed"

result = asyncio.run(screenshot(
    "https://example.com",
    "/home/openclaw/.openclaw/skills/data-scraping/output/screenshot.png"
))
print(result)
```

### 7. Xuất kết quả ra file

```python
import asyncio
import json
import csv
from crawl4ai import AsyncWebCrawler, CacheMode

OUTPUT_DIR = "/home/openclaw/.openclaw/skills/data-scraping/output"

async def crawl_and_save(url, filename, fmt="markdown"):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, cache_mode=CacheMode.BYPASS)
        if not result.success:
            return f"Error: {result.error_message}"

        filepath = f"{OUTPUT_DIR}/{filename}"

        if fmt == "markdown":
            filepath += ".md"
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result.markdown.raw_markdown)

        elif fmt == "json":
            filepath += ".json"
            data = {
                "url": result.url,
                "title": result.metadata.get("title", ""),
                "content": result.markdown.raw_markdown,
            }
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

        return f"Saved: {filepath}"

result = asyncio.run(crawl_and_save(
    "https://example.com",
    "example_content",
    fmt="markdown"
))
print(result)
```

## Quy trình thực hiện (Workflow) — BẮT BUỘC

### ⚠️ QUY TẮC SỐ 1: LUÔN GỢI Ý TRƯỚC — KHÔNG TỰ Ý CHẠY

Khi người dùng yêu cầu crawl/cào/scrape, **KHÔNG được tự ý chạy ngay**. Phải đưa ra menu gợi ý để người dùng chọn trước.

### Bước 1: Phân tích URL & đưa gợi ý

Sau khi nhận URL từ người dùng, **trả lời với menu gợi ý** theo format sau:

```
🔍 Phân tích: <url>

Anh muốn cào kiểu nào?

1️⃣ **Toàn bộ nội dung** → Lấy hết markdown
2️⃣ **Chỉ nội dung chính** → Bỏ header/footer/sidebar
3️⃣ **Trích xuất dữ liệu** → Lấy bảng/danh sách/sản phẩm ra JSON
4️⃣ **Chụp ảnh trang** → Screenshot
5️⃣ **Crawl sâu** → Theo link con cùng domain

📦 Output: markdown | json | csv
⚙️ Tùy chọn thêm: CSS selector, chờ JS load, số trang tối đa

Anh chọn số mấy? (hoặc mô tả thêm yêu cầu)
```

### Bước 2: Nhận lựa chọn & xác nhận

Sau khi người dùng chọn, **xác nhận lại 1 lần** trước khi chạy:

```
✅ OK, em sẽ:
- Crawl: <url>
- Kiểu: <mô tả>
- Output: <format>
- Lưu tại: <filepath>

Chạy luôn không anh?
```

### Bước 3: Viết script & chạy crawl
- Tạo file Python trong `/home/openclaw/.openclaw/skills/data-scraping/scripts/`
- Sử dụng các pattern phù hợp từ các ví dụ ở trên
- Luôn dùng `~/crawl4ai-venv/bin/python` để chạy

```bash
~/crawl4ai-venv/bin/python /home/openclaw/.openclaw/skills/data-scraping/scripts/<ten_script>.py
```

### Bước 4: Kiểm tra & trả kết quả
- Kiểm tra file output trong `/home/openclaw/.openclaw/skills/data-scraping/output/`
- Gửi file hoặc nội dung trực tiếp cho người dùng
- Tóm tắt kết quả: số ký tự, số mục trích xuất được, thời gian crawl

## Lưu ý quan trọng

1. **Luôn dùng venv:** `~/crawl4ai-venv/bin/python` — KHÔNG dùng `python3` hệ thống
2. **NumPy:** Đã pin ở version 2.0.2 (tương thích CPU). KHÔNG upgrade numpy
3. **Headless mode:** Chromium luôn chạy headless trong môi trường server
4. **Rate limiting:** Khi crawl nhiều trang, nên thêm delay giữa các request
5. **Cache:** Mặc định dùng `CacheMode.BYPASS` để lấy dữ liệu mới nhất
6. **Timeout:** Mặc định 30s, có thể tăng với `page_timeout` cho trang chậm
7. **Output dir:** Lưu kết quả vào `./output/` trong thư mục skill
