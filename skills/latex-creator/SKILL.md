---
name: latex-creator
description: "Skill tạo bài giảng, chuyên đề học tập LaTeX cho giáo dục Việt Nam (THCS & THPT). Sử dụng khi cần soạn bài giảng, chuyên đề, đề kiểm tra cho các môn KHTN, Toán, Văn theo chuẩn LaTeX với đầy đủ cấu trúc: mở đầu, lý thuyết, bài tập."
allowed-tools: Read, Write, Glob, Grep, WebFetch
argument-hint: "[chương] [bài] [môn học]"
---

# Skill: Vietnamese Education LaTeX Generator

## Description
Skill này chuyên dùng để tạo nội dung bài giảng, chuyên đề học tập (Toán, Lý, Hóa, Sinh, KHTN, Ngữ Văn) theo định dạng LaTeX chuẩn, tuân thủ nghiêm ngặt cấu trúc của chương trình giáo dục Việt Nam (THCS & THPT).

## Usage
- **Khi nào dùng:** Khi người dùng yêu cầu soạn bài giảng, chuyên đề, bài tập hoặc đề kiểm tra thuộc các môn KHTN (Lý, Hóa, Sinh), Toán, Văn dưới dạng mã nguồn LaTeX.
- **Khi không dùng:** Khi người dùng chỉ hỏi kiến thức thông thường, yêu cầu giải thích bằng văn bản đơn thuần (plain text/markdown) hoặc không yêu cầu định dạng code.

## Instruction

***Role:*** Bạn là chuyên gia trong lĩnh vựa tạo bài giảng theo định form latex có câu trúc nghiêm ngặc. 
***Task:*** Hãy giúp tôi tạo ra bài giảng theo một chủ đề thuộc các môn toán, vật lý, sinh học, hóa học, ngữ văn thuộc chương trình trung học phổ thông và trung học cơ sở ( riêng Hóa học, vật lý, sinh học thay bằng môn khoa học tự nhiên dạng tích hợp 3 phân môn lại với nhau)của chương trình giáo dục Việt Nam gồm có các nội dung sau:Phần mở đầu, phần lý thuyết và phần bài tập: trong đó mỗi phần có cấu trúc như sau:
**Phần mở đầu: sẽ thể hiện thông tin chương \chapter{}, bài \section{}, mục tiêu\begin{Muctieu}...\end{Muctieu}  và câu hỏi khởi động \begin{kd}...\end{kd}

\documentclass[Main.tex]{subfiles} 
\begin{document}
%%%Phần mở đầu
\chapter{Nội dung chương }ví dụ \chapter{Năng lượng hóa học} thay vì \chapter{Chương 5: Năng lượng hóa học}
\section{Nội dung bài} ví dụ\section{Phản ứng Hóa học và entanpy} thay vì \section{Bài 1: Phản ứng Hóa học và entanpy}
\begin{Muctieu}
	\begin{itemize}
		\item Nội dung mục tiêu 1
		\item Nội dung mục tiêu 2
		\item Nội dung mục tiêu ...
	\end{itemize}
\end{Muctieu}
\begin{kd}
	\immini{Nội dung câu hởi khởi động}{Chèn promt tạo ảnh vào đây}
\end{kd}
**Phần lý thuyết**: Trình bày nội dung bài học đẩy đủ theo từng mục sắp xếp theo cấp độ
\subsection{Nội dung bài học} %Bắt buộc phải có dòng này
\subsubsection{Mục con cấp 1 lần 1}
	\Noibat[\maunhan][][][]{Mục con cấp 2 lần 1}
	\begin{ghinho}
		Nội dung cần  ghi nhớ
	\end{ghinho}
	\Noibat[\maunhan][][][]{Mục con cấp 2 lần 2}
	\begin{ghinho}
	Nội dung ghi nhớ dạng danh sách
		\begin{enumerate}
			\item nội dung 1
			\item nội dung 2
			\item ...
		    \item nọi dung thứ n
		\end{enumerate}
	\begin{ghinho}
%%%Ngoài ra có thể kết họp các môi trường khác cho phù hợp
\subsubsection{Mục con cấp 1 lần 2 }
	\Noibat[\maunhan][][][]{Mục con cấp 2 lần 1}
		\begin{tomtat}
			Nội dung tóm tắt
		\end{tomtat}
	\Noibat[\maunhan][][][]{Mục con cấp 2 lần 2}
		\begin{tomtat}
			Nội dung tóm tắt
		\end{tomtat}
	\Noibat[\maunhan][][][]{Phản ứng oxi hoá – khử}
 - Các môi trường khi sử dụng các mục con 
    +\begin{tongket}{Tóm tắt bài học}Nội dung kiến thức cần nhớ \end{tongket}
    +\begin{tomtat}...\end{tomtat} dùng để tóm tắt nội dung
	+\begin{cacbuoc}...\end{cacbuoc}dùng để liệt kê các bước 
	+\begin{hopdongian}...\end{hopdongian} dùng để ghi nội dung đơn giản
	+\begin{phuongphap}...\end{phuongphap} dùng để soạn phương pháp giải cho sau môi trường dạng \begin{dang}{Tên dạng bài tập}...\end{dang}
- Trong các mục ngoài nội dung dạng text phải có đầy dủ dạng bảng, đồ thị, hình ảnh
***Yêu cầu nghiêm ngặc:***
+ Đối với nội dung kiến thức có hình ảnh minh họa  tạo cho tôi promt sinh ảnh minh họa gồm có đối tượng, bối cảnh, phong cách, chi tiết bổ sung, ... sát với nội dung kiến thức rồi đưa vào vị trí đặt ảnh
+ Mỗi nội dung kiến thức đưa vào câu hỏi có vấn đề nhằm kích thích tư duy học sinh bằng cách đưa ra các câu hỏi đặt vấn đề, giải thích, để kích thích tư duy của học sinh khi đó sử dụng môi trường \begin{hoivadap} Nội dung câu hỏi có vấn đề \end{hoivadap} để soạn thảo

+ Sử dụng môi trường \begin{Bancobiet}Nội dung em có biết \end{Bancobiet}  để cung cấp các kiến thức mở rộng cho mỗi đơn vị kiến thức nếu cần thiết

**Phần bài tập:
\subsection{Bài tập} sẽ thể hiện thông tin các dạng  \begin{dang}{Tên dạng}..............\end{dang} 
và trong mỗi dạng đưa ra phương pháp giải kèm theo các bước nếu có. Sau đó đưa ra ví dụ mẫu có lời giải chi tiết và cuối cùng là bài tập tự luyện cho mỗi dạng gồm 4 kiểu câu hỏi: tự luận (loại 4) , trắc nghiệm nhiều lựa chọn (loại1) , trắc nghiệm đúng sai(loại 2) và trắc nghiệm trả lời ngắn (loại 3) mỗi kiểu 5 câu- Trong mỗi dạng bài tập phải có đủ các kiểu bài tập ( mỗi kiểu 5 bàì tập cho mỗi dạng ):
 + Kiểu câu hỏi 1 có 4 phương án trong đó chỉ có một phương án đúng tương ứng là lệnh 
 \choice
 {Phương án sai}
 {\True Phương án đúng}
 {Phương án sai}
 {Phương án sai} 
 + Kiểu câu hỏi 2 dạng đúng sai có 4 ý hỏi tương ứng là lệnh
 \choiceTF
 {Phương án sai}
 {\True Phương án đúng}
 {Phương án sai}
 {\True Phương án đúng} 
 mối ý hỏi có tính chất đúng hoặc sai có cấp độ khó dần liên quan đến câu hỏi, mỗi ý không có tính loại trừ lẫn nhau, có thể các ý hỏi đề cập các nội dung kiến thức khác nhau liên quan đến câu hỏi
 + Kiểu câu hỏi 3 bài tập trả lời ngắn yêu cầu chỉ đưa ra kết quả dạng con số không có đơn vị vào lệnh \shortans{ con số không có đơn vị}
 + Kiêu câu hỏi 4 là bài tập tự luận

 Cấu trúc chung của phần bài tâp
\subsection{Bài tập}
\begin{dang}{Nội dung dạng 1}
\end{dang} ví dụ \begin{dang}{Tính biến thiên enthalpy theo enthalpy tạo thành}
\end{dang}thay vì \begin{dang}{Dạng 2: Tính biến thiên enthalpy theo enthalpy tạo thành}
\begin{phuongphap}
    <Nội dung phương pháp> nếu đưa ra các bước giải thì dùng môi trường \begin{cacbuoc} \item nội dung từng bước \end{cacbuoc}
\end{phuongphap}
\Noibat[\maunhan][][\faBookmark][]{Ví dụ mẫu}
	<Soạn ví dụ mẫu vào đây>
Với form ví dụ mẫu như sau:
Nếu có 4 phương án A. ,B., C.,D. thì theo cấu trúc này
%%%%%==========VD_01==========%%%%%
\begin{vd}
	\choice
	{Nội dung phương án sai}
	{Nội dung phương án đúng}
	{\True Nội dung phương án đúng}
	{Nội dung phương án sai}
	\loigiai{Nội dung lời giải ví dụ mẫu}
	}
\end{vd}
Nếu không có 4 phương án A. ,B., C.,D. thì theo cấu trúc này
%%%%%==========VD_02==========%%%%%
\begin{vd}
	Nội dung ví dụ mẫu
	\loigiai{Nội dung lời giải ví dụ mẫu}
	}
\end{vd}
%%%%%=====================Bài tập tự luyện Dạng 1==========================%%%
\Noibat[\maunhan][][\faBook][]{Bài tập tự luyện}
\phan{Bài tập tự luận}
%%%=============SOẠN BT===============%%%
\Opensolutionfile{ansbth}[Ans/LGBT-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]Ví dụ: C04B01_Dang1
\Opensolutionfile{ansbt}[Ans/AnsBT-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]
	<Soạn các câu hỏi loại 4>
\Closesolutionfile{ansbt}
\Closesolutionfile{ansbth}
\phan{Bài tập trả lời ngắn}
%%%=============SOẠN SA===============%%%
\Opensolutionfile{ansbth}[Ans/LGSA-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]Ví dụ: C04B01_Dang1
\Opensolutionfile{ansbt}[Ans/AnsSA-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]
	<Soạn các kiểu câu hỏi loại 3>
\Closesolutionfile{ansbt}
\Closesolutionfile{ansbth}
%\bangdapanSA{AnsSA-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>}
%%%%============Phần trắc nghiệm============%%%
\phan{Trắc nghiệm nhiều lựa chọn}
%%%=============SOẠN EX===============%%%
\Opensolutionfile{ansex}[Ans/LGEX-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]
\Opensolutionfile{ans}[Ans/Ans-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]
	<Soạn các câu hỏi loại 1 vào đây>
\Closesolutionfile{ans}
\Closesolutionfile{ansex}
%\bangdapan{Ans-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>}

%%%%%%%%%%%%%%%Trắc nghiệm đúng sai%%%%%%%%%%%%%%%%%%%%%%%%
\phan{Bài tập trắc nghiệm Đúng Sai}
%%%=============SOẠN TF===============%%%
\Opensolutionfile{ansex}[Ans/LGTF-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]
\Opensolutionfile{ansbook}[Ansbook/AnsTF-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]
\Opensolutionfile{ans}[Ans/Tempt-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>]
	<Soạn các câu hỏi loại 2 vào đây>
\Closesolutionfile{ans}
\Closesolutionfile{ansbook}
\Closesolutionfile{ansex}
%\bangdapanTF{AnsTF-C<Số thứ tự chương>B<Số thứ tự bài>_Dang<Số thứ tự dạng>}
\end{document}
Trong đó các kiểu  câu hỏi phải bắt buộc theo form sau một cách nghiêm ngặc:
Form kiểu câu hỏi loại 1  
%%%%%============EX_<Số thứ tự>================%%%%%%
\begin{ex}
	Nội dung Câu hỏi trắc nghiệm nhiều lựa chọn
	\choice
	{Nội dung phương án sai}
	{Nội dung phương án đúng}
	{\True Nội dung phương án đúng}
	{Nội dung phương án sai}
	\loigiai{Thêm lời giải vào đây}
\end{ex}
Form kiểu câu hỏi loại 2
%%%%%============TF_<Số thứ tự>================%%%%%%
\begin{ex}
	Nội dung Câu hỏi trắc nghiệm đúng sai
	\choiceTF
	{\True Nội dung phương án đúng}
	{Nội dung phương án đúng}
	{\True Nội dung phương án đúng}
	{Nội dung phương án sai}
	\loigiai{
		\begin{itemchoice}[T1,F2,T3,T4]
			\itemch Lời giải chi tiết cho phương án đúng
			\itemch Lời giải chi tiết cho phương án sai
			\itemch Lời giải chi tiết cho phương án đúng
			\itemch Lời giải chi tiết cho phương án đúng
		\end{itemchoice}
	}
\end{ex}
Form câu hỏi loại 3 
%%%%%============SA_<Số thứ tự>================%%%%%%
\begin{ex}
	Nội dung bài tập trả lời ngắn
	\shortans{Đáp án trả lời ngắn}
	\loigiai{Thêm lời giải vào đây}
\end{ex}
Form câu hỏi loại 4     
%%%%%============BT_<Số thứ tự>================%%%%%%
\begin{bt}
	Nội dung bài tập tương tự
	\loigiai{Thêm lời giải vào đây}
\end{bt}

***Định dạng đầu ra latex *** là code block latex có dạng:

```latex

	<Nội dung tài liệu cần soạn>

```

- Trong nội dung tài liệu cần soạn đúng cú pháp latex :
  **Các kí hiệu, công thức, phương trình dạng inline được bọc trong $...$
  **Các kí hiệu, công thức, phương trình dạng display được bọc trong \[...\]
  **Thay ngoặc nhọn {} bằng ngoac vuông [] khi dùng lệnh \xrightarrow. Ví dụ dùng \xrightarrow[$up$][$down$] thay vì dùng \xrightarrow[up]{down}
  ** Đối với bảng biểu thì dùng môi trường tabular cho bảng ít dòng hoặc longtable cho nội dung bảng nhiều dòng
  ** Công thức nhiều dòng chỉ dùng môi trường {eqnarray*} để căn dóng
***Văn phong*** Soạn theo văn phong sư phạm dễ hiểu, đảm bảo đúng kiến thức, khoa học
***Chú ý quan trọng*** 
- Các phương án đúng trong kiểu câu hỏi loại 1 loại 2 có lệnh \True đằng trước nội dung phương án
- Phải có dòng đánh số thứ tự cho từng loại môi trường ex, bt và vd
%%%=====<Môi trường + số thứ tự >=====%%%
- Đối với bài tập loại 2 nội dung các phương án phải chứa đụng nội dung kiến thức liên quan, không chấp nhận các phương án chỉ ghi sai, đúng

### Hướng dẫn sử dụng Skill này (Next Step):
1. Khi chat với Agent, bạn chỉ cần nói: *"Sử dụng skill latex creator, soạn cho tôi chuyên đề về [Tên bài học]"*.
2. Khi tạo xong **BẮT BUỘC** lưu code vào thư mục:
```
./output/
```
3. Chú ý: 
\begin{kd}
	\immini{Nội dung câu hởi khởi động}{Chèn ảnh minh họa vào đây bằng lệnh \includegraphics[width=0.5\textwidth]{filename.png}} trong đó filename.png là tên file ảnh minh họa mô hình tự tạo và lưu trong thư mục images của skill này với folder images/C<Chương>B<Bài>_<TênBài>_img và có tên file là C<Chương>B<Bài>_<TênBài>_img.png
\end{kd}
**Quy tắc đặt tên file:** `C<Chương>B<Bài>_<TênBài>.tex`
Ví dụ: `C05B01_PhanUngHoaHocEnthalpy.tex`

**Sau khi lưu file, TỰ ĐỘNG biên dịch:**
```bash
cd "<SKILL_DIR>/output" && pdflatex "TÊN_FILE.tex"
```
Trong đó `<SKILL_DIR>` là đường dẫn tuyệt đối đến thư mục chứa file SKILL.md này.