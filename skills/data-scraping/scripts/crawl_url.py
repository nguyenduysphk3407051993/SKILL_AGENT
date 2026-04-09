#!/usr/bin/env python3
"""
Universal crawl script - Crawl một hoặc nhiều URL.
Usage:
    python crawl_url.py <url> [--format markdown|json] [--selector "css"] [--output filename]
    python crawl_url.py <url1> <url2> ... [--format markdown|json]
"""
import asyncio
import argparse
import json
import os
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig

OUTPUT_DIR = "/home/openclaw/.openclaw/skills/data-scraping/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


async def crawl_single(crawler, url, css_selector=None):
    """Crawl a single URL."""
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        css_selector=css_selector,
        page_timeout=30000,
    )
    result = await crawler.arun(url=url, config=config)
    return result


async def main(args):
    async with AsyncWebCrawler() as crawler:
        for url in args.urls:
            print(f"\n🔍 Crawling: {url}")
            result = await crawl_single(crawler, url, args.selector)

            if not result.success:
                print(f"❌ Failed: {result.error_message}")
                continue

            content = result.markdown.raw_markdown
            title = result.metadata.get("title", "untitled") if result.metadata else "untitled"
            print(f"✅ Success: {len(content)} chars | Title: {title}")

            if args.output:
                # Save to file
                if args.format == "json":
                    filepath = os.path.join(OUTPUT_DIR, f"{args.output}.json")
                    data = {
                        "url": result.url,
                        "title": title,
                        "content": content,
                    }
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                else:
                    filepath = os.path.join(OUTPUT_DIR, f"{args.output}.md")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(f"# {title}\n\n")
                        f.write(f"Source: {result.url}\n\n---\n\n")
                        f.write(content)
                print(f"💾 Saved: {filepath}")
            else:
                # Print to stdout
                print(f"\n--- Content ---\n{content[:2000]}")
                if len(content) > 2000:
                    print(f"\n... (truncated, total {len(content)} chars)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl URLs with Crawl4AI")
    parser.add_argument("urls", nargs="+", help="URL(s) to crawl")
    parser.add_argument("--format", "-f", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--selector", "-s", help="CSS selector to extract specific content")
    parser.add_argument("--output", "-o", help="Output filename (without extension)")
    args = parser.parse_args()

    asyncio.run(main(args))
