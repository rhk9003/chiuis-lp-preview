#!/usr/bin/env python3
"""組裝 CHIUIS 銷售頁改版預覽（GitHub Pages）：index、verisol、fortigel 三頁。

頁面正本是客戶資料夾的產生器：
    個人客戶/CHIUIS邱氏擇食/03_文案素材/銷售頁改版/build_lp.py → 預覽/*.html、預覽/img/
本腳本讀那三頁，加上文字修改層（跟 Tippy、羽試、Viola 同一套 review-*.js）：
- 產生器標的 data-copy="區塊名" 換成 data-copy-id（每頁從 copy-001 起）＋data-copy-label
- 載入 review-core.js／review.js／review.css，加 noindex
- 圖片照搬到 img/

改了文字要同步提高 REVISION（舊草稿會因原文不符被拒絕匯入，不會誤套）。
PAGE 名稱不要跟同網域其他預覽撞名（tippy-lp、landing、version-a…）。
用法：python3 _build/build.py
"""
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT.parent.parent / "個人客戶/CHIUIS邱氏擇食/03_文案素材/銷售頁改版/預覽"
REVISION = "2026-11-18a"
PAGES = {  # 檔名: (localStorage 頁名, 修改單標題)
    "verisol.html": ("chiuis-verisol", "CHIUIS 維麗素銷售頁"),
    "fortigel.html": ("chiuis-fortigel", "CHIUIS 富特固銷售頁"),
}

HEAD_ADD = """<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="review.css"><script defer src="review-core.js"></script><script defer src="review.js"></script>
<style>
#copy-review-root{--review-blue:#2E4FC9;--review-line:#d9def5}
#copy-review-root .review-launcher{background:#2E4FC9!important;border-color:#2E4FC9!important;color:#fff!important}
mark.review-mark{background:#f6eab8!important;color:inherit}
body.review-active [data-copy-id]:hover{outline:2px solid #2E4FC9;outline-offset:2px}
body.review-active .cx-btn[data-copy-id]{background-color:#111!important}
.cx-cap p[data-copy-id]{cursor:text}
</style>
"""


def tag(html):
    n = 0

    def rep(m):
        nonlocal n
        n += 1
        return f'data-copy-id="copy-{n:03d}" data-copy-label="{m.group(1)}"'

    return re.sub(r'data-copy="([^"]+)"', rep, html), n


def main():
    for name, (page, title) in PAGES.items():
        html = (SRC / name).read_text(encoding="utf-8")
        html = html.replace("</head>", HEAD_ADD + "</head>", 1)
        html = html.replace("<body>", f'<body data-review-page="{page}" data-review-revision="{page}-{REVISION}" '
                                      f'data-review-title="{title}">', 1)
        html, n = tag(html)
        (ROOT / name).write_text(html, encoding="utf-8")
        print(f"{name}: {n} 個可修改區塊")
    idx = (SRC / "index.html").read_text(encoding="utf-8").replace("</head>", '<meta name="robots" content="noindex,nofollow"></head>', 1)
    (ROOT / "index.html").write_text(idx, encoding="utf-8")
    if (ROOT / "img").exists():
        shutil.rmtree(ROOT / "img")
    shutil.copytree(SRC / "img", ROOT / "img")
    print("img/ 已同步：", sum(1 for p in (ROOT / "img").rglob("*") if p.is_file()), "個檔案")


if __name__ == "__main__":
    main()
