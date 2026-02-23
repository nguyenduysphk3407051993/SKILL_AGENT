---
name: update-claude
description: Cập nhật file CLAUDE.md dựa trên thay đổi trong codebase. Sử dụng khi có thay đổi lớn trong project hoặc khi muốn đồng bộ documentation với code hiện tại.
allowed-tools: Read, Glob, Grep, Edit, Write
argument-hint: [focus-area]
---

# Update CLAUDE.md Skill

Khi được gọi, skill này sẽ phân tích codebase và cập nhật file CLAUDE.md để phản ánh trạng thái hiện tại của project.

## Các bước thực hiện

1. **Đọc CLAUDE.md hiện tại** (nếu có)
2. **Quét codebase** để tìm:
   - Các file và thư mục mới
   - Dependencies và tech stack
   - Các function/class quan trọng
   - Patterns và conventions đang sử dụng
3. **So sánh** với nội dung CLAUDE.md hiện tại
4. **Cập nhật** các section cần thiết

## Focus areas (tùy chọn)

Nếu người dùng truyền argument `$ARGUMENTS`, tập trung vào area đó:
- `structure` - Cập nhật cấu trúc project
- `features` - Cập nhật danh sách tính năng
- `tech` - Cập nhật tech stack
- `conventions` - Cập nhật code conventions
- `all` - Cập nhật toàn bộ (mặc định)

## Format CLAUDE.md chuẩn

```markdown
# Project Name

## Project Overview
[Mô tả ngắn gọn về project]

## Tech Stack
[Liệt kê các công nghệ sử dụng]

## Project Structure
[Cấu trúc thư mục và file chính]

## Key Features
[Các tính năng chính]

## Development
[Hướng dẫn chạy và phát triển]

## Code Conventions
[Quy ước code trong project]
```

## Lưu ý

- Giữ nguyên các section custom mà người dùng đã thêm
- Không xóa thông tin quan trọng, chỉ cập nhật hoặc bổ sung
- Viết ngắn gọn, súc tích
- Dùng tiếng Việt nếu project dùng tiếng Việt, ngược lại dùng tiếng Anh
