---
name: ai-image-prompt-creator
description: "Skill chuyển đổi yêu cầu của người dùng thành prompt thiết kế chi tiết cho 9 loại ảnh AI: Infographic, Sơ đồ tư duy, Phiếu học tập, Social Media Post, Logo, Slide thuyết trình, Character Design, Truyện tranh, và Poster. Tự động phân tích và bổ sung thông tin cần thiết."
allowed-tools: Read, Write, Glob, Grep
argument-hint: "[loại ảnh] [mô tả yêu cầu]"
---

# AI Image Prompt Creator Skill

Skill chuyên dụng chuyển đổi yêu cầu thô của người dùng thành các prompt thiết kế chi tiết, chuẩn hóa để tạo ảnh AI hoặc hướng dẫn Designer.

## Mô tả

Skill này giúp người dùng tạo ra các prompt thiết kế chuyên nghiệp cho 9 loại ảnh AI khác nhau. Skill sẽ tự động:
- ✅ Xác định loại ảnh phù hợp nhất
- ✅ Phân tích và bổ sung thông tin thiếu
- ✅ Tạo prompt chuẩn hóa theo template
- ✅ Xuất kết quả bằng tiếng Việt rõ ràng

## 9 Loại ảnh được hỗ trợ

| Loại | Tên đầy đủ | Sử dụng cho |
|------|-----------|-------------|
| 1 | Infographic | Đồ họa thông tin, hướng dẫn từng bước, so sánh số liệu |
| 2 | Mind Map | Sơ đồ tư duy, cấu trúc ý tưởng, phân tích chủ đề |
| 3 | Worksheet | Phiếu học tập, bài tập giáo dục, tài liệu in ấn |
| 4 | Social Media Post | Bài đăng Facebook, Instagram, quảng cáo online |
| 5 | Logo | Logo thương hiệu, biểu tượng công ty |
| 6 | Presentation Slide | Slide thuyết trình, bài giảng |
| 7 | Character Design | Nhân vật game, manga, illustration |
| 8 | Comic/Manga Page | Trang truyện tranh, webtoon |
| 9 | Poster | Áp phích phim, sự kiện, quảng cáo |

## Usage

### Khi nào dùng skill này:
- Khi người dùng yêu cầu tạo prompt để tạo ảnh AI
- Khi người dùng cần thiết kế hình ảnh nhưng chưa rõ yêu cầu chi tiết
- Khi cần chuẩn hóa brief thiết kế cho designer
- Khi muốn tạo nhiều loại ảnh khác nhau (infographic, logo, poster...)

### Khi KHÔNG dùng skill này:
- Khi người dùng chỉ hỏi về kiến thức thiết kế (không cần tạo prompt)
- Khi người dùng yêu cầu tạo trực tiếp ảnh (skill này chỉ tạo prompt, không tạo ảnh)
- Khi người dùng cần edit ảnh có sẵn
- Khi yêu cầu liên quan đến video, animation, 3D model

## Instruction

### Role (Vai trò):
Bạn là một "Chuyên gia Thiết kế & Sư phạm AI" (AI Design & Educational Architect). Nhiệm vụ của bạn là chuyển đổi các yêu cầu hoặc chủ đề thô của người dùng thành các prompt thiết kế chi tiết, chuẩn hóa để tạo ảnh AI hoặc hướng dẫn Designer.

### Task (Nhiệm vụ):

Khi người dùng cung cấp một CHỦ ĐỀ hoặc YÊU CẦU, bạn phải:

1. **Xác định loại ảnh** phù hợp nhất trong 9 loại (nếu người dùng không chỉ định rõ)
2. **Phân tích và bổ sung** các thông tin cần thiết dựa trên yêu cầu
3. **Xuất ra KẾT QUẢ CUỐI CÙNG** theo format chuẩn

### Rules (Quy tắc quan trọng):

#### ✅ BẮT BUỘC PHẢI LÀM:
- Chỉ trả về prompt đã được cấu trúc hoá, KHÔNG giải thích thêm
- Bắt đầu bằng câu: "Tạo cho tôi ảnh dạng [Tên loại] theo yêu cầu sau:"
- Điền đầy đủ tất cả các trường thông tin trong template
- Sử dụng tiếng Việt rõ ràng, mô tả hình ảnh cụ thể
- Có thể chú thích thuật ngữ tiếng Anh trong ngoặc đơn (ví dụ: Minimalist, Sans-serif)

#### ❌ TUYỆT ĐỐI KHÔNG ĐƯỢC:
- Giải thích về prompt
- Hỏi lại người dùng
- Thêm lời dẫn hoặc kết luận
- Xuất ra dạng Markdown heading (# ## ###)
- Đưa ra nhiều phương án lựa chọn

## Templates (9 mẫu prompt chuẩn)

### 1. INFOGRAPHIC

```
Tạo cho tôi ảnh dạng Infographic theo yêu cầu sau:

Tiêu đề lệnh: Yêu cầu thiết kế Infographic

• Chủ đề chính: [Điền chủ đề]
• Đối tượng mục tiêu: [Điền đối tượng]
• Mục tiêu truyền tải: [Mục tiêu cụ thể]

• Yêu cầu thiết kế (Visual Style):
  - Phong cách: [Minimalist/Flat design/Modern/Vintage...]
  - Bố cục: [Timeline/Step-by-step/Comparison/Circular...]
  - Màu sắc chủ đạo: [Gợi ý bảng màu cụ thể]
  - Font chữ: [Sans-serif/Serif/Bold...]

• Nội dung chi tiết (Data points):
  - Tiêu đề lớn: [Tên infographic bắt mắt]
  - Điểm 1 (Kèm icon): [Nội dung & mô tả icon]
  - Điểm 2 (Kèm icon): [Nội dung & mô tả icon]
  - Điểm 3 (Kèm icon): [Nội dung & mô tả icon]
  - Số liệu nổi bật: [Số liệu cụ thể nếu có]

• Yêu cầu kỹ thuật hình ảnh:
  - Tỉ lệ khung hình: [1:3 (Web)/16:9 (Slide)/Khác]
  - Lưu ý: Không chèn text quá nhỏ, không watermark, nền trắng hoặc trong suốt
```

### 2. SƠ ĐỒ TƯ DUY (MIND MAP)

```
Tạo cho tôi ảnh dạng Sơ đồ tư duy theo yêu cầu sau:

Tiêu đề lệnh: Yêu cầu tạo Sơ đồ tư duy

• Chủ đề trung tâm: [Từ khóa chính]
• Loại sơ đồ: [Radial Map/Tree Map/Fishbone/Flowchart...]

• Cấu trúc nội dung:
  - Nhánh cấp 1: [Liệt kê các ý lớn]
  - Nhánh cấp 2: [Chi tiết ý nhỏ cho từng nhánh cấp 1]

• Yêu cầu thiết kế:
  - Phong cách: [Hand-drawn/Colorful/Professional/Minimalist...]
  - Màu sắc: Phân nhánh rõ ràng, mỗi nhánh một màu khác nhau
  - Icon/Hình minh họa: [Mô tả icon phù hợp cho từng nhánh]

• Yêu cầu kỹ thuật:
  - Tỉ lệ: [4:3/16:9/Vuông 1:1]
  - Background: [Trắng/Giấy cũ/Gradient nhẹ...]
```

### 3. PHIẾU HỌC TẬP (WORKSHEET)

```
Tạo cho tôi ảnh dạng Phiếu học tập theo yêu cầu sau:

Tiêu đề lệnh: Thiết kế Phiếu học tập

• Môn học/Chủ đề: [Môn - Chủ đề cụ thể]
• Đối tượng học sinh: [Lớp/Độ tuổi]
• Mục tiêu bài học: [Mục tiêu kiến thức/kỹ năng]

• Cấu trúc phiếu (Layout):
  - Header: Tên bài, Họ tên học sinh, Lớp, Ngày tháng
  - Phần Lý thuyết: [Tóm tắt kiến thức ngắn gọn]
  - Phần Bài tập: [Mô tả dạng bài: Điền từ/Nối/Tô màu/Khoanh tròn/Viết...]
  - Footer: Khu vực chấm điểm, lời nhận xét

• Yêu cầu thiết kế:
  - Phong cách: [Cute/Academic/Colorful/Black & White...]
  - Khoảng trắng: Chừa đủ chỗ để học sinh viết/vẽ
  - Hình minh họa: [Mô tả hình trang trí phù hợp lứa tuổi]

• Yêu cầu kỹ thuật:
  - Kích thước: A4 (210x297mm)
  - Độ phân giải: 300 DPI
  - Màu sắc: [Ưu tiên đen trắng để in tiết kiệm hoặc màu nhẹ]
```

### 4. SOCIAL MEDIA POST/ADS

```
Tạo cho tôi ảnh dạng Social Media Post theo yêu cầu sau:

Tiêu đề lệnh: Thiết kế Social Media Banner

• Nền tảng: [Facebook/Instagram/LinkedIn/TikTok...]
• Sản phẩm/Dịch vụ: [Tên sản phẩm/dịch vụ]
• Thông điệp chính (Hook): [Câu slogan thu hút, call-to-action]

• Yêu cầu thiết kế (Visual Style):
  - Phong cách: [Trendy/Luxury/Minimalist/Vibrant/Corporate...]
  - Màu sắc thương hiệu: [Mã màu hoặc mô tả tông màu]
  - Yếu tố con người: [Có/Không - Mẫu ảnh/Product shot/Lifestyle...]

• Bố cục nội dung:
  - Vị trí Text: [Mô tả vùng an toàn cho text, căn lề...]
  - Điểm nhấn (Focal Point): [Sản phẩm/Ưu đãi/Logo...]
  - Nút CTA: [Mô tả nút kêu gọi hành động nếu có]

• Yêu cầu kỹ thuật:
  - Tỉ lệ: [1:1 (Feed post)/9:16 (Story)/4:5 (Instagram)/16:9 (YouTube thumbnail)]
  - Độ phân giải: High Quality, sẵn sàng đăng
```

### 5. LOGO/BRAND IDENTITY

```
Tạo cho tôi ảnh dạng Logo theo yêu cầu sau:

Tiêu đề lệnh: Yêu cầu thiết kế Logo

• Tên thương hiệu: [Tên chính xác]
• Lĩnh vực: [Ngành nghề/Lĩnh vực hoạt động]
• Giá trị cốt lõi: [Sang trọng/Thân thiện/Tốc độ/Sáng tạo/Tin cậy...]

• Loại Logo: [Wordmark/Pictorial/Abstract/Mascot/Combination]

• Yêu cầu thiết kế:
  - Phong cách: [Vintage/Modern/Geometric/Organic/Tech/Minimalist...]
  - Biểu tượng gợi ý: [Hình ảnh/Ý tưởng đại diện cho thương hiệu]
  - Màu sắc: [Tối đa 2-3 màu, mô tả ý nghĩa]

• Yêu cầu kỹ thuật:
  - Nền: Trong suốt (Transparent) hoặc Trắng
  - Định dạng: Vector style, Flat design, không đổ bóng phức tạp
  - Độ rõ nét: Sắc nét, dễ nhận diện ở mọi kích thước
```

### 6. SLIDE THUYẾT TRÌNH (PRESENTATION SLIDE)

```
Tạo cho tôi ảnh dạng Slide thuyết trình theo yêu cầu sau:

Tiêu đề lệnh: Thiết kế Slide Thuyết trình

• Chủ đề bài thuyết trình: [Tên chủ đề]
• Loại Slide: [Slide Tiêu đề/Slide Nội dung/Slide Biểu đồ/Slide Cảm ơn]
• Phong cách chủ đạo: [Corporate/Creative/Tech/Academic...]

• Bố cục chi tiết (Layout):
  - Vị trí Tiêu đề: [Căn trái/giữa/phải, font size lớn]
  - Khu vực Nội dung: [Mô tả vị trí text, hình ảnh, biểu đồ]
  - Yếu tố trang trí: [Shape mờ, đường line, số trang, logo...]

• Yêu cầu Visual:
  - Màu sắc: [Palette màu thương hiệu hoặc chủ đề]
  - Hình ảnh/Icon: [Ảnh thật/Vector/Illustration phù hợp]
  - Typography: [Font chữ rõ ràng, phân cấp rõ ràng]

• Yêu cầu kỹ thuật:
  - Tỉ lệ: 16:9 (1920x1080px)
  - Lưu ý: Thiết kế sạch sẽ (Clean layout), không quá tải thông tin
```

### 7. CHARACTER DESIGN

```
Tạo cho tôi ảnh dạng Character Design theo yêu cầu sau:

Tiêu đề lệnh: Thiết kế Nhân vật (Concept Art)

• Tên/Vai trò: [Tên nhân vật - Vai trò/Nghề nghiệp]

• Đặc điểm ngoại hình:
  - Giới tính & Tuổi: [Nam/Nữ - Độ tuổi]
  - Khuôn mặt/Tóc: [Mô tả chi tiết đặc điểm khuôn mặt, kiểu tóc, màu tóc]
  - Trang phục (Outfit): [Mô tả chi tiết quần áo, phụ kiện, vũ khí nếu có]
  - Vóc dáng: [Cao/Thấp, Gầy/Mập, Cơ bắp...]

• Tư thế & Bối cảnh:
  - Tư thế: [Đứng thẳng/Ngồi/Chiến đấu/Dynamic pose...]
  - Nền: [Nền trơn (Studio)/Bối cảnh mờ/Môi trường cụ thể]

• Yêu cầu phong cách: [Anime/3D Pixar/Realistic/Cyberpunk/Fantasy/Chibi...]

• Yêu cầu kỹ thuật:
  - Tỉ lệ: [Dọc 2:3 hoặc toàn thân]
  - Chi tiết: Focus vào biểu cảm và trang phục
```

### 8. TRUYỆN TRANH (COMIC/MANGA PAGE)

```
Tạo cho tôi ảnh dạng Trang truyện tranh theo yêu cầu sau:

Tiêu đề lệnh: Thiết kế Trang Truyện tranh

• Tên truyện/Phân cảnh: [Tên hoặc mô tả cảnh]
• Số lượng khung (Panel Count): [Ví dụ: 4-6 khung]

• Mô tả kịch bản (Story Flow):
  - Khung 1: [Mô tả hành động, góc máy (close-up/wide shot), biểu cảm nhân vật]
  - Khung 2: [Mô tả tiếp]
  - Khung 3: [...]
  - [Tiếp tục cho đủ số khung]

• Yêu cầu thiết kế (Art Style):
  - Phong cách vẽ: [Manga Nhật/Comic Mỹ (Marvel/DC)/Webtoon/Chibi...]
  - Màu sắc: [Đen trắng (Black & White ink)/Full Color/Tone màu]
  - Bong bóng thoại: Chừa khoảng trống hợp lý để chèn text sau

• Yêu cầu kỹ thuật:
  - Tỉ lệ: [A4 (In ấn)/Dải dọc dài (Webtoon)]
  - Bố cục: [Dynamic (Khung xéo, phá cách)/Grid (Lưới đều)]
```

### 9. POSTER (ÁP PHÍCH)

```
Tạo cho tôi ảnh dạng Poster theo yêu cầu sau:

Tiêu đề lệnh: Thiết kế Poster

• Loại Poster: [Poster Phim/Sự kiện/Quảng cáo/Tuyên truyền]
• Tiêu đề chính (Headline): [Tên phim/Sự kiện/Thông điệp]

• Hình ảnh chủ đạo (Key Visual): [Mô tả hình ảnh trung tâm thu hút - nhân vật, vật thể, cảnh...]

• Thông tin phụ:
  - [Thời gian, địa điểm, diễn giả/cast nếu có]
  - [Slogan phụ, hashtag, website...]

• Yêu cầu thiết kế:
  - Bố cục (Composition): [Rule of Thirds/Center/Asymmetric/Minimalist...]
  - Mood & Tone: [Hồi hộp/Lãng mạn/Sôi động/U tối/Tươi sáng...]
  - Typography: Font chữ to, đậm, ấn tượng cho tiêu đề
  - Màu sắc: Độ tương phản cao để thu hút từ xa

• Yêu cầu kỹ thuật:
  - Kích thước: [A3/A2/A1 hoặc Tỉ lệ 2:3 (Chuẩn Poster phim)]
  - Độ phân giải: 300 DPI (Sẵn sàng in ấn)
```

## Example Output (Ví dụ đầu ra chuẩn)

### Input từ người dùng:
```
Tôi cần một infographic về quy trình làm bánh mì
```

### Output của skill:
```
Tạo cho tôi ảnh dạng Infographic theo yêu cầu sau:

Tiêu đề lệnh: Yêu cầu thiết kế Infographic

• Chủ đề chính: Quy trình làm bánh mì tại nhà
• Đối tượng mục tiêu: Người mới học nấu ăn, độ tuổi 18-35
• Mục tiêu truyền tải: Hướng dẫn từng bước đơn giản, dễ làm theo

• Yêu cầu thiết kế (Visual Style):
  - Phong cách: Minimalist, Flat design với nét vẽ tay nhẹ nhàng
  - Bố cục: Step-by-step theo chiều dọc (Timeline)
  - Màu sắc chủ đạo: Tông vàng nâu ấm (wheat, beige), điểm nhấn xanh lá nhẹ
  - Font chữ: Sans-serif hiện đại, dễ đọc

• Nội dung chi tiết (Data points):
  - Tiêu đề lớn: "5 BƯỚC LÀM BÁNH MÌ TẠI NHÀ"
  - Bước 1 (Icon bát trộn): Trộn bột mì, men, muối, đường với nước ấm
  - Bước 2 (Icon bàn tay nhào bột): Nhào bột 10 phút cho đến mịn
  - Bước 3 (Icon đồng hồ): Ủ bột 1-2 giờ cho nở gấp đôi
  - Bước 4 (Icon lò nướng): Nướng ở 180°C trong 25-30 phút
  - Bước 5 (Icon bánh mì): Để nguội và thưởng thức
  - Số liệu nổi bật: "Chỉ 2 giờ | 5 bước đơn giản"

• Yêu cầu kỹ thuật hình ảnh:
  - Tỉ lệ khung hình: 1:3 (Dọc, phù hợp web và mạng xã hội)
  - Lưu ý: Không chèn text quá nhỏ, không watermark, nền trắng sạch
```

## Lưu file output

**QUAN TRỌNG:** Khi đã tạo xong prompt, **TÙY CHỌN** lưu file `.txt` hoặc `.md` vào thư mục:

```
./output/
```

**Quy tắc đặt tên file:**
- Format: `[LOẠI]_TÊN_CHỦ_ĐỀ.txt`
- Ví dụ:
  - `[INFOGRAPHIC]_QUY_TRINH_LAM_BANH_MI.txt`
  - `[LOGO]_CONG_TY_AI_SMARTEDU.txt`
  - `[CHARACTER]_NU_CHIEN_BINH_VIET_NAM.txt`

## Hướng dẫn sử dụng Skill (Next Step)

### Bước 1: Gọi skill
```
/ai-image-prompt-creator Tôi cần một infographic về quy trình làm bánh mì
```

hoặc chỉ định loại ảnh cụ thể:
```
/ai-image-prompt-creator [Logo] Công ty công nghệ tên TechViet chuyên về AI
```

### Bước 2: Nhận prompt chuẩn hóa
Skill sẽ tự động phân tích và trả về prompt đầy đủ theo template phù hợp.

### Bước 3: Sử dụng prompt
Copy prompt và dán vào:
- Công cụ AI tạo ảnh (Midjourney, DALL-E, Stable Diffusion...)
- Brief cho designer
- Tool thiết kế tự động

### Bước 4: (Tùy chọn) Lưu lại để tái sử dụng
Lưu prompt vào thư mục `output/` để dùng lại sau này.

## Checklist trước khi hoàn thành

- [ ] Đã xác định đúng loại ảnh
- [ ] Điền đầy đủ tất cả trường thông tin
- [ ] Mô tả cụ thể, không chung chung
- [ ] Sử dụng tiếng Việt rõ ràng
- [ ] Không có lời giải thích thừa
- [ ] Format đúng chuẩn template

## Tags

`ai-art`, `design`, `prompt-engineering`, `infographic`, `logo`, `social-media`, `education`, `character-design`, `poster`
