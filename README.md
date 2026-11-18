# CHIUIS 銷售頁改版預覽（設計提案＋文字修改器）

網址：https://rhk9003.github.io/chiuis-lp-preview/

D&J 為 CHIUIS 官網兩個銷售頁做的改版提案：維麗素 `/pages/verisol`、富特固 `/pages/fortigel`。手機版樣式，上方黑色列只是官網頁首的位置示意。

- 說服區塊是設計好的區塊圖（圖上有文案）；每張圖下方灰框是「圖上的文字」，給客戶框選改字，也是我方逐字核對用。
- 選購、常見問題、延伸閱讀是網頁文字；商品卡連到官網現有商品頁。
- 包裝圖、商品圖、倒粉與攪拌照片取自 CHIUIS 官網（2026-11-18 讀取），權利屬原權利人；生活照與區塊圖由 ChatGPT 生成。本儲存庫僅作版型提案預覽。
- 頁面有 noindex 與 robots.txt；這是公開預覽，noindex 不代表存取保護。沒有分析追蹤或後端。

## 文字修改層

按右下角「提出文字修改」進入修改模式（跟 Tippy、羽試、Viola 預覽同一套）。可框選同一段落中的部分文字，也可點選整段，再填入改稿與補充說明。

- 草稿用 localStorage 存在這台裝置的瀏覽器，沒有自動傳送或雲端同步。
- 「下載修改單」產生可閱讀的 HTML；「複製給 Dennis」產生純文字。使用者需自行傳送。
- 兩頁各自存草稿（`chiuis-verisol`、`chiuis-fortigel`），不會互相覆蓋。

## 改頁面

頁面正本是 D&J 客戶資料夾的產生器 `個人客戶/CHIUIS邱氏擇食/03_文案素材/銷售頁改版/build_lp.py`。改完重跑產生器，再執行：

```
python3 _build/build.py
```

會把 `data-copy` 換成修改器要的 `data-copy-id`、掛上修改器、同步圖片。改了文字要同步提高 `_build/build.py` 的 `REVISION`。
