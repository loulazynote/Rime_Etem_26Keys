# RIME 倚天26鍵輸入方案（Cross-platform）

> ~~本方案是參考 @oniondelta/Onion_Rime_Files 的[洋蔥輸入法](https://github.com/oniondelta/Onion_Rime_Files)~~

> 本方案參考了 (20250425)
>
> 1. @rime/rime-bopomofo 的[rime-bopomofo](https://github.com/rime/rime-bopomofo)
> 1. @jachuchen/Rime-et26 的[Rime-et26](https://github.com/jachuchen/Rime-et26)

## 簡介

- 注音符號輸入
- 倚天26鍵 (忘形26)
- 支援繁簡轉換
- 支援全形半形切換
- 支援中英文切換
- 支援網頁、郵件、網址識別
- 支援自動選字
- Enter候選字輸出

## 檔案列表

- 倚天26鍵 RIME輸入方案 :
    - `Etem_26Keys.schema.yaml`
    - `Etem26keys.dict.yaml`
    - `Etem26keys_phrase.dict.yaml`

- RIME 設定及Theme
    - `Setting/default.custom.yaml` : 此檔案才能正確完成輸入法設定
    - `Setting/weasel.custom.yaml` : 我本人慣用的樣式主題 for windows OS

## 安裝方式

1. 將上列檔案複製進用戶資料夾:
   - Windows: `%APPDATA%\Rime`
   - Linux (fcitx5): `~/.local/share/fcitx5/rime/`
   - Linux (IBus): `~/.config/ibus/rime/`
   - MacOS: `~/Library/Rime/`

2. 執行 **重新部署** ，即可在選單(F4)內找到該輸入法
   - Windows: 從開始選單選擇 **重新部署**;或當開啓右下工具列看到輸入法Icon時，對Icon點右鍵選擇 **重新佈署**
   - Linux : 點輸入法狀態欄（或IBus菜單）上的 ⟲ (Deploy) 按鈕
      > 如果是用Gnome desktop可以到Gnome Extension安裝[**Input Method Panel**](https://extensions.gnome.org/extension/261/kimpanel/)
   - MacOS: 在系統語言文字選單中選擇 **重新佈署**

3. 完成後即可在選單(F4)內找到該輸入法

## 注意事項

- ~~`essay-zh-hant-mc.txt` 是引用至 [洋蔥輸入法](https://github.com/oniondelta/Onion_Rime_Files/blob/main/allfiles/essay-zh-hant-mc.txt)~~  
  > ~~20240620 停用預設八股文依賴, 改用洋蔥輸入法提供八股文~~
- 簡繁轉換需安裝opencc才可使用

## 聯想詞優化

- 參考 [JeffChien/rime-flypyquick5](https://github.com/JeffChien/rime-flypyquick5) 的作法，新增 `Etem26keys_phrase.dict.yaml`
  作為獨立的詞語碼表，提升詞句候選排序與聯想詞品質。
- 提供 `tools/generate_phrase_dict.py` 與 `Resource/phrase_seed.txt` 兩個輔助檔案，可依需求調整常用語並重新
  產生詞語碼表，部署時會由主字典自動匯入。

### 如何使用聯想詞碼表

1. **調整詞語清單**：開啟 `Resource/phrase_seed.txt`，每行填入一個常用詞或短語。檔案可加入 `#` 開頭的註解，
   方便分組整理，手機版本不需要另外維護。
2. **重新產生碼表**：在專案根目錄執行下列指令，自動依據主字典 (`Etem26keys.dict.yaml`) 的字根組合出對應碼：

   ```bash
   python3 tools/generate_phrase_dict.py \
     Etem26keys.dict.yaml \
     Resource/phrase_seed.txt \
     Etem26keys_phrase.dict.yaml
   ```

   - `tools/generate_phrase_dict.py` 會讀取主字典每個字最常用的編碼，幫清單中的詞語排出合適的連打碼，並依序配置權重，
     讓輸入法在部署後能優先顯示這些聯想詞。
   - 如果詞語內出現主字典沒有的字，腳本會在終端機列出該詞與缺漏的字，便於補齊資料。
3. **重新部署**：將產生好的 `Etem26keys_phrase.dict.yaml` 與其他設定檔一同複製到 RIME 用戶資料夾，照一般流程重新部署即可。

## 輸入方法

當鍵入文字後, 會呈現類似新注音的預選文字, Enter後才會完全輸出

![示意圖](https://github.com/user-attachments/assets/dfb58cdc-e197-4e79-be2c-97cfcc4efac0)

## 鍵位圖

![倚天鍵位](https://user-images.githubusercontent.com/33840759/129006031-ba7e1b72-7a5f-4d84-8bf8-8fd45d92310d.jpg)
