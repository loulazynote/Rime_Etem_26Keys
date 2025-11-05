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

- 參考 [JeffChien/rime-flypyquick5](https://github.com/JeffChien/rime-flypyquick5) 的結構，重新整理 `Etem26keys_phrase.dict.yaml`
  的碼長與排序，維持與主字典一致的倚天26鍵字根組合，避免長碼造成選字失敗。
- 聯想詞碼表現採靜態維護，如需新增或調整常用詞語，直接編輯 `Etem26keys_phrase.dict.yaml` 後重新部署即可。建議沿用現有
  權重配置，讓常用詞仍能保持較高排序。

### 如何使用聯想詞碼表

1. **編輯碼表**：以文字編輯器開啟 `Etem26keys_phrase.dict.yaml`，依照 `詞語<Tab>編碼<Tab>權重` 的格式增修條目，
   編碼需使用倚天26鍵字根的連打碼。
2. **重新部署**：存檔後重新部署輸入法，新的聯想詞編碼會立即載入並參與候選排序。

## 輸入方法

當鍵入文字後, 會呈現類似新注音的預選文字, 按下 <kbd>Space</kbd> 或 <kbd>Enter</kbd> 皆可將首選候選字上屏。

- 需要輸入真正的空白時, 請在沒有組字碼的狀態下直接按 <kbd>Space</kbd>。
- 若候選字非首選, 可繼續補碼或搭配數字鍵 <kbd>1</kbd>〜<kbd>9</kbd>（含 <kbd>0</kbd>）選取。

![示意圖](https://github.com/user-attachments/assets/dfb58cdc-e197-4e79-be2c-97cfcc4efac0)

## 鍵位圖

![倚天鍵位](https://user-images.githubusercontent.com/33840759/129006031-ba7e1b72-7a5f-4d84-8bf8-8fd45d92310d.jpg)
