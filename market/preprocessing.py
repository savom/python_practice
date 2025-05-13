# 작업 폴더 생성하기
from pathlib import Path

WORK_DIR = Path(__file__).parent
OUT_DIR = WORK_DIR / "output"
OUT_DIR.mkdir(exist_ok=True)

# 데이터 전처리리
import pandas as pd
import json

with open(OUT_DIR / "page_1.json","r",encoding="utf-8") as fp:
    parsed = json.load(fp)
parsed

type(parsed)
parsed.keys()

pd.DataFrame(parsed["body"])
df_raw = pd.DataFrame(parsed["body"], columns=parsed["header"])
df_raw = df_raw.dropna(axis=0, how="any")
df_raw = df_raw.iloc[:,:-1]

def clean_white_space(text:str):
    return " ".join(text.split())

df_raw.columns

for col in df_raw.columns:
    df_raw[col] = df_raw[col].apply(clean_white_space)
df_raw

df_raw.to_csv(OUT_DIR/"page_1.csv",index=False)