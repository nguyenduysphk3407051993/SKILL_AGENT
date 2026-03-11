# JSON schema mẫu (rút gọn)

```json
{
  "thong_tin_chung": {
    "truong": "...",
    "tieu_de": "...",
    "nam_hoc": "2025 - 2026",
    "mon_hoc": "...",
    "thoi_gian": "60",
    "lop": "6"
  },
  "bang_dac_ta": [
    {
      "tt": 1,
      "chuong": "...",
      "danh_sach_noi_dung": [
        {
          "noi_dung": "...",
          "yeu_cau_can_dat": [
            {
              "cap_do_tu_duy": "Biết",
              "chi_bao": ["..."],
              "cau_hoi": {"EX": ["C1"]}
            }
          ]
        }
      ]
    }
  ]
}
```

Quy ước loại câu hỏi:
- `EX`: trắc nghiệm 1 đáp án
- `TF`: đúng/sai
- `SA`: trả lời ngắn
- `BT`: tự luận
