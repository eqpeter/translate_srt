import sys
import os
from deep_translator import GoogleTranslator
import re

def translate_file(input_file):
    # 創建新檔名
    filename, ext = os.path.splitext(input_file)
    output_file = f"{filename}_chinese{ext}"
    
    try:
        # 創建翻譯器
        translator = GoogleTranslator(source='en', target='zh-TW')
        
        # 讀取原始檔案
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 翻譯內容
        translated_content = translator.translate(text=content)
        
        # 寫入新檔案
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_content)
            
        print(f"✓ 翻譯完成！")
        print(f"原始檔案: {input_file}")
        print(f"翻譯檔案: {output_file}")
        
    except Exception as e:
        print(f"\n❌ 錯誤：{type(e).__name__}")
        print(f"詳細訊息: {str(e)}")
        import traceback
        print("\n完整錯誤追蹤:")
        print(traceback.format_exc())

def main():
    if len(sys.argv) < 2:
        print("請提供要翻譯的檔案名稱")
        print("使用方式: python translate_srt.py <檔案名稱>")
        return
        
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"錯誤：找不到檔案 '{input_file}'")
        return
        
    translate_file(input_file)

if __name__ == "__main__":
    main()
    input("\n按 Enter 鍵結束...")