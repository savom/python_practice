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

# 전체 페이지 개수 확인
# 1. 페이지 이동 데이터의 테이블 태그 추출
btn_last = page.locator("table", has_text="페이지 네비게이션").locator("tbody > tr > td > a").last
url = btn_last.get_attribute("href")
# print(url)

# 2. <a> 태그의 href 속성에서 전페 페이지 개수 추출
"/sise/sise_market_sum.naver?&page=47".split("*")[-1]
total_page = int(url.split("*")[-1])
print(total_page)
page.pause

# 페이지를 이동하면서 시가총액 데이터 수집
tag_header = []
tag_body = []
for idx in range(1,total_page+1):
    page.goto("https://finance.naver.com/sise/sise_market_sum.naver?&page=" + str(idx))
    # 시가총액 데이터 추출
    # 파일로 저장하기
    tag_table = page.locator("table",has_text="코스피")
    if len(tag_header) == 0:
        tag_header = tag_table.locator("thead > tr > th").all_inner_texts()
        
    for tag_tr in tag_table.locator("tbody > tr").all():
        tag_td = tag_tr.locator("td").all_inner_texts()
        tag_body.append(tag_td)
        
print(tag_header)
print(tag_body)
page.pause()

# 데이터 전처리리
import pandas as pd

df_raw = pd.DataFrame(tag_body, columns=tag_header)
df_raw = df_raw.dropna(axis=0, how="any")
df_raw = df_raw.iloc[:,:-1]

def clean_white_space(text:str):
    return " ".join(text.split())

for col in df_raw.columns:
    df_raw[col] = df_raw[col].apply(clean_white_space)

from pathlib import Path
OUT_DIR = Path(__file__).parent / "output"
df_raw.to_csv(OUT_DIR/"page_1.csv",index=False)