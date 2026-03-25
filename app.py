import streamlit as st
import requests
import pandas as pd

# 1. 基础配置
st.set_page_config(page_title="AI私人数操站", layout="wide")
st.title("⚽ 足球实时比分监控 (API版)")

# 你的 API 信息（已填好）
MY_KEY = "c9d1c77c3de7cf3ca57bf8288eeca53b"
API_HOST = "v3.football.api-sports.io"

def fetch_live_data():
    # 获取全球正在进行的比赛
    url = "https://api-sports.io"
    headers = {
        'x-rapidapi-key': MY_KEY,
        'x-rapidapi-host': API_HOST
    }
    try:
        res = requests.get(url, headers=headers, timeout=15)
        data = res.json()
        if data.get('response'):
            results = []
            for item in data['response']:
                results.append({
                    "联赛": item['league']['name'],
                    "主队": item['teams']['home']['name'],
                    "客队": item['teams']['away']['name'],
                    "比分": f"{item['goals']['home']}-{item['goals']['away']}",
                    "比赛分钟": f"{item['fixture']['status']['elapsed']}'"
                })
            return pd.DataFrame(results)
        return "empty"
    except Exception as e:
        return str(e)

# 2. 界面展示
st.info("💡 这是一个完全属于你的数据监控站")

if st.button('🚀 立即刷新：调取全球实时赛况', type="primary"):
    with st.spinner('正在穿越大气层抓取数据...'):
        df = fetch_live_data()
        if isinstance(df, pd.DataFrame):
            st.success(f"✅ 成功连接！当前共有 {len(df)} 场比赛正在进行。")
            st.dataframe(df, use_container_width=True)
        elif df == "empty":
            st.warning("⚠️ 目前全球暂时没有正在进行的比赛。")
        else:
            st.error(f"连接失败: {df}")

st.divider()
st.caption("项目状态：已成功挂载 API-Sports 数据源 | app.py 已就绪")
