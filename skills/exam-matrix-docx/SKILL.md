---
name: exam-matrix-docx
description: Trích xuất ma trận đề thi từ DOCX/PDF/TXT/Markdown sang JSON chuẩn (EX/TF/SA/BT), tạo câu hỏi theo ma trận thành Markdown đúng form, rồi chuyển Markdown sang DOCX bằng logic xử lý tương đương script PyQt6 (không cần GUI). Use when user yêu cầu tạo đề cương/đề thi .docx từ file ma trận nhiều định dạng.
---

# Exam Matrix → DOCX

## Quy trình

1. Nhận file ma trận đầu vào (ưu tiên DOCX/TXT/PDF).
2. Trích xuất thành JSON theo schema:
   - `thong_tin_chung`
   - `bang_dac_ta[]`
   - key dạng câu hỏi: `EX`, `TF`, `SA`, `BT`
3. Sinh đề/câu hỏi dạng Markdown đúng format hệ thống user yêu cầu.
4. Chuyển Markdown → DOCX bằng script CLI:
   - `scripts/md_to_docx_core.py`
   - giữ logic xử lý markdown (bảo vệ bảng, dàn trang đáp án A/B/C/D, tô màu phần bold, tab stop, font Times New Roman).

## User preferences cần giữ mặc định (Telegram user 7638885552)

- Khi user yêu cầu “tạo đề theo ma trận”, ưu tiên xuất luôn file `.docx` (không chỉ trả text).
- Bố cục đề có tiêu đề chính + tiêu đề từng phần (PHẦN I/II/III...) giống mẫu docx user gửi.
- Nếu user nói "loại 3" thì hiểu là **trả lời ngắn dạng số** (SA) với bảng đáp án 4 ô.
- Nếu user nói "loại 2" thì hiểu là **đúng/sai** (TF), hỗ trợ cả dạng thường và dạng bảng.
- Luôn giữ định dạng markdown trung gian tương thích script chuyển docx trước khi xuất file.

## Chạy chuyển đổi Markdown sang DOCX (không GUI)

```bash
/home/openclaw/.openclaw/workspace/venvs/md2docx/bin/python \
  skills/exam-matrix-docx/scripts/md_to_docx_core.py \
  --input /path/to/input.md \
  --output /path/to/output.docx
```

Tùy chọn template:

```bash
/home/openclaw/.openclaw/workspace/venvs/md2docx/bin/python \
  skills/exam-matrix-docx/scripts/md_to_docx_core.py \
  --input /path/to/input.md \
  --output /path/to/output.docx \
  --template /path/to/template.docx
```

## Tham chiếu

- `references/json-schema-example.md`: mẫu JSON ma trận cần map.
- `references/markdown-output-rules.md`: quy tắc output markdown nghiêm ngặt cho 4 loại câu hỏi.
