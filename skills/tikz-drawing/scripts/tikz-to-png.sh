#!/bin/bash
# Script: tikz-to-png.sh
# Mục đích: Biên dịch file .tex TikZ standalone → PNG chất lượng cao
# Cách dùng: bash tikz-to-png.sh <file.tex> [dpi]
#   <file.tex> : file LaTeX standalone cần compile
#   [dpi]      : độ phân giải (mặc định 300, cao = 600)
# Ví dụ:
#   bash tikz-to-png.sh triangle.tex
#   bash tikz-to-png.sh triangle.tex 600
#
# Cấu trúc output:
#   ./output/Filetex/   ← file .tex nguồn
#   ./output/Filepdf/   ← file .pdf biên dịch
#   ./output/Images/    ← file .png chất lượng cao
# --------------------------------------------------------

set -e

# Kiểm tra tham số đầu vào
if [ -z "$1" ]; then
    echo "❌ Thiếu tên file. Dùng: bash tikz-to-png.sh <file.tex> [dpi]"
    exit 1
fi

TEX_FILE="$1"
DPI="${2:-300}"
BASENAME="$(basename "${TEX_FILE%.tex}")"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_BASE="$(pwd)/output"

# Thư mục output theo cấu trúc chuẩn
DIR_TEX="${OUTPUT_BASE}/Filetex"
DIR_PDF="${OUTPUT_BASE}/Filepdf"
DIR_IMG="${OUTPUT_BASE}/Images"

# Tạo thư mục nếu chưa có
mkdir -p "$DIR_TEX" "$DIR_PDF" "$DIR_IMG"

echo "📄 File nguồn : $TEX_FILE"
echo "🎯 Độ phân giải: ${DPI} DPI"
echo "📁 Output:"
echo "   Tex → $DIR_TEX"
echo "   PDF → $DIR_PDF"
echo "   PNG → $DIR_IMG"
echo ""

# Bước 1: Copy file .tex vào Filetex/
cp "$TEX_FILE" "${DIR_TEX}/${BASENAME}.tex"

# Bước 2: Compile LaTeX → PDF (output vào Filepdf/)
pdflatex \
    -interaction=nonstopmode \
    -output-directory="$DIR_PDF" \
    "$TEX_FILE"

PDF_FILE="${DIR_PDF}/${BASENAME}.pdf"

# Bước 3: PDF → PNG chất lượng cao (output vào Images/)
pdftoppm \
    -r "$DPI" \
    -png \
    -singlefile \
    "$PDF_FILE" \
    "${DIR_IMG}/${BASENAME}"

PNG_FILE="${DIR_IMG}/${BASENAME}.png"

echo ""
echo "✅ Hoàn thành!"
echo "📄 Tex : ${DIR_TEX}/${BASENAME}.tex"
echo "📕 PDF : $PDF_FILE"
echo "🖼️  PNG : $PNG_FILE"
