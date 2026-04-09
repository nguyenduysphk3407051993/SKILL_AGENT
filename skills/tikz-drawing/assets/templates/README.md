# 📁 Templates TikZ Drawing

Các mẫu hình TikZ thuần — sẵn sàng dùng và chỉnh sửa.

---

## 📐 geometry/ — Hình học phẳng

| File | Mô tả |
|------|-------|
| `triangle-basic.tex` | Tam giác ABC cơ bản |
| `triangle-altitude.tex` | Tam giác ABC với đường cao AH, ký hiệu góc vuông |
| `circle-chord.tex` | Đường tròn tâm O, dây cung AB, bán kính OA OB |
| `circle-tangent.tex` | Tiếp tuyến AB, điểm C trên đường tròn với AC=AB — `\foreach \t/\col/\r/\g`, font qag `\bfseries`, `shift={(\g:7pt)}` |
| `angle-rays.tex` | Góc AOB với hai tia, cung góc, nhãn alpha |

## 📊 graph/ — Đồ thị hàm số

| File | Mô tả |
|------|-------|
| `quadratic-function.tex` | Hàm bậc hai y = x²-2x-3, đỉnh, nghiệm, trục đối xứng |
| `linear-function.tex` | Hai hàm bậc nhất giao nhau, chiếu giao điểm |

## 🧊 space/ — Hình học không gian

| File | Mô tả |
|------|-------|
| `rectangular-box.tex` | Hình hộp chữ nhật ABCD-A'B'C'D' (phối cảnh xiên) |
| `pyramid-square.tex` | Hình chóp tứ giác đều S.ABCD, đường cao SO |

## 🔷 diagram/ — Sơ đồ

| File | Mô tả |
|------|-------|
| `flowchart-basic.tex` | Flowchart: start, process, decision, io, stop |

---

## 💡 Quy tắc chỉnh sửa template

1. **Thay tọa độ**: chỉnh `\coordinate` hoặc `\pgfmathsetmacro` ở phần đầu
2. **Thay nhãn**: tìm `\path (...) node` và sửa text trong `{}`
3. **Thay màu**: sửa `blue`, `red`, `green!60!black`...
4. **Thay độ dày**: sửa `thick` → `very thick` / `thin`...
5. **Scale**: chỉnh `scale=` trong `\begin{tikzpicture}[...]`

## 📦 Compile

```bash
cd /home/openclaw/.openclaw/skills/tikz-drawing/assets/templates/<thư mục>
pdflatex <tên file>.tex
```
