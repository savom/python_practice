# 누적합 계산하기
nums = list(range(1,10))

import pandas as pd
pd.DataFrame(nums)
df = pd.DataFrame(nums,columns=["nums"])
df["cumsum"] = df.cumsum()
df.sum()
df.sum()["nums"]
df["nums"].sum()

df["cumsum"] / df["nums"].sum()

# 시가총액 상위 50% 종목 구하기
from pathlib import Path
OUT_DIR = Path(__file__).parent / "output"
CSV = OUT_DIR / "total_page.csv"

df_raw = pd.read_csv(CSV)

# 시가총액 문자열 -> 정수형으로 변환
df_raw["시가총액"] = df_raw["시가총액"].str.replace(",","").astype("int")

# 전체 DataFrame을 시가총액 기주능로 정렬(열만 정렬 x)
df_raw["시가총액"] = df_raw.sort_values(by="시가총액",ascending=False)

df_raw["누적비율"] = df_raw["시가총액"].cumsum() / df_raw["시가총액"].sum()

df_filtered = df_raw.filter(["종목명", "시가총액", "누적비율"])
df_sliced = df_filtered.loc[df_filtered["누적비율"] <= 0.5]
df_sliced.to_csv(OUT_DIR / "top.csv", index=False)

# 시가총액 데이터 시각화하기
values = list(range(1,6))
df = pd.DataFrame(values, columns=["values"])
import plotly.express as px

px.treemap(df, values="values", path=["values"])

#=================================================================================

# df변수에 저장된 데이터 프레임의 홀수, 짝수 의미 부여하기
df["odd_even"] = ["odd", "even", "odd","even","odd"]
px.treemap(df, values="values",path=["odd_even","values"])

# 실제 계산한 시가총액 데이터를 바탕으로 트리맵 그리기
fig= px.treemap(df_sliced,values="시가총액", path=["종목명"])
fig.update_traces(marker={"pad":{"t":0,"b":0,"l":0,"r":0}})
fig.update_layout(margin={"t":0,"b":0,"l":0,"r":0})
