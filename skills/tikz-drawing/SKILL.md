---
name: tikz-drawing
description: "Skill vẽ hình bằng TikZ/PGFPlots trong LaTeX. Sử dụng khi cần vẽ hình hình học, đồ thị hàm số, sơ đồ, mạch điện, flowchart, hình không gian cho tài liệu giáo dục Việt Nam (THCS & THPT)."
allowed-tools: Read, Write, Glob, Grep, Exec
argument-hint: "[loại hình] [mô tả hình cần vẽ]"
---

# Skill: TikZ Drawing

## Description
Skill chuyên vẽ hình bằng TikZ và PGFPlots trong LaTeX. Hỗ trợ đầy đủ các loại hình từ hình học cơ bản đến sơ đồ chuyên dụng, phục vụ soạn thảo tài liệu giáo dục.

## Danh sách Skills

### 1. 📄 Soạn LaTeX tổng quát
- Cấu trúc tài liệu LaTeX (article, report, book, beamer)
- Quản lý package, preamble
- Template báo cáo, đề thi, slides

### 2. 🧮 Công thức toán nâng cao
- Môi trường `align`, `cases`, `equation`
- Ma trận, hệ phương trình
- Đánh số công thức, tham chiếu chéo

### 3. 📐 TikZ từ cơ bản đến nâng cao
- Tọa độ, `node`, `path`, `draw`
- Style, layer, clip, transform
- Macro và tái sử dụng code

### 4. 🔺 Vẽ hình học
- Tam giác, đường tròn, góc, vector
- Hình không gian (hình hộp, hình chóp...)
- Hình minh hoạ bài toán hình học

### 5. 📊 Đồ thị hàm số (pgfplots)
- Vẽ đồ thị 2D / 3D
- Nhiều hàm trên cùng trục tọa độ
- Tùy biến nhãn, trục, màu sắc

### 6. 🔌 Sơ đồ chuyên dụng
- Mạch điện với `circuitikz`
- Sơ đồ khối / flowchart
- Sơ đồ cây (tree)
- Biểu đồ giao hoán (`tikz-cd`)

### 7. 🎨 Tối ưu mã TikZ
- Tách style/macro riêng biệt
- Code gọn, dễ đọc, dễ tái sử dụng
- Dễ chỉnh sửa và mở rộng

### 8. 🛠️ Sửa lỗi compile
- Lỗi package xung đột
- Lỗi TikZ syntax
- Lỗi căn chỉnh hình và chữ

---

## Usage

### 1. Khi nào dùng
- Khi người dùng yêu cầu vẽ hình hình học (tam giác, đường tròn, góc, vector, hình không gian...)
- Khi cần vẽ đồ thị hàm số (hàm bậc 1, bậc 2, lượng giác, mũ, log...)
- Khi cần tạo sơ đồ (flowchart, cây, mạch điện, biểu đồ...)
- Khi cần nhúng hình TikZ vào file LaTeX có sẵn
- Khi cần tối ưu hoặc sửa lỗi code TikZ

### 2. Khi không dùng
- Khi người dùng yêu cầu chèn ảnh từ file bên ngoài (dùng `\includegraphics`)
- Khi yêu cầu chỉ là soạn câu hỏi/đề thi (dùng skill `exam-latex-creator`)

### 3. Quy tắc hỏi lại trước khi thực hiện (BẮT BUỘC)
Nếu người dùng chưa cung cấp đủ thông tin, **không được tự ý vẽ**. Phải hỏi lại:

1. **Loại hình**: hình học / đồ thị / sơ đồ / mạch điện / khác
2. **Mô tả chi tiết**: kích thước, tọa độ, nhãn, màu sắc...
3. **Đầu ra**: chỉ code TikZ / file `.tex` độc lập / nhúng vào file có sẵn
4. **Package đặc biệt**: có dùng `circuitikz`, `pgfplots`, `tikz-cd`... không?

---

## Instruction

**Role:** Bạn là chuyên gia vẽ hình bằng TikZ thuần trong LaTeX, chuyên phục vụ tài liệu giáo dục Việt Nam (THCS & THPT).

### Nguyên tắc vẽ hình

#### 🔍 Quy trình bắt buộc: Phân tích đề trước khi viết code

> Trước khi viết bất kỳ lệnh TikZ nào, **bắt buộc** phải đi qua 5 bước phân tích sau:

**Bước 1 — Xác định đối tượng hình học**
Liệt kê toàn bộ đối tượng có trong bài:
- Điểm — có bao nhiêu? Tên gì? Vị trí tương quan ra sao?
- Đoạn thẳng / cạnh — nối các điểm nào?
- Đường tròn — tâm, bán kính?
- Đường cao, trung tuyến, phân giác — có không?
- Góc — cần đánh dấu góc nào? Góc vuông?
- Nhãn — chữ cái, số đo, tiếu sử nhãn nào?
- Đồ thị — hàm số, trục, nghiệm, đỉnh?
- Hình không gian — cạnh khuất, cạnh thấy, phối cảnh?

**Bước 2 — Phân loại dạng hình**
Xác định rõ thuộc nhóm nào để chọn template phù hợp:

| Dạng | Dấu hiệu nhận biết | Template gợi ý |
|------|-------------------|-----------------|
| Hình học phẳng | Tam giác, tứ giác, đường tròn | `geometry/` |
| Đồ thị hàm số | Hàm bậc nhất, bậc hai, trục Oxy | `graph/` |
| Hình không gian | Hình hộp, hình chóp, cạnh khuất | `space/` |
| Sơ đồ / quy trình | Flowchart, mũi tên, khối | `diagram/` |

**Bước 3 — Lập danh sách điểm cần khai báo**
Liệt kê theo thứ tự logic (gốc → đỉnh → điểm phụ):
1. Các điểm chính (đỉnh tam giác, tâm đường tròn...)
2. Các điểm tính toán từ các điểm chính (chân đường cao, trung điểm...)
3. Các điểm phụ (ký hiệu góc vuông, mũi tên...)

**Bước 4 — Xác định thứ tự vẽ**
Vẽ theo thứ tự từ dưới lên, từ phụ đến chính:
1. **Lới / nền** (nếu cần)
2. **Đường phụ** (nét đứt: đường cao, trung tuyến, chiếu, cạnh khuất)
3. **Vùng tô** (nếu có tô màu)
4. **Đường chính** (cạnh, đường tròn, đồ thị)
5. **Điểm** (\fill circle)
6. **Ký hiệu góc** (\pic {angle=...}, ký hiệu vuông)
7. **Nhãn** (\path node)

**Bước 5 — Kiểm tra trước khi viết**
- Đã có đủ 4 màu `\definecolor` chưa?
- Có dùng `declare function` cho hàm số không?
- Mọi comment đã đặt riêng dòng trước lệnh chưa?
- Đã dùng `\path ... coordinate` thay `\coordinate` chưa?
- Cạnh khuất đã dùng `dashed, thin` chưa?

---

**Ví dụ phân tích:** Đề bài “*Cho tam giác ABC vuông tại A, kẻ AH ⊥ BC. Vẽ hình minh hoạ.*”

```
• Đối tượng:
  - Điểm chính : A (vuông), B, C
  - Điểm tính  : H = hình chiếu A lên BC  → dùng $(B)!(A)!(C)$
  - Đường chính: cạnh AB, AC, BC (tam giác)
  - Đường phụ  : AH (đường cao, nét đứt)
  - Ký hiệu    : góc vuông tại A, góc vuông tại H
  - Nhãn       : A, B, C, H

• Thứ tự vẽ:
  1. Khai báo A, B, C
  2. Tính H = $(B)!(A)!(C)$
  3. Vẽ tam giác ABC (đường chính)
  4. Vẽ AH (nét đứt)
  5. Ký hiệu góc vuông tại A
  6. Ký hiệu góc vuông tại H
  7. fill các điểm A, B, C, H
  8. Đặt nhãn A, B, C, H
```

---

#### ⚠️ Quy tắc bắt buộc: Chỉ dùng TikZ thuần
- **KHÔNG** dùng `pgfplots`, `circuitikz`, `tikz-cd` hay bất kỳ thư viện ngoài nào trừ khi người dùng yêu cầu rõ ràng.
- **CHỈ** dùng các lệnh TikZ core: `\path`, `\draw`, `\fill`, `\node`, `\foreach`, `\coordinate`, đường cong Bézier (`.. controls .. ..`), `pic`.
- Đồ thị hàm số vẽ bằng TikZ thuần (dùng `\draw plot[domain=..., samples=...]`).
- Trục tọa độ vẽ tay bằng `\draw[->]`.

#### Môi trường biên dịch — dùng `standalone`

> **Bắt buộc** dùng `\documentclass[border=Npt]{standalone}` khi tạo file TikZ độc lập. KHÔNG dùng `article`, `report` hay bất kỳ class nào khác cho file vẽ hình riêng lẻ.

```latex
% Cấu trúc file .tex chuẩn cho TikZ standalone
\documentclass[border=5pt]{standalone}
% border=5pt: padding xung quanh hình (có thể chỉnh số)
% border={5pt 5pt 5pt 5pt}: chỉnh riêng từng cạnh (trên phải dưới trái)

\usepackage{tikz}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usetikzlibrary{calc, angles, quotes, intersections, arrows.meta}

\begin{document}
\begin{tikzpicture}[...]
    % ... các lệnh vẽ
\end{tikzpicture}
\end{document}
```

**Các giá trị `border` thường dùng:**
| `border=` | Dùng khi |
|-----------|----------|
| `0pt` | Không có padding |
| `5pt` | Mặc định, gọn |
| `10pt` | Có khoảng trống rộng hơn |
| `{2pt 10pt 2pt 10pt}` | Padding khác nhau mỗi cạnh |

**Compile bằng lệnh:**
```bash
# Biên dịch ra PDF (thủ công)
pdflatex ten-file.tex

# Biên dịch ra PNG chất lượng cao (dùng script có sẵn trong skill)
bash /home/openclaw/.openclaw/skills/tikz-drawing/scripts/tikz-to-png.sh ten-file.tex
# Hoặc chỉ định DPI cao hơn (mặc định 300):
bash /home/openclaw/.openclaw/skills/tikz-drawing/scripts/tikz-to-png.sh ten-file.tex 600
```

**Cấu trúc thư mục output bắt buộc:**
```
./output/
├── Filetex/    ← file .tex nguồn
├── Filepdf/    ← file .pdf biên dịch
└── Images/     ← file .png chất lượng cao
```

> **Quy tắc:** Nếu người dùng yêu cầu `.png` hoặc ảnh chất lượng cao → **bắt buộc dùng script `scripts/tikz-to-png.sh`**. Script tự động phân loại file vào đúng 3 thư mục `Filetex/`, `Filepdf/`, `Images/`.

**Nhúng (include) vào tài liệu chính:**
```latex
% Trong document chính dùng \input hoặc \includegraphics
\usepackage{standalone}   % package standalone hỗ trợ \input file .tex trực tiếp
% Hoặc compile sẵn ra PDF rồi nhúng bằng:
\includegraphics{ten-file.pdf}
```

#### Packages cần khai báo
```latex
\usepackage[utf8]{inputenc}       % nhận diện ký tự UTF-8 (tiếng Việt)
\usepackage[T5]{fontenc}          % mã hoá font T5 cho tiếng Việt
\usepackage[vietnamese]{babel}    % ngôn ngữ tiếng Việt (ngắt dòng, dấu câu)
\usepackage{helvet}               % font sans-serif (không chân)
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{calc, angles, quotes, intersections, through, backgrounds, arrows.meta}
```

> **Lưu ý khi dùng `standalone`:** cần thêm `\usepackage[utf8]{inputenc}` và `\usepackage[T5]{fontenc}` trước `\usepackage{tikz}` để nhãn node tiếng Việt hiển thị đúng dấu.

#### Cấu trúc hình TikZ chuẩn
```latex
\begin{tikzpicture}[scale=1, >=Stealth,
    % Font không chân mặc định cho toàn bộ tikzpicture
    every node/.style={font=\sffamily},
    % Đường nối trơn giữa các đoạn thẳng
    line join=round,
    line cap=round,
]
    % Khai báo tọa độ
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    % Vẽ
    \draw[thick] (A) -- (B);
    % Nhãn - ưu tiên \path ... node
    \path (A) node[below left] {$A$};
    % Điểm
    \fill (A) circle (2pt);
\end{tikzpicture}
```

#### 🎨 Tùy chọn Style khi vẽ (Gợi ý hỏi người dùng)

##### Độ dày đường (`line width`)
| Tùy chọn | Độ dày | Dùng khi |
|----------|--------|----------|
| `ultra thin` | 0.1pt | Lưới nền, phụ trợ |
| `very thin` | 0.2pt | Đường phụ, dashed |
| `thin` | 0.4pt | Mặc định LaTeX |
| `semithick` | 0.6pt | Đường thường |
| `thick` | 0.8pt | **Đường chính** (khuyên dùng) |
| `very thick` | 1.2pt | Nhấn mạnh |
| `ultra thick` | 1.6pt | Trục tọa độ, viền ngoài |
| `line width=Npt` | tuỳ chỉnh | Khi cần chính xác |

##### Kiểu nối đường (`line join`) — **trơn/gãy góc**
| Tùy chọn | Mô tả | Khuyên dùng |
|----------|-------|-------------|
| `line join=round` | **Nối tròn, trơn** | ✅ Mặc định dùng |
| `line join=miter` | Nối nhọn (mặc định TikZ) | Chỉ dùng đường song song |
| `line join=bevel` | Nối vát góc | Ít dùng |

##### Kiểu đầu đường (`line cap`) — đầu đoạn thẳng
| Tùy chọn | Mô tả |
|----------|-------|
| `line cap=round` | Đầu tròn, mềm mại ✅ |
| `line cap=butt` | Cắt thẳng (mặc định) |
| `line cap=rect` | Vuông, thò ra chút |

##### Font chữ không chân (sans-serif) — Danh sách đầy đủ

| Package | Font name | Internal ID | Đặc điểm | Dùng khi |
|---------|-----------|-------------|----------|----------|
| `\usepackage{helvet}` | **Helvetica** | `phv` | Chuẩn, sạch, phổ biến nhất | Mặc định khuyên dùng |
| `\usepackage[scaled]{helvet}` | Helvetica scaled | `phv` | Cân bằng tốt hơn với text | Kết hợp math + text |
| `\usepackage{tgadventor}` | **TeX Gyre Adventor** | `qag` | Góc cạnh, kỹ thuật, có sẵn TeX Live | Hình kỹ thuật, sơ đồ |
| `\usepackage{iwona}` | Iwona | `qiw` | Mảnh, hiện đại | Đề thi, tài liệu |
| `\usepackage{kurier}` | Kurier | `qku` | Đậm hơn Iwona | Tiêu đề, nhấn mạnh |
| `\usepackage[default]{sourcesanspro}` | Source Sans Pro | — | Dễ đọc, chuyên nghiệp | Tài liệu in ấn |
| `\usepackage[default]{cabin}` | Cabin | — | Thân thiện, tròn | Bài giảng, slides |
| `\usepackage{lmodern}` | LM Sans | `lmss` | Mặc định LaTeX modern | Dùng chung |

**Cách dùng trong TikZ:**
```latex
% Cách 1: Toàn bộ tikzpicture (khuyên dùng)
every node/.style={font=\sffamily}

% Cách 2: Dùng font cụ thể (ví dụ qag - URW Grotesque)
every node/.style={font=\fontfamily{qag}\selectfont}

% Cách 3: Từng node riêng lẻ
\path (A) node[font=\sffamily\small] {$A$};

% Cách 4: Toàn document (đặt trong preamble)
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
```

**Gợi ý mặc định cho hình hình học giáo dục:**
```latex
\usepackage{helvet}       % hoặc tgadventor cho phong cách kỹ thuật
\renewcommand{\familydefault}{\sfdefault}
% Trong tikzpicture:
every node/.style={font=\sffamily\small}
```

**Dùng font qag đậm (`\bfseries`) cho nhãn điểm/cạnh hình học:**
```latex
% Khai báo trong preamble
\usepackage{tgadventor}
\newcommand{\qagbf}{\fontfamily{qag}\fontseries{b}\selectfont}

% Trong tikzpicture options
every node/.style={font=\qagbf\small}

% Hoặc tikzset style riêng
\tikzset{
    nhan diem/.style={font=\qagbf\small},
    nhan canh/.style={font=\qagbf\scriptsize},
}
```

##### Kiểu đường (`dash pattern`)
| Tùy chọn | Dùng khi |
|----------|----------|
| `solid` | Đường liền (mặc định) |
| `dashed` | Đường phụ, đường cao |
| `dotted` | Đường chiếu, tham chiếu |
| `dash dot` | Trục đối xứng |
| `loosely dashed` | Dashed thưa hơn |

##### Màu sắc — Hệ màu tập trung dễ đổi theme

> **Quy tắc:** Định nghĩa 4 màu chính bằng `\definecolor` (hex) ngay sau preamble. Trong các lệnh vẽ **chỉ dùng** `\mauchinh`, `\mauphu`, `\maunoibat`, `\mauvien` kết hợp với độ đậm nhạt. Không hard-code màu trực tiếp (`blue`, `red`...).

```latex
% ── Định nghĩa hệ màu (chỉnh tại đây để đổi toàn bộ) ──────────────
\definecolor{mauchinh} {HTML}{1565C0}  % Xanh dương đậm — đường chính, trục
\definecolor{mauphu}   {HTML}{43A047}  % Xanh lá — điểm, nhấn mạnh thứ 2
\definecolor{maunoibat}{HTML}{E53935}  % Đỏ — nghiệm, điểm đặc biệt
\definecolor{mauvien}  {HTML}{424242}  % Xám đậm — viền, nẹt phụ, chữ
```

**Cách dùng trong lệnh vẽ — kết hợp độ đậm nhạt:**
```latex
% Đường chính
\draw[mauchinh, thick] (A) -- (B);

% Đường nhạt 60%
\draw[mauchinh!60, thin] (A) -- (B);

% Tô nền nhạt 15%
\fill[mauchinh!15] (A) -- (B) -- (C) -- cycle;

% Viền + tô
\filldraw[draw=mauvien, fill=mauchinh!10] (O) circle (2);

% Điểm đặc biệt (nghiệm, đỉnh parabol...)
\fill[maunoibat] (P) circle (2.5pt);

% Đường phụ (chiếu, đối xứng...)
\draw[mauphu!70, dashed, thin] (A) -- (H);

% Nhãn chữ
\path (A) node[mauvien] {$A$};
```

**Gợi ý độ đậm nhạt theo loại đường:**
| Độ đậm | Dùng cho |
|---------|----------|
| `100%` (mặc định) | Đường chính, điểm nổi bật |
| `70%` | Đường phụ, nghịch đảo |
| `40%` | Nét đứt, tham chiếu |
| `15%` | Tô nền nhạt, vùng |

**Gam màu thay thế (chỉ sửa 4 dòng `\definecolor`):**
| Gam | mauchinh | mauphu | maunoibat | mauvien |
|-----|----------|--------|-----------|--------|
| Mặc định (xanh-lá-đỏ) | `1565C0` | `43A047` | `E53935` | `424242` |
| Tối (navy-teal-cam) | `0D47A1` | `00695C` | `E65100` | `212121` |
| Pastel (nhạt) | `1976D2` | `388E3C` | `D32F2F` | `616161` |

##### Mẫu khai báo style tổng hợp (khuyên dùng)
```latex
\begin{tikzpicture}[
    scale=1,
    >=Stealth,
    line join=round,      % nối đường trơn
    line cap=round,       % đầu đường tròn
    every node/.style={font=\sffamily},  % font không chân
    thick,                % độ dày mặc định
]
```

#### 🧮 Tính toán Tọa Độ bằng Toán Học (BẮt Buộc Dùng)

> **Nguyên tắc:** Không đặt tọa độ thủ công nếu có thể tính toán. Mọi điểm đặc biệt đều phải được suy ra từ toán học: trung điểm, chạm nhậu, hình chiếu, đối xứng...

##### Thư viện `calc` — Tính toán tọa độ
```latex
\usetikzlibrary{calc}  % Bắt buộc khai báo

% Khai báo điểm cơ bản — dùng \path coordinate (KHÔNG dùng \coordinate)
\path (0,0)    coordinate (A);   % Điểm A tại gốc
\path (4,0)    coordinate (B);   % Điểm B tại (4,0)
\path (1,3)    coordinate (C);   % Điểm C tại (1,3)

% Trung điểm của AB
\path ($(A)!0.5!(B)$) coordinate (M);   % M là trung điểm AB

% Điểm cách A một khoảng t theo hướng AB
\path ($(A)!{t}!(B)$) coordinate (P);   % P nằm trên AB, tỷ lệ t (0<=t<=1)

% Tọa độ tổ hợp tuyến tính
\path ($(A) + 0.5*(B) - 0.3*(C)$) coordinate (Q);

% Dịch chuyển: A dịch 2cm theo trục x
\path ($(A) + (2,0)$) coordinate (A2);

% Nhân vô hướng: phóng to tọa độ B từ A
\path ($(A)!2!(B)$) coordinate (B2);    % B2 sao cho AB2 = 2*AB
```

##### Thư viện `intersections` — Giao điểm đường
```latex
\usetikzlibrary{intersections}

% Giao điểm của 2 đường — đặt tên cho mỗi đường rồi truy xuất giao
\draw[name path=line1] (A) -- (B);   % đường thẳng AB
\draw[name path=circ1] (O) circle (r); % đường tròn tâm O
\path[name intersections={of=line1 and circ1, by={P,Q}}];
% P, Q là 2 giao điểm — tự động tính
```

##### Thư viện `through` — Đường tròn qua điểm
```latex
\usetikzlibrary{through}
% Vẽ đường tròn tâm O đi qua điểm A
\draw (O) circle[radius=distance(O)(A)];
% Hoặc dùng through:
\draw (O) .. circle (through: (A));
```

##### Hình chiếu (chân đường vuông góc)
```latex
% H là hình chiếu của A lên BC (chân đường cao AH)
\path ($(B)!(A)!(C)$) coordinate (H);   % H: chân đường cao AH

% Hình chiếu của A lên trục Ox
\path ($(0,0)!(A)!(1,0)$) coordinate (Ax);  % Ax: hình chiếu A lên trục x
```

##### Khai báo hàm và biến — dùng `declare function` (KHÔNG dùng `\def` hay `\pgfmathsetmacro` đề khai báo hàm)

> **Quy tắc:** 
> - Dùng `declare function` trong `\begin{tikzpicture}[...]` để khai báo hàm toán học rõ ràng, tái sử dụng được
> - Dùng `\pgfmathsetmacro` chỉ cho **hằng số cụ thể** (giá trị số), không dùng để khai báo hàm
> - **Không dùng** `\def` để gán giá trị biến toán học

```latex
% Cách đúng: declare function trong tikzpicture options
\begin{tikzpicture}[
    declare function={
        % Hàm y = x^2 - 2x - 3
        f(\x) = \x*\x - 2*\x - 3;
        % Hàm lượng giác tùy chỉnh
        px(\r,\a) = \r*cos(\a);
        py(\r,\a) = \r*sin(\a);
    },
    scale=1, >=Stealth,
    line join=round, line cap=round,
    every node/.style={font=\sffamily\small},
]
    % Bán kính = 2
    \pgfmathsetmacro{\R}{2}

    % Vẽ parabol dùng hàm f(\x)
    \draw[blue, thick]
        plot[domain=-2:4, samples=100, variable=\x] (\x, {f(\x)});

    % Vẽ điểm trên đường tròn bán kính R tại góc 60°
    \path ({px(\R,60)}, {py(\R,60)}) coordinate (P);

    % Vẽ 6 đỉnh lục giác đều
    \foreach \angle in {0, 60, ..., 300} {
        % Điểm trên đường tròn tại góc \angle
        \fill ({px(\R,\angle)}, {py(\R,\angle)}) circle (2pt);
    }
\end{tikzpicture}
```

```latex
% So sánh: Đúng vs Sai

% SAI - không dùng \def để gán biến toán
\def\myR{2}
\def\myFunc#1{#1*#1 - 2*#1 - 3}

% SAI - không dùng \pgfmathsetmacro để khai báo hàm
\pgfmathsetmacro{\f}{\x*\x - 2*\x - 3}

% ĐÚNG - hằng số cụ thể dùng \pgfmathsetmacro
\pgfmathsetmacro{\R}{2}
\pgfmathsetmacro{\ang}{60}

% ĐÚNG - hàm toán học dùng declare function
declare function={ f(\x) = \x*\x - 2*\x - 3; }
```

##### Hằng số cụ thể — dùng `\pgfmathsetmacro` (giá trị số)
```latex
% Bán kính = 2
\pgfmathsetmacro{\R}{2}
% Góc 60 độ
\pgfmathsetmacro{\ang}{60}
% Cạnh đáy tam giác
\pgfmathsetmacro{\a}{4}
% Chiều cao hình chóp
\pgfmathsetmacro{\h}{3.5}
```
```

##### Tọa độ đối xứng
```latex
% Điểm đối xứng của A qua điểm O
\path ($(2*(O)) - (A)$) coordinate (A');    % A' = đối xứng A qua tâm O

% Điểm đối xứng của A qua trục Ox
\path ($(A) - 2*(0, {\py})$) coordinate (As);  % As = đối xứng A qua Ox
```

##### Quy tắc comment bắt buộc
> Mọi lệnh `\path coordinate`, `\pgfmathsetmacro`, `\draw`, `\fill`... đều phải có **comment riêng 1 dòng ở trước** giải thích ý nghĩa toán học. Không đặt comment inline cùng dòng với lệnh.
```latex
% r = sqrt(3): bán kính nội tiếp
\pgfmathsetmacro{\r}{sqrt(3)}
% H: chân đường cao AH lên BC
\path ($(B)!(A)!(C)$) coordinate (H);
% M: trung điểm AB
\path ($(A)!0.5!(B)$) coordinate (M);
% Cạnh AB của tam giác
\draw (A) -- (B);
% Đường cao AH (nét đứt)
\draw[dashed] (A) -- (H);
% Đánh dấu trung điểm M
\fill (M) circle (2pt);
```

---

#### Các lệnh core được phép dùng

| Lệnh | Mục đích |
|------|----------|
| `\path` | Khai báo đường đi (không vẽ) |
| `\draw` | Vẽ đường thẳng, đường cong |
| `\fill` | Tô màu vùng kín / điểm |
| `\filldraw` | Vừa vẽ viền vừa tô |
| `\path ... node[...]` | **Ưu tiên** đặt nhãn kết hợp với path |
| `\node` | Chỉ dùng khi node đứng độc lập hoàn toàn |
| `\path ... coordinate(name)` | **Ưu tiên** khai báo điểm tọa độ |
| `(A \|- B)` / `(A -\| B)` | Giao điểm đường đứng/ngang qua A và B |
| `++(x,y)` / `+(x,y)` | Tọa độ tương đối (có/không cập nhật current point) |
| `\foreach` | Lặp lại vẽ nhiều phần tử |
| `.. controls P1 and P2 ..` | Đường cong Bézier |
| `pic` | Vẽ hình mẫu có sẵn (góc vuông, góc...) |
| `\clip` | Cắt vùng vẽ |

#### Vẽ đồ thị hàm số bằng TikZ thuần
```latex
\begin{tikzpicture}[scale=1, >=Stealth]
    % Trục tọa độ
    \draw[->] (-0.5,0) -- (4,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,5) node[above] {$y$};
    % Đánh dấu trục
    \foreach \x in {1,2,3} \draw (\x,2pt) -- (\x,-2pt) node[below] {$\x$};
    \foreach \y in {1,2,3,4} \draw (2pt,\y) -- (-2pt,\y) node[left] {$\y$};
    % Vẽ hàm y = x^2 (dùng plot)
    \draw[blue, thick] plot[domain=0:2.2, samples=80] (\x, {\x*\x});
\end{tikzpicture}
```

#### Vẽ đường cong Bézier
```latex
% Đường cong qua A, điều khiển bởi P1, P2, đến B
\draw[thick] (A) .. controls (P1) and (P2) .. (B);
```

#### Dùng pic để vẽ góc
```latex
\usetikzlibrary{angles, quotes}
% Vẽ góc tại B giữa BA và BC
\pic[draw, angle radius=0.5cm, "$\alpha$"] {angle = A--B--C};
% Góc vuông
\pic[draw] {right angle = A--B--C};
```

### Quy tắc đặt tên & nhãn
- Điểm hình học: dùng chữ cái IN HOA (`A`, `B`, `C`...)
- Nhãn góc: dùng `pic` kết hợp `angles` + `quotes` library
- Đơn vị: tính bằng `cm` hoặc theo tỉ lệ `scale`
- Màu mặc định: `black` cho đường thẳng, `blue` cho đồ thị, `red` cho điểm đặc biệt
- Gốc tọa độ `O`: `\node[below left] at (0,0) {$O$};`

### Yêu cầu nghiêm ngặt
- **Chỉ dùng TikZ thuần** — không dùng pgfplots, không dùng thư viện ngoài
- **Luôn** khai báo đầy đủ `\usetikzlibrary` cần thiết
- **Không** dùng đường dẫn tuyệt đối cho file ảnh
- **Phải** test compile trước khi trả kết quả (nếu được yêu cầu tạo file)
- **Đảm bảo** hình vẽ cân đối, nhãn không chồng lên đường
- **Ưu tiên** dùng `\path ... coordinate(name)` thay vì `\coordinate` độc lập — giúp khai báo điểm trực tiếp trên path, nhất quán với phong cách TikZ thuần
- **Không dùng** `\coordinate (X) at (...);` — thay bằng `\path (...) coordinate (X);`
- **Ưu tiên** dùng `\path ... node[vị trí]{nhãn}` thay vì `\node` độc lập — giúp gắn nhãn trực tiếp trên đường path, gọn và chính xác hơn
- **Chỉ dùng** `\node` độc lập khi nhãn không liên quan đến path nào
- **Vòng lặp điểm + nhãn:** Dùng `\foreach` với nhiều biến để vẽ điểm và nhãn gọn — xem kỹ thuật `\t`/`\g` trong phần Ví dụ mẫu
- **Hướng nhãn bằng tọa độ cực:** Dùng `shift={(<góc>:<khoảng>pt)}` thay cho `left=`, `above=`... để kiểm soát hướng chính xác
- **Nhãn tên đỉnh/cạnh:** KHÔNG dùng `$...$` cho tên điểm (A, B, C) và tên cạnh (AB, R) — chỉ dùng `$...$` cho công thức toán học thực sự

---

## Workflow

### Bước 0: Kiểm tra đầu vào (BẮT BUỘC)
- Xác nhận loại hình, mô tả chi tiết, đầu ra mong muốn trước khi vẽ.

### Bước 1: Tạo code TikZ
- Viết code TikZ/pgfplots theo đúng chuẩn.
- Đảm bảo có đầy đủ package khai báo.
- Lưu file vào: `./skills/tikz-drawing/output/<ten_hinh>.tex` (nếu yêu cầu tạo file).

### Bước 2: Compile kiểm tra (nếu yêu cầu)
```bash
cd /home/openclaw/.openclaw/skills/tikz-drawing/output
pdflatex -interaction=nonstopmode <ten_hinh>.tex
pdflatex -interaction=nonstopmode <ten_hinh>.tex
```

### Bước 3: Trả kết quả
- Trả code TikZ trực tiếp trong chat (nếu chỉ cần code).
- Thông báo đường dẫn file (nếu tạo file `.tex` / PDF).
- Nếu compile thất bại, báo lỗi cụ thể.

---

## Ví dụ mẫu

### Vẽ tam giác ABC với đường cao AH
```latex
\begin{tikzpicture}[>=Stealth, scale=1.2]
    % Khai báo tọa độ
    \coordinate (A) at (1,3);
    \coordinate (B) at (0,0);
    \coordinate (C) at (4,0);
    % Chân đường cao H (dùng calc)
    \coordinate (H) at ($(B)!(A)!(C)$);
    % Vẽ tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    % Vẽ đường cao
    \draw[dashed, blue] (A) -- (H);
    % Ký hiệu góc vuông tại H
    \path (H) -- ++(0.15,0) coordinate (H1);
    \path (H) -- ++(0,0.15) coordinate (H2);
    \draw (H1) -- ($(H1)+(0,0.15)$) -- (H2);
    % Nhãn - dùng \path ... node thay vì \node độc lập
    \path (A) node[above] {$A$};
    \path (B) node[below left] {$B$};
    \path (C) node[below right] {$C$};
    \path (H) node[below] {$H$};
    % Điểm
    \foreach \p in {A,B,C,H} {\fill (\p) circle (1.5pt);}
\end{tikzpicture}
```

### Vẽ đồ thị hàm bậc hai y = x² - 2x - 3 (TikZ thuần)
```latex
\begin{tikzpicture}[scale=0.8, >=Stealth]
    % Trục tọa độ
    \draw[->] (-1.5,0) -- (4,0) node[right] {$x$};
    \draw[->] (0,-4.5) -- (0,3) node[above] {$y$};
    \node[below left] at (0,0) {$O$};
    % Đánh dấu trục x
    \foreach \x in {-1,1,2,3} {
        \draw (\x,2pt) -- (\x,-2pt) node[below] {$\x$};
    }
    % Đánh dấu trục y
    \foreach \y in {-4,-3,-2,-1,1,2} {
        \draw (2pt,\y) -- (-2pt,\y) node[left] {$\y$};
    }
    % Vẽ parabol y = x^2 - 2x - 3
    \draw[blue, thick] plot[domain=-1.2:3.2, samples=100, variable=\x] (\x, {\x*\x - 2*\x - 3});
    % Nghiệm x = -1 và x = 3
    \fill[red] (-1,0) circle (2.5pt) node[above right] {$(-1;0)$};
    \fill[red] (3,0) circle (2.5pt) node[above left] {$(3;0)$};
    % Đỉnh V(1; -4)
    \fill[green!60!black] (1,-4) circle (2.5pt) node[right] {$V(1;{-4})$};
    \draw[dashed, gray] (1,0) -- (1,-4) -- (0,-4);
\end{tikzpicture}
```

### Vẽ đường tròn tâm O với dây cung AB
```latex
\begin{tikzpicture}[>=Stealth, scale=1.5]
    \coordinate (O) at (0,0);
    \coordinate (A) at (-0.866, 0.5);  % góc 150°
    \coordinate (B) at (0.866, 0.5);   % góc 30°
    % Đường tròn
    \draw[thick] (O) circle (1cm);
    % Dây cung AB
    \draw[blue, thick] (A) -- (B);
    % Bán kính OA, OB
    \draw[dashed] (O) -- (A);
    \draw[dashed] (O) -- (B);
    % Nhãn
    \node[below] at (O) {$O$};
    \node[left] at (A) {$A$};
    \node[right] at (B) {$B$};
    % Điểm
    \foreach \p in {O,A,B} {\fill (\p) circle (1.5pt);}
\end{tikzpicture}
```

### Vẽ điểm + nhãn đỉnh bằng `\foreach` (kỹ thuật `\t`/`\g`)

> **Kỹ thuật chuẩn:** Dùng `\foreach` với 2 biến `\t` (tên đỉnh) và `\g` (góc cực hướng nhãn). Tên đỉnh `\t` dùng làm **cả tên coordinate lẫn text nhãn**. Hướng nhãn dùng `shift={(\g:7pt)}` để đẳy nhãn ra đúng hướng, không chồng đường vẽ.

```latex
% Trong preamble:
% \usepackage{tgadventor}
% \newcommand{\qagbf}{\fontfamily{qag}\fontseries{b}\selectfont}
% \tikzset{
%     nhan diem/.style={font=\qagbf\small},
%     nhan canh/.style={font=\qagbf\scriptsize},
% }

% \t  = tên đỉnh (là tên coordinate VÀ text nhãn)
% \col = màu điểm và nhãn
% \r   = bán kính chấm điểm
% \g   = góc cực (độ) hướng ra ngoài hình
\foreach \t/\col/\r/\g in {
    O/mauchinh/1.5pt/-45,
    A/mauvien/1.5pt/180,
    B/maunoibat/1.8pt/125,
    C/mauphu/1.8pt/235
}{
    % Chấm điểm
    \fill[\col] (\t) circle (\r);
    % Nhãn tên đỉnh: shift theo góc cực, không dùng $...$
    \path (\t) node[\col, nhan diem, shift={(\g:7pt)}] {\t};
}

% Nhãn tên cạnh — shift theo góc cực, không dùng $...$
\path (A) -- (B)
    node[midway, nhan canh, maunoibat, shift={(125:7pt)}] {AB};
\path (A) -- (C)
    node[midway, nhan canh, mauphu, shift={(235:7pt)}] {AC = AB};
```

**Nguyên tắc chọn góc `\g`:**
| Điểm / Cạnh | Góc gợi ý |
|------------|------------|
| Trên trái | 125°–135° |
| Trên phải | 45°–60° |
| Dưới trái | 215°–235° |
| Dưới phải | −45° (=315°) |
| Trái thuần | 180° |
| Phải thuần | 0° |

### Vẽ đường cong Bézier
```latex
\begin{tikzpicture}[scale=1]
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    \coordinate (P1) at (1,3);   % điểm điều khiển 1
    \coordinate (P2) at (3,3);   % điểm điều khiển 2
    % Đường cong Bézier bậc 3
    \draw[thick, blue] (A) .. controls (P1) and (P2) .. (B);
    % Đường điều khiển (minh hoạ)
    \draw[dashed, gray] (A) -- (P1) -- (P2) -- (B);
    % Điểm
    \foreach \p/\lab in {A/$A$, B/$B$, P1/$P_1$, P2/$P_2$} {
        \fill (\p) circle (2pt);
        \node[above] at (\p) {\lab};
    }
\end{tikzpicture}
```
