---
name: camofox-browser
description: "Skill duyệt web anti-detection sử dụng Camoufox (Firefox-based). Dùng khi cần truy cập website có chống bot (Google, Amazon, LinkedIn, YouTube...), điều khiển trình duyệt tự động, chụp screenshot, lấy transcript YouTube, import cookies xác thực, hoặc tương tác với trang web SPA/JS-heavy."
allowed-tools: camofox_create_tab, camofox_snapshot, camofox_click, camofox_type, camofox_navigate, camofox_scroll, camofox_screenshot, camofox_close_tab, camofox_evaluate, camofox_list_tabs, camofox_import_cookies, Read, Write, Exec
argument-hint: "[url hoặc macro tìm kiếm] [hành động: browse|search|screenshot|transcript|interact]"
---

# Skill: Camofox Anti-Detection Browser

## Description
Skill này sử dụng **Camoufox Browser** — trình duyệt Firefox-based anti-detection tích hợp qua plugin OpenClaw. Camofox bypass được bot detection trên hầu hết các website (Google, Amazon, LinkedIn, YouTube, Instagram, TikTok...) nhờ fingerprint giả lập, humanize interactions, và proxy geoip.

**Server:** `http://localhost:9377` (auto-start cùng Gateway)
**Engine:** Camoufox (Playwright Firefox + anti-fingerprint)

## Khi nào dùng
- Truy cập website có **chống bot/anti-scraping** (Google, LinkedIn, Amazon, YouTube...)
- Cần **tương tác với trang web** (click, type, scroll, fill form...)
- Cần **chụp screenshot** hoặc lấy **accessibility snapshot** của trang
- Cần **lấy transcript YouTube** video
- Cần **import cookies** để đăng nhập sẵn vào website
- Cần **chạy JavaScript** trong context trang web
- Cần **tìm kiếm web** qua macro (@google_search, @youtube_search, @amazon_search...)
- Website là **SPA/JS-heavy** cần rendering đầy đủ
- Cần bypass **CAPTCHA/consent dialog** (auto-dismiss)

## Khi không dùng
- Chỉ cần **tìm kiếm thông tin** nhanh → dùng `web_search`
- Chỉ cần **đọc nội dung** đơn giản 1 trang tĩnh → dùng `web_fetch`
- Cần **crawl hàng loạt** nhiều trang → dùng skill `data-scraping` (Crawl4AI)
- Website **không chống bot** và chỉ cần text → dùng `web_fetch`

## Tools Reference

### 1. `camofox_create_tab` — Mở tab mới
Tạo tab trình duyệt mới, navigate tới URL. Trả về `tabId` để dùng cho các thao tác tiếp theo.

```
Params: { url: string }
Returns: { tabId: string, url: string, title: string }
```

### 2. `camofox_snapshot` — Lấy accessibility snapshot + screenshot
Lấy cây accessibility (dạng YAML) với ref id (e1, e2, e3...) để click/type, kèm screenshot. Trang lớn sẽ phân trang — dùng `offset` để xem tiếp.

```
Params: { tabId: string, offset?: number }
Returns: { url, refsCount, snapshot (YAML), screenshot (image), truncated?, hasMore?, nextOffset? }
```

### 3. `camofox_click` — Click element
Click element bằng ref (e1, e2...) từ snapshot hoặc CSS selector.

```
Params: { tabId: string, ref?: string, selector?: string }
```

### 4. `camofox_type` — Nhập text
Nhập text vào input/textarea. Có thể kết hợp pressEnter.

```
Params: { tabId: string, text: string, ref?: string, selector?: string, pressEnter?: boolean }
```

### 5. `camofox_navigate` — Chuyển trang hoặc tìm kiếm
Navigate tới URL hoặc dùng **search macro** để tìm kiếm trực tiếp.

```
Params: { tabId: string, url?: string, macro?: string, query?: string }

Macros có sẵn:
  @google_search    — Google Search
  @youtube_search   — YouTube
  @amazon_search    — Amazon
  @reddit_search    — Reddit
  @wikipedia_search — Wikipedia
  @twitter_search   — Twitter/X
  @linkedin_search  — LinkedIn
  @instagram_search — Instagram
  @tiktok_search    — TikTok
  @twitch_search    — Twitch
  @yelp_search      — Yelp
  @spotify_search   — Spotify
  @netflix_search   — Netflix
```

### 6. `camofox_scroll` — Cuộn trang
```
Params: { tabId: string, direction: "up"|"down"|"left"|"right", amount?: number }
```

### 7. `camofox_screenshot` — Chụp ảnh trang
Trả về ảnh PNG base64 của trang hiện tại.
```
Params: { tabId: string }
```

### 8. `camofox_evaluate` — Chạy JavaScript
Chạy JavaScript expression trong context trang web. Dùng để đọc DOM, gọi API trang, inject script.
```
Params: { tabId: string, expression: string }
```

### 9. `camofox_list_tabs` — Liệt kê tabs
```
Params: {} (không cần)
Returns: [{ tabId, userId, url, title }]
```

### 10. `camofox_close_tab` — Đóng tab
```
Params: { tabId: string }
```

### 11. `camofox_import_cookies` — Import cookies
Import file cookies Netscape format để đăng nhập sẵn. File cookies nằm trong `~/.camofox/cookies/`.
```
Params: { cookiesPath: string, domainSuffix?: string }
```

## Workflow — Quy trình sử dụng

### Quy trình chuẩn: Browse & Interact

```
1. camofox_create_tab(url) → nhận tabId
2. camofox_snapshot(tabId)  → xem cấu trúc trang + screenshot
3. Dùng ref (e1, e2...) để:
   - camofox_click(tabId, ref) — click link/button
   - camofox_type(tabId, ref, text) — nhập text vào input
   - camofox_scroll(tabId, direction) — cuộn trang
4. Lặp lại snapshot → interact cho đến khi xong
5. camofox_close_tab(tabId) — dọn dẹp
```

### Quy trình: Google Search

```
1. camofox_create_tab(url: "https://www.google.com")
2. camofox_navigate(tabId, macro: "@google_search", query: "từ khóa")
3. camofox_snapshot(tabId) → đọc kết quả SERP (đã được optimize riêng cho Google)
4. camofox_click(tabId, ref: "e3") → click vào kết quả
5. camofox_snapshot(tabId) → đọc nội dung trang đích
```

### Quy trình: YouTube Transcript

```
POST http://localhost:9377/youtube/transcript
Body: { "url": "https://youtube.com/watch?v=...", "languages": ["vi", "en"] }

Hỗ trợ:
- yt-dlp (ưu tiên, nhanh)
- Browser fallback (tự mở video, intercept captions)
```

Hoặc dùng `exec` gọi trực tiếp:
```bash
curl -s -X POST http://localhost:9377/youtube/transcript \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://youtube.com/watch?v=VIDEO_ID","languages":["en"]}'
```

### Quy trình: Import Cookies (Login sẵn)

```
1. Đặt file cookies.txt (Netscape format) vào ~/.camofox/cookies/
2. camofox_import_cookies(cookiesPath: "linkedin_cookies.txt", domainSuffix: ".linkedin.com")
3. camofox_create_tab(url: "https://linkedin.com") → đã đăng nhập
```

## Tính năng đặc biệt

### Auto-dismiss Consent Dialogs
Camoufox tự động tắt các popup cookie consent, privacy dialog (OneTrust, GDPR, CCPA) khi load trang.

### Google SERP Optimization
Khi truy cập Google Search, snapshot được tối ưu riêng — trả về kết quả sạch với title, URL, snippet, pagination.

### Snapshot Pagination
Trang lớn được cắt tự động (~80K chars). Nếu `hasMore=true`, gọi lại `camofox_snapshot(tabId, offset: nextOffset)` để xem tiếp. Phần cuối trang (navigation/pagination) luôn được giữ lại.

### Browser Health & Auto-Recovery
- Tự restart browser khi phát hiện lỗi liên tiếp
- Auto-destroy tab bị stuck (sau 3 consecutive timeouts)
- Idle shutdown sau 5 phút không có session
- Per-user concurrency limit (3 thao tác đồng thời)

### Tab Lock Serialization
Mỗi tab có lock riêng — các thao tác trên cùng 1 tab được serialize để tránh race condition.

## Cấu hình Server

| Biến môi trường | Mặc định | Mô tả |
|---|---|---|
| `CAMOFOX_PORT` | 9377 | Port server |
| `MAX_SESSIONS` | 50 | Số session tối đa |
| `MAX_TABS_PER_SESSION` | 10 | Tabs/session |
| `MAX_TABS_GLOBAL` | 10 | Tổng tabs toàn hệ thống |
| `SESSION_TIMEOUT_MS` | 600000 | Session timeout (10 phút) |
| `BROWSER_IDLE_TIMEOUT_MS` | 300000 | Browser idle (5 phút) |
| `NAVIGATE_TIMEOUT_MS` | 25000 | Navigate timeout |
| `BUILDREFS_TIMEOUT_MS` | 12000 | Snapshot build timeout |
| `PROXY_HOST/PORT/USERNAME/PASSWORD` | — | Proxy config |
| `CAMOFOX_API_KEY` | — | API key cho cookie import |

## Lưu ý quan trọng

1. **Luôn đóng tab** sau khi dùng xong (`camofox_close_tab`) để giải phóng tài nguyên
2. **Snapshot trước khi interact** — cần ref id để click/type chính xác
3. **Dùng ref thay vì selector** khi có thể — ref từ snapshot đã được disambiguate
4. **Trang nặng JS:** Snapshot có thể mất 5-12s, không timeout sớm
5. **Cookie import:** Cần `CAMOFOX_API_KEY` được set trong env
6. **Proxy:** Khi có proxy, Camoufox tự detect locale/timezone/geolocation từ IP
7. **Google SERP:** Không cần scroll — snapshot đã trích xuất đầy đủ kết quả
8. **Max 10 tabs global** — đóng tab cũ trước khi mở mới nếu đạt giới hạn
