# 字幕翻譯與處理工具集
[![GitHub license](https://img.shields.io/github/license/your-username/your-repo)](https://github.com/your-username/your-repo/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/your-username/your-repo)](https://github.com/your-username/your-repo/stargazers)

這個專案包含三個 Python 程式，用於處理和翻譯字幕檔案。

## 快速開始

### 下載
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

## 環境需求

- Python 3.x
- deep-translator 套件

安裝必要套件：
```bash
pip install deep-translator
```

## 程式說明

### 1. translate_srt.py - 字幕翻譯程式

將英文 SRT 字幕檔翻譯成繁體中文。

**功能特點：**
- 自動將英文字幕翻譯成繁體中文
- 保留原始字幕的時間碼和格式
- 保持 HTML 標籤（如 `<i>` 標籤）的格式

**使用方法：**
1. 確保要翻譯的字幕檔與程式在同一目錄
2. 執行程式並指定要翻譯的檔案：
```bash
python translate_srt.py <檔案名稱>
```
例如：
```bash
python translate_srt.py input.srt
```
3. 翻譯結果將儲存為 '原檔名_chinese.srt'

### 2. times.py - 字幕時間調整程式

用於調整 SRT 字幕檔的時間碼，可以將所有時間往後延遲 40 秒。

**功能特點：**
- 自動處理所有時間碼
- 精確到毫秒的時間調整
- 保持原始字幕的其他格式不變

**使用方法：**
1. 將要調整的字幕檔命名為 '132.srt'
2. 執行程式：
```bash
python times.py
```
3. 調整後的檔案將儲存為 '原檔名_adjusted.srt' （例如：'132_adjusted.srt'）

### 3. test_import.py - 環境測試程式

用於測試翻譯環境是否正確設置。

**功能特點：**
- 檢查 Python 版本
- 測試 deep-translator 套件是否正確安裝
- 執行簡單的翻譯測試

**使用方法：**
```bash
python test_import.py
```

如果測試成功，將顯示：
- Python 版本資訊
- 翻譯器創建成功訊息
- 測試翻譯結果

如果有錯誤，程式會顯示詳細的錯誤訊息和解決方案。

## 注意事項

- 確保執行程式時有穩定的網路連接，因為翻譯功能需要連接 Google 翻譯服務
- 翻譯大型檔案時可能需要較長時間，請耐心等待
- 建議在執行翻譯前先使用 test_import.py 確認環境設置正確

## 貢獻
歡迎提交 Pull Request 或建立 Issue 來改善這個專案。

## 授權
本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案。