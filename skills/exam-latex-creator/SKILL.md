---
name: exam-latex-creator
description: "Skill tạo câu hỏi/bài tập LaTeX cho giáo dục Việt Nam (THCS & THPT). Sử dụng khi cần soạn câu hỏi loại 1 (trắc nghiệm), loại 2 (đúng/sai), loại 3 (trả lời ngắn), loại 4 (tự luận) cho các môn KHTN, Toán,Vật lý, Hóa học, sinh học,lịch sử, địa lý, ngữ văn theo chuẩn LaTeX."
allowed-tools: Read, Write, Glob, Grep, WebFetch, Exec
argument-hint: "[loại câu hỏi] [số lượng] [chủ đề/chương/bài]"
---

# Skill: Vietnamese Education LaTeX Generator

## Description
Skill này chuyên dùng để tạo các câu hỏi theo chủ đề/chương, bài, dạng (Toán, Lý, Hóa, Sinh, KHTN, Ngữ Văn) theo định dạng LaTeX chuẩn, tuân thủ nghiêm ngặt cấu trúc của chương trình giáo dục Việt Nam (THCS & THPT).

## Usage

### 1. Khi nào dùng
* **Soạn thảo mới:** Khi người dùng yêu cầu soạn các câu hỏi loại 1, loại 2, loại 3, loại 4 thuộc các môn KHTN (Lý, Hóa, Sinh), Toán, Văn dưới dạng mã nguồn LaTeX.
* **Trích xuất & Chuyển đổi:** Khi người dùng cung cấp tài liệu đầu vào là **file ảnh (PNG, JPG,...)** hoặc **file PDF** và yêu cầu số hóa, chuyển đổi nội dung từ các file này sang định dạng câu hỏi LaTeX.
* **Tạo đề thi theo mấu template có sẵn**
* **Yêu cầu giữ nguyên gốc:** Khi cần chuyển đổi định dạng từ tài liệu tĩnh (ảnh/PDF) sang tài liệu động (LaTeX) mà vẫn đảm bảo tính toàn vẹn của nội dung, thông số và ngữ nghĩa từ file gốc.

### 2. Khi không dùng
* Khi người dùng chỉ hỏi kiến thức thông thường, yêu cầu giải thích bằng văn bản đơn thuần (plain text/markdown).
* Khi người dùng không yêu cầu định dạng code hoặc không có nhu cầu sử dụng mã nguồn LaTeX.
* Khi người dùng yêu cầu sáng tạo nội dung mới hoàn toàn không dựa trên tài liệu đính kèm.

## Instruction

***Role:*** Bạn là chuyên gia trong tạo ra các loại câu hỏi theo dạng thuộc chủ đề khác nhau của môn học thuộc chương trình lớp 6, 7, 8, 9, 10, 11, 12.

***Cấu trúc câu hỏi chuẩn (BẮT BUỘC):***

### Câu hỏi loại 1 (Trắc nghiệm nhiều lựa chọn):
```latex
%%%============EX_<số thứ tự>=============%%%
\begin{ex}%[ID6]
    Nội dung câu hỏi trắc nghiệm nhiều lựa chọn
    \choice
    {Nội dung phương án A}
    {Nội dung phương án B}
    {\True Nội dung phương án C (Đúng)}
    {Nội dung phương án D}
    \loigiai{Nội dung lời giải chi tiết.}
\end{ex}
```

### Câu hỏi loại 2 (Trắc nghiệm Đúng/Sai):
```latex
%%%=============TF_<số thứ tự>=============%%%
\begin{ex}%[ID6]
    Nội dung câu hỏi trắc nghiệm đúng sai
    \choiceTF
    {\True Nội dung phương án đúng}
    {Nội dung phương án sai}
    {\True Nội dung phương án đúng}
    {\True Nội dung phương án đúng}
    \loigiai{
        \begin{itemchoice}[T1,F2,T3,T4] 
            \itemch Lời giải chi tiết ý a.
            \itemch Lời giải chi tiết ý b.
            \itemch Lời giải chi tiết ý c.
            \itemch Lời giải chi tiết ý d.
        \end{itemchoice}
    }
\end{ex}
```

### Câu hỏi loại 3 (Trả lời ngắn):
```latex
%%%=============SA_<Số thứ tự>==============%%%
\begin{ex}%[ID6]
    Nội dung bài tập trả lời ngắn
    \shortans{Đáp án dạng số} % Lưu ý: Chỉ điền SỐ hoặc KÝ TỰ ĐƠN GIẢN (tránh tiếng Việt có dấu trong {} để không lỗi UTF-8)
    \loigiai{Nội dung Lời giải chi tiết.}
\end{ex}
```

### Câu hỏi loại 4 (Tự luận):
```latex
%%%=============BT_<số thứ tự>=============%%%
\begin{bt}%[ID6]
    Nội dung câu hỏi tự luận
    \loigiai{Nội dung lời giải chi tiết bài tập tự luận.}
\end{bt}
```

***Yêu cầu nghiêm ngặt***
#Cấu trúc:
## Phải theo đúng chuẩn form từng loại câu hỏi tôi nêu trên
### Đối với câu hỏi loại 1:
- Lệnh choice bắt buộc phải đủ 4 tham số và chỉ có 1 phương án đúng  \choice{}{}{}{} ( tương ứng với 4 phương án ) không được bỏ trống trong đó  chỉ phương án đúng mới đặt lệnh \True phía trước phương án
- Các phương án không có dấu chấm ở cuối
### Đối với câu hỏi loại 2:
- Lệnh choiceTF bắt buộc phải đủ 4 tham số \choiceTF{}{}{}{} ( tương ứng với 4 phương án ) không được bỏ trống trong đó phương án đúng phải đặt lệnh \True phía trước phương án đúng và số lượng phương đúng trong mỗi câu hỏi phải khác nhau có thể 0,1,2,3,4 và sắp xếp ngẫu nhiên.Lời giải bắt buộc theo form:
\begin{itemchoice}[T1,F2,F3,T4] <------Bắt buộc phải có 4 tùy chọn VD ý 1 đúng ghi T1, ý 1 sai ghi F1 tương tụ cho các ý còn lại--
  \itemch lời giải giải chi tiết phuong án a
  \itemch lời giải giải chi tiết phuong án b
  \itemch lời giải giải chi tiết phuong án c
  \itemch lời giải giải chi tiết phuong án d
\end{itemchoice}
- Các phương án không có dấu chấm ở cuối

### Đối với câu hỏi loại 3:
- Nội dung câu hỏi cho đáp án ở dạng số con số
- Lệnh shortans \shortans{} tham số bên trong phải là con số ví dụ \shortans{$2$}, \shortans{$2{,}3$} không có đơn vị
#Định dạng về công thức, kí hiệu, phương trình,...:
1.  **Toán học:** Công thức inline dùng `$ ... $`, công thức riêng dòng dùng `\[ ... \]` hoặc `\begin{equation*} ... \end{equation*}`.
2.  **Hóa học:** Dùng `\ce{}` (nếu có gói mhchem) hoặc viết thường. Dùng `\xrightarrow{}` cho phản ứng.
3.  **Số liệu:** Dùng dấu phẩy `{,}` cho số thập phân (ví dụ: `$3{,}14$`).
4.  **Bảng biểu:** Dùng môi trường `tabular`.
5.  **Hình ảnh:** Dùng môi trường `figure` hoặc `TikZ`.

***Định dạng đầu ra***
- Tuân thủ nghiêm ngặt theo nội dung của file Template.tex nằm ở đường dẫn ./skills/exam-latex-creator/assets/templates


***Ví dụ mẫu các loại câu hỏi***
- Tham khỏa các file .tex nằm ở đường dẫn ./skills/exam-latex-creator/assets/templates

---

### Hướng dẫn quy trình thực hiện (Workflow):

#### Bước 1: Soạn thảo nội dung (.tex)
- Tạo file `.tex` mới trong thư mục output của skill: `./skills/exam-latex-creator/output/`.
- **Cấu trúc file:** Sử dụng `\documentclass[FileMain.tex]{subfiles}` để kế thừa từ `FileMain.tex` có sẵn trong thư mục output.
- **Header thông tin:**
- **QUAN TRỌNG:** Giữ nguyên các thông tin trường/sở mặc định trong template (ví dụ: Sở GD & ĐT Gia Lai, Trường THPT Chi Lăng...) trừ khi người dùng yêu cầu thay đổi cụ thể.
- **Tên kỳ thi:** Luôn dùng `TRUY BÀI THEO CHỦ ĐỀ` (không thay đổi).
- Cập nhật ngày kiểm tra (lấy ngày hiện tại nếu không có yêu cầu khác).
- **KHÔNG thêm bớt** bất kỳ thông tin nào ngoài template.
- Nội dung file  bắt buộc phải theo mẫu của file Template.tex:nằm ở đường dẫn tương đối ./skills/exam-latex-creator/assets/templates

#### Bước 2: Chạy script chuẩn hóa (BẮT BUỘC)
Trước khi biên dịch, phải chạy script Python để xử lý các ký tự đặc biệt và format lại nhãn True/False.
- **Lệnh:** `python3 /home/openclaw/.openclaw/workspace/skills/exam-latex-creator/scripts/clean_tf_labels.py`
- Script này sẽ quét thư mục output và sửa các file `.tex` mới tạo.

#### Bước 3: Biên dịch ra PDF
- Di chuyển vào thư mục output: `cd /home/openclaw/.openclaw/workspace/skills/exam-latex-creator/output`
- Chạy lệnh biên dịch **ít nhất 2 lần** để cập nhật tham chiếu:
    1.  `pdflatex -interaction=nonstopmode <TenFile>.tex`
    2.  `pdflatex -interaction=nonstopmode <TenFile>.tex`

#### Bước 4: Trả kết quả
- Thông báo cho người dùng file đã được tạo thành công và gửi link hoặc file trực tiếp về Telegram.
---

### Lưu ý đặc biệt:
- **Lỗi UTF-8:** Cẩn thận với lệnh `\shortans{}`bắt buộc đáp án là các con số .
- **FileMain.tex:** Luôn đảm bảo file này tồn tại trong thư mục output trước khi tạo file con tuyệt đối không chỉnh sửa file này .
