import sys
import os
from deep_translator import GoogleTranslator

# 強制輸出緩衝
os.environ['PYTHONUNBUFFERED'] = '1'

def main():
    try:
        print("="*50)
        print(f"Python 版本: {sys.version}")
        print("="*50)
        
        print("\n1. 測試 deep_translator 導入")
        translator = GoogleTranslator(source='en', target='zh-TW')  # 修改這裡：zh-tw -> zh-TW
        print("✓ 翻譯器創建成功")
        
        print("\n2. 執行測試翻譯")
        test_text = "Hello, World!"
        print(f"原文: {test_text}")
        result = translator.translate(text=test_text)
        print(f"譯文: {result}")
        
        print("\n✓ 全部測試完成!")
        
    except ImportError as e:
        print(f"\n❌ 錯誤：無法導入模組")
        print(f"詳細訊息: {str(e)}")
        print("\n請執行以下命令安裝：")
        print("pip install deep-translator")
        
    except Exception as e:
        print(f"\n❌ 錯誤：{type(e).__name__}")
        print(f"詳細訊息: {str(e)}")
        import traceback
        print("\n完整錯誤追蹤:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
    input("\n按 Enter 鍵結束...")