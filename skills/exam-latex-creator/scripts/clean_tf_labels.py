import os
import re

# Set directory to the output folder
output_dir = r"d:\QUAN_NHIEM_BAN_TRU\9A1\TAI_LIEU_GIANG_DAY\AGENT\skills\exam_latex_creator\output"

print(f"Scanning directory: {output_dir}")

# Advanced Regex Dictionary provided by user
latex_error_dict = {
    r'"([^"]*)"': r'\\lq\\lq \1 \\rq\\rq',    
    r'\$\$([\S\s]*?)\$\$': r'\\[ \1 \\]',     
    r'\\xrightarrow\[([^\]]*)\]\[([^\]]*)\]': r'\\xrightarrow[$\1$][$\2$]',
    r'\\xrightarrow\[([^\]]*)\]\{([^}]*)\}': r'\\xrightarrow[$\1$][$\2$]',
    r'\\xrightarrow\[([^\]]*)\](?![\[\{])': r'\\xrightarrow[$\1$]',
    r'\\xrightarrow\{([^}]*)\}': r'\\xrightarrow[$\1$]', 
    r'\.\.\.': r'\\dots',                      
    r'(\d+)\s*x\s*(\d+)': r'\1 \\times \2',  
    r'\\frac': r'\\dfrac',                      
    r'_đ': r'_{\\text{đ}}',       
    r'_{đ}': r'_{\\text{đ}}', 
    r'_tđ': r'_{\\text{tđ}}',
    r'_{tđ}': r'_{\\text{tđ}}',
    r'\[cite_start\]': '',
    r'\[cite_end\]': '',
    r'\[cite[:\s]*[\d,\s]+\]': '',
    r'(\\itemch)\s*(?:Sai\.|Đúng\.)\s*': r'\1 ',
}

files_updated = 0

if os.path.exists(output_dir):
    for filename in os.listdir(output_dir):
        if filename.endswith(".tex") and filename.startswith("De_Thi_"):
            filepath = os.path.join(output_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Iterate through the dictionary and apply all replacements
                for pattern, replacement in latex_error_dict.items():
                    content = re.sub(pattern, replacement, content)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"[UPDATED] {filename}")
                    files_updated += 1
                else:
                    print(f"[SKIPPED] {filename} (No changes needed)")
            except Exception as e:
                print(f"[ERROR] Could not process {filename}: {e}")

    print(f"\nCompleted. Total files updated: {files_updated}")
else:
    print(f"[ERROR] Directory not found: {output_dir}")
