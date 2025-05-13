# 작업 폴더 생성하기
from pathlib import Path

WORK_DIR = Path(__file__).parent
OUT_DIR = WORK_DIR / "output"
OUT_DIR.mkdir(exist_ok=True)

# playwright 패키지 불러오기
from playwright.sync_api import sync_playwright

# 크로미움 웹 브라우저 실행하기
play = sync_playwright().start()
browser = play.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=500)
page = browser.new_page(no_viewport=True)

page.goto("https://finance.naver.com")
page.pause()

# 버튼 클릭 자동화
page.get_by_role("lick", name="국내증시").click()
page.get_by_role("listitem").filter(has_text="시가총액").nth(1).click()
page.pause()

print(page.locator("table", has_text="코스피").locator("thead > tr > th").all_inner_texts())
print(page.locator("table", has_text="코스피").locator("thead > tr").nth(1).locator("td").all_inner_texts())
page.pause

# 파일로 저장하기
tag_table = page.locator("table",has_text="코스피")
tag_header = tag_table.locator("thead > tr > th").all_inner_texts()
tag_body = []
for tag_tr in tag_table.locator("tbody > tr").all():
    tag_td = tag_tr.locator("td").all_inner_texts()
    tag_body.append(tag_td)
    
import json
dumped = json.dumps({"header" : tag_header, "body" : tag_body}, indent=2,ensure_ascii=False)
with open(OUT_DIR / "page_1.json", "w",encoding="utf-8") as fp:
    fp.write(dumped)