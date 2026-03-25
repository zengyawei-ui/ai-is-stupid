import streamlit as st
import requests

# 1. 页面基础配置 (全局只能有一个)
st.set_page_config(page_title="足球情报站", layout="wide")
st.title("⚽️ 实时足球赔率监测站")

# 2. 从保险柜拿钥匙 (确保你在 Secrets 里填了 MY_FOOTBALL_KEY)
MY_KEY = st.secrets["MY_FOOTBALL_KEY"]

# 3. 精准的数据抓取函数
def fetch_live_odds():
    # 这里的 URL 必须带上 /odds 才是取赔率的柜台
    url = "https://api-sports.io"
    params = {"live": "all"}
    headers = {
        'x-rapidapi-key': MY_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    try:
        res = requests.get(url, params=params, headers=headers)
        return res.json()
    except Exception as e:
        st.error(f"连接失败: {e}")
        return None

# 4. 界面逻辑：全页面只有这一个按钮
st.info("提示：点击下方按钮，抓取全球实时赔率。")

if st.button("🎯 立即同步实时数据"):
    with st.spinner('正在搜寻全球赛场...'):
        data = fetch_live_odds()
        if data and data.get('response'):
            results = data['response']
            st.success(f"成功！已找到 {len(results)} 场实时比赛。")
            for item in results:
                l_name = item.get('league', {}).get('name', '未知联赛')
                home = item.get('teams', {}).get('home', {}).get('name', '主队')
                away = item.get('teams', {}).get('away', {}).get('name', '客队')
                with st.expander(f"🏆 {l_name}: {home} VS {away}"):
                    st.json(item.get('bookmakers', []))
        else:
            st.warning("⚠️ 目前暂无正在进行且有赔率更新的比赛，或 API 额度已满。")
