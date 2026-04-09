# 📚 Kỹ thuật TikZ hay từ tikz.dev
# Nguồn: https://tikz.dev (PGF/TikZ Manual)
# Tổng hợp: các kỹ thuật path, coordinates, calc hay dùng trong hình học giáo dục
# --------------------------------------------------------

## 1. 🔄 Toạ độ cực (Polar) — cú pháp ngắn gọn

```latex
% Điểm trên đường tròn bán kính 2cm tại góc 30°
\path (30:2cm) coordinate (P);

% Vẽ các tia từ gốc đến 6 điểm đều trên đường tròn
\foreach \angle in {0, 60, 120, 180, 240, 300} {
    % Tia từ O đến điểm trên đường tròn
    \draw (0,0) -- (\angle:2);
}

% Vẽ hình lục giác đều bằng polar
\draw (0:2) \foreach \a in {60,120,...,360} { -- (\a:2) } -- cycle;
```

---

## 2. ↔️ Giao điểm đường thẳng đứng/ngang — toán tử `|-` và `-|`

```latex
% (A |- B): lấy x của A, y của B  => giao giữa đường dọc qua A và đường ngang qua B
% (A -| B): lấy y của A, x của B  => giao giữa đường ngang qua A và đường dọc qua B

\path (1, 3) coordinate (A);
\path (4, 1) coordinate (B);

% Điểm có x=1 (của A) và y=1 (của B)
\path (A |- B) coordinate (Hfoot);

% Vẽ đường vuông góc từ A xuống đường ngang qua B
\draw[dashed] (A) -- (A |- B);

% Dùng để vẽ đường chiếu lên trục
\path (2, 3) coordinate (P);
% Điểm chiếu của P xuống Ox: lấy x của P, y=0
\path (P |- 0,0) coordinate (Px);
% Điểm chiếu của P sang Oy: lấy y của P, x=0
\path (0,0 |- P) coordinate (Py);

\draw[dotted] (P) -- (Px);
\draw[dotted] (P) -- (Py);
```

---

## 3. 📐 Thư viện `calc` — tính toán tọa độ nâng cao

```latex
\usetikzlibrary{calc}

% --- Trung điểm ---
% M là trung điểm của AB
\path ($(A)!0.5!(B)$) coordinate (M);

% --- Chia đoạn tỉ lệ t ---
% P chia AB theo tỉ lệ t (0 ≤ t ≤ 1)
\path ($(A)!0.3!(B)$) coordinate (P);  % P cách A 30% đoạn AB

% --- Hình chiếu vuông góc ---
% H là hình chiếu của C xuống đường thẳng AB
\path ($(A)!(C)!(B)$) coordinate (H);

% --- Dịch chuyển ---
% A dịch theo vector (2, 1)
\path ($(A) + (2,1)$) coordinate (A2);

% --- Đối xứng qua điểm ---
% A' là đối xứng của A qua O
\path ($(2*(O)) - (A)$) coordinate (Aprime);

% --- Phóng to/thu nhỏ từ điểm ---
% B2: điểm sao cho OB2 = 2*OB
\path ($(O)!2!(B)$) coordinate (B2);

% --- Điểm cách đường thẳng một khoảng ---
% P cách đường AB một khoảng 0.5 về phía trái
\path ($(A)!0.5!(B)!0.5cm!90:(B)$) coordinate (P);
```

---

## 4. 🔺 Thư viện `angles` — vẽ góc và nhãn góc

```latex
\usetikzlibrary{angles, quotes}

% Vẽ cung góc tại B giữa tia BA và BC
\pic[draw, angle radius=0.6cm] {angle = A--B--C};

% Vẽ cung góc với nhãn
\pic[draw, angle radius=0.6cm,
     angle eccentricity=1.5,
     "$\alpha$"] {angle = A--B--C};

% Góc vuông (ký hiệu hình vuông nhỏ)
\pic[draw] {right angle = A--B--C};

% Nhiều màu và style
\pic[draw=blue, fill=blue!10,
     angle radius=0.8cm,
     "$\beta$"{blue}] {angle = D--E--F};
```

---

## 5. 🎯 Giao điểm hai đường bất kỳ — `intersections` library

```latex
\usetikzlibrary{intersections}

% Đặt tên cho hai đường
\draw[name path=duong1] (A) -- (B);
\draw[name path=duong2] (C) -- (D);

% Tìm giao điểm tự động
\path[name intersections={of=duong1 and duong2, by={G}}];

% G là giao điểm
\fill[red] (G) circle (2pt);
\path (G) node[above right] {$G$};

% Đường thẳng và đường tròn giao nhau
\draw[name path=thangAB] (A) -- (B);
\draw[name path=tronO] (O) circle (2);
\path[name intersections={of=thangAB and tronO, by={P, Q}}];

% P và Q là hai giao điểm
\fill (P) circle (2pt);
\fill (Q) circle (2pt);
```

---

## 6. ➡️ Đường gấp khúc vuông góc — toán tử `-|` và `|-`

```latex
% Vẽ đường từ A đến B: đi ngang trước rồi lên
\draw (A) -| (B);

% Vẽ đường từ A đến B: đi lên trước rồi ngang
\draw (A) |- (B);

% Ứng dụng trong flowchart
\draw[->] (proc) |- (output);
\draw[->] (cond) -| (yes_block);
```

---

## 7. 〰️ Đường cong Bézier nâng cao

```latex
% Bézier bậc 2 (1 điểm điều khiển)
\draw (A) .. controls (P1) .. (B);

% Bézier bậc 3 (2 điểm điều khiển)
\draw (A) .. controls (P1) and (P2) .. (B);

% Dùng tọa độ tương đối với +(...)
\path (0,0) coordinate (A);
\path (4,0) coordinate (B);
% Cong lên giữa: điều khiển tại +(1,2) và +(3,2) so với điểm đầu
\draw (A) .. controls ($(A)+(1,2)$) and ($(B)+(-1,2)$) .. (B);

% Vẽ đường cong "mượt" qua nhiều điểm dùng \foreach
\draw plot[smooth, tension=0.8] coordinates {
    (0,0) (1,2) (2,1) (3,3) (4,0)
};
```

---

## 8. 🔁 `\foreach` nâng cao — lặp vẽ hình học

```latex
% Vẽ đa giác đều n cạnh
\pgfmathsetmacro{\n}{6}
\draw \foreach \i in {1,...,\n} {
    -- ({360/\n * \i}:2)
} -- cycle;

% Vẽ và đặt nhãn cùng lúc
\foreach \p/\lab in {A/A, B/B, C/C, H/H} {
    % Điểm tại mỗi đỉnh
    \fill (\p) circle (2pt);
    % Nhãn tại mỗi đỉnh
    \path (\p) node[above] {$\lab$};
}

% Đánh số trên trục
\foreach \x [count=\i] in {-2,-1,0,1,2} {
    % Vạch trên trục x
    \draw (\x, 2pt) -- (\x, -2pt);
    % Nhãn số
    \path (\x, 0) node[below] {$\x$};
}
```

---

## 9. 📌 Relative coordinates — tọa độ tương đối

```latex
% +(x,y): tương đối so với điểm trước, KHÔNG cập nhật current point
% ++(x,y): tương đối, CÓ cập nhật current point

% Ví dụ: vẽ hình chữ L
\draw (0,0) -- ++(3,0) -- ++(0,2) -- ++(-1,0);

% Dùng + để vẽ kí hiệu góc vuông tại H
\path (H) coordinate (H);
\draw (H) +(0.2,0) -- +(0.2,0.2) -- +(0,0.2);
```

---

## 10. 🖊️ `\path` đa năng — khai báo nhiều thứ trên 1 dòng

```latex
% \path có thể khai báo coordinate + node + fill cùng lúc
\path
    (0,0)  coordinate (A) node[below left] {$A$}
    (4,0)  coordinate (B) node[below right] {$B$}
    (2,3)  coordinate (C) node[above] {$C$};

% \path với fill để đánh dấu điểm
\path[fill=black]
    (A) circle (2pt)
    (B) circle (2pt)
    (C) circle (2pt);
```
