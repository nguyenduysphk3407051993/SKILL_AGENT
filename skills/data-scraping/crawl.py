#!/usr/bin/env python3
"""
Crawl4AI wrapper script — dùng với venv /home/openclaw/.venvs/crawl4ai
Usage: python crawl.py <url> [--format markdown|json] [--selector CSS]
"""
import asyncio
import sys
import json
import argparse
from crawl4ai import AsyncWebCrawler, CacheMode

async def crawl(url, output_format="markdown", css_selector=None, wait_for=None):
    async with AsyncWebCrawler(verbose=False) as crawler:
        kwargs = dict(
            url=url,
            cache_mode=CacheMode.BYPASS,
        )
        if css_selector:
            kwargs["css_selector"] = css_selector
        if wait_for:
            kwargs["wait_for"] = wait_for

        result = await crawler.arun(**kwargs)

        if not result.success:
            print(f"ERROR: {result.error_message}", file=sys.stderr)
            sys.exit(1)

        if output_format == "json":
            out = {
                "url": url,
                "title": result.metadata.get("title", "") if result.metadata else "",
                "markdown": result.markdown,
                "links": result.links,
            }
            print(json.dumps(out, ensure_ascii=False, indent=2))
        else:
            print(result.markdown)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--format", default="markdown", choices=["markdown", "json"])
    parser.add_argument("--selector", default=None)
    parser.add_argument("--wait-for", default=None)
    args = parser.parse_args()

    asyncio.run(crawl(
        url=args.url,
        output_format=args.format,
        css_selector=args.selector,
        wait_for=args.wait_for,
    ))
