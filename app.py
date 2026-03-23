import streamlit as st
import requests

st.set_page_config(page_title="AI Soccer Hub", layout="wide")
st.title("🤖 实时足球赔率监测站")

MY_KEY = "c9d1c77ce8msh35384666f22e8fdp17865ejsn9a531f8f3c7b"

def fetch_live_odds():
    # 核心修正：必须使用 /odds 端点
    url = "https://v3.football.api-sports.io"
    params = {"live": "all"}
    headers = {'x-rapidapi-key': MY_KEY, 'x-rapidapi-host': 'v3.football.api-sports.io'}
    try:
        res = requests.get(url, headers=headers, params=params, timeout=15)
        return res.json()
    except: return None

if st.button("🎯 刷新赔率"):
    data = fetch_live_odds()
    if data and data.get('response'):
        for item in data['response']:
            st.write(f"🏆 {item['league']['name']}")
            # ... 剩余展示逻辑 ...
    else:
        st.info("目前没有实时比赛数据。")
