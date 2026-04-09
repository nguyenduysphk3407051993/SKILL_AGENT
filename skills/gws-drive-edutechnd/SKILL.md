---
name: gws-drive-edutechnd
description: "Upload tài liệu lên Google Drive OPENCLAW và tự động phân loại vào đúng thư mục."
metadata:
  version: 1.0.0
  openclaw:
    category: "productivity"
    requires:
      bins:
        - gws
---

# gws-drive-edutechnd — Upload & Phân loại tài liệu

> Upload file lên Google Drive OPENCLAW, tự động phân loại vào thư mục phù hợp dựa trên nội dung/loại file.

## Cây thư mục Drive OPENCLAW

```
OPENCLAW/  (id: 15yux2MyPNwEuUh-tUKW1__rWLTA_kn9D)
├── DOCUMENT/  (id: 1Dsj4dd9YaGM5iyGOBAcXCWuy2AmheXtY)
│   ├── LOP_6/   (id: 1v_I65II8e54o_gYez_8MDv0hroBs4Ydb)   ← tài liệu lớp 6
│   ├── LOP_7/   (id: 1diwIn2A7VOWplxwv5pxPSet7sJxYav4Z)   ← tài liệu lớp 7
│   ├── KTTX/    (id: 1t7OboOjq84VLUFnnwK969xENcfYUxajX)   ← kiểm tra thường xuyên
│   ├── DSHS/    (id: 1REorHtrqj06gpuJxe_KM0VwqL9hZ4Is0)   ← danh sách học sinh
│   ├── EMAIL/   (id: 1EnjXzT8Lgl2kX2PU9vHrKp6UMm0DsZ5o)   ← tài liệu email/thông báo
│   ├── LUAT/    (id: 1u-u_Rf47Nvb4olyhYFTm842ALCWXwr75)    ← văn bản pháp luật
│   └── KHAC/    (id: 12m3DskzoElc9ITFCKLFATHLar9dmnd74)    ← tài liệu khác
├── IMAGES/  (id: 1-zFZNM-oZ0xpG6WybLA_F97ie0sdbfc8)        ← ảnh (.jpg, .png, .gif...)
├── AUDIO/   (id: 19msCccCoiAbaAZupcQVPot3sg6WyoK4w)        ← âm thanh (.mp3, .wav, .ogg...)
├── VIDEO/   (id: 17m9kOTc1d08LpdppE5Y-1WcqZN0EQUgD)        ← video (.mp4, .mkv, .avi...)
├── SOFT/    (id: 1HUKTTMOtjHljpFsKKT-cIvjcdTIqtDdu)        ← phần mềm (.exe, .rar, .zip...)
└── Bat_Dang_Thuc_THCS/  (id: 1gtth1hItptP2afZIexCHK0s1V46sa4xe)  ← tài liệu bất đẳng thức THCS
```

## Quy tắc phân loại tự động

### 1. Theo loại file (MIME type)
| Loại file | Thư mục đích |
|-----------|-------------|
| image/* (.jpg, .png, .gif, .webp, .svg) | `IMAGES/` |
| audio/* (.mp3, .wav, .ogg, .m4a) | `AUDIO/` |
| video/* (.mp4, .mkv, .avi, .mov) | `VIDEO/` |
| .exe, .rar, .zip (phần mềm) | `SOFT/` |

### 2. Theo nội dung/tên file (DOCUMENT)
| Từ khóa trong tên | Thư mục đích |
|-------------------|-------------|
| `lop_6`, `lớp 6`, `6A`, `6B`, `KHTN6`, `lich_su_6`, `sinh_6`, `hoa_6` | `DOCUMENT/LOP_6/` |
| `lop_7`, `lớp 7`, `7A`, `7B`, `KHTN7`, `hoa_7`, `sinh_7` | `DOCUMENT/LOP_7/` |
| `KTTX`, `kiem_tra_thuong_xuyen`, `kiem tra thường xuyên`, `15phut` | `DOCUMENT/KTTX/` |
| `danh_sach`, `danh sách`, `DSHS`, `hoc_sinh`, `sĩ số` | `DOCUMENT/DSHS/` |
| `email`, `thong_bao`, `thông báo`, `mau_email` | `DOCUMENT/EMAIL/` |
| `luat`, `luật`, `nghi_dinh`, `thong_tu`, `quy_dinh`, `van_ban` | `DOCUMENT/LUAT/` |
| `bat_dang_thuc`, `BDT`, `bất đẳng thức`, `HSG`, `thi_vao_10` | `Bat_Dang_Thuc_THCS/` |
| Không khớp → | `DOCUMENT/KHAC/` |

## Cách upload

```bash
# Upload file lên Drive, tự chọn thư mục đích
gws drive files create \
  --params '{"uploadType":"multipart"}' \
  --body '{"name":"<tên_file>","parents":["<folder_id>"]}' \
  --media <đường_dẫn_file>
```

## Quy trình khi người dùng yêu cầu upload

1. **Luôn bắt đầu từ thư mục cha `OPENCLAW/`** — không tự ý upload/làm việc ở thư mục Drive khác nếu người dùng chưa yêu cầu
2. **Nhận file** từ người dùng (path hoặc URL)
3. **Phân tích tên file + loại file** theo bảng quy tắc trên để chọn **thư mục con phù hợp bên trong `OPENCLAW/`**
4. **Xác nhận với người dùng** thư mục con sẽ upload vào nếu có mơ hồ hoặc nhiều khả năng khớp
5. **Upload** bằng `gws drive files create`
6. **Trả về link** file vừa upload và nêu rõ đã xếp vào thư mục con nào trong `OPENCLAW/`

## Quy tắc bắt buộc

- Khi người dùng nói upload tài liệu lên Drive/driver, mặc định hiểu là upload vào cây thư mục dưới **`OPENCLAW/`**
- **Không tự ý làm việc ở thư mục cha/đích khác** ngoài `OPENCLAW/` trừ khi người dùng chỉ định rõ
- **Tự phân loại và sắp xếp** vào thư mục con phù hợp nhất trong cây `OPENCLAW/`
- Nếu không tìm thấy nhóm phù hợp rõ ràng, dùng `DOCUMENT/KHAC/` trong `OPENCLAW/`
- Nếu cần tạo cấu trúc con mới, phải hỏi người dùng trước

## Ví dụ

**Upload ảnh:**
```bash
gws drive files create \
  --params '{"uploadType":"multipart"}' \
  --body '{"name":"anh_lop_6.jpg","parents":["1-zFZNM-oZ0xpG6WybLA_F97ie0sdbfc8"]}' \
  --media /path/to/anh_lop_6.jpg
```

**Upload đề kiểm tra lớp 6:**
```bash
gws drive files create \
  --params '{"uploadType":"multipart"}' \
  --body '{"name":"De_KTTX_Toan_6A.pdf","parents":["1t7OboOjq84VLUFnnwK969xENcfYUxajX"]}' \
  --media /path/to/De_KTTX_Toan_6A.pdf
```

## Lấy link chia sẻ sau khi upload

```bash
gws drive permissions create \
  --params '{"fileId":"<file_id>","sendNotificationEmail":"false"}' \
  --body '{"role":"reader","type":"anyone"}'
```
