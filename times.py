import re
import os

def add_40_seconds(time_str):
    try:
        # 分解時間字串 "00:01:25,352"
        h, m, last_part = time_str.split(':')
        s, ms = last_part.split(',')
        
        # 轉換為整數
        h = int(h)
        m = int(m)
        s = int(s)
        ms = int(ms)
        
        # 轉換為毫秒並加上 40 秒
        total_ms = h * 3600000 + m * 60000 + s * 1000 + ms + 40000
        
        # 轉回時分秒毫秒格式
        new_h = total_ms // 3600000
        total_ms %= 3600000
        new_m = total_ms // 60000 
        total_ms %= 60000
        new_s = total_ms // 1000
        new_ms = total_ms % 1000
        
        return f"{new_h:02d}:{new_m:02d}:{new_s:02d},{new_ms:03d}"
    except Exception as e:
        print(f"處理時間 {time_str} 時發生錯誤: {str(e)}")
        return time_str

# 讀取檔案
input_file = '132.srt'
# 生成新檔名：在原始檔名的副檔名前加上_adjusted
file_name, file_ext = os.path.splitext(input_file)
output_file = f"{file_name}_adjusted{file_ext}"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正則表達式找出並替換時間碼
pattern = r'(\d{2}:\d{2}:\d{2},\d{3})'
new_content = re.sub(pattern, lambda x: add_40_seconds(x.group()), content)

# 寫入新檔案
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("處理完成！")