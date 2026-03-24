import streamlit as st
import requests

# 1. 基础配置
st.set_page_config(page_title="AI Soccer Hub", layout="wide")
st.title("🤖 实时足球赔率监测站")

# 2. 你的 API 密钥 (保持不变)
MY_KEY = "c9d1c77ce8msh35384666f22e8fdp17865ejsn9a531f8f3c7b"

# 3. 数据获取函数
def fetch_live_odds():
    # 注意：这里的 /odds 是关键
    url = "https://v3.football.api-sports.io"
    params = {"live": "all"}
    headers = {
        'x-rapidapi-key': MY_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    try:
        res = requests.get(url, headers=headers, params=params, timeout=15)
        return res.json()
    except Exception as e:
        st.error(f"连接失败: {e}")
        return None

# 4. 界面逻辑
if st.button("🎯 立即同步实时赔率"):
    with st.spinner('数据加载中...'):
        data = fetch_live_odds()
        
    if data and data.get('response'):
        results = data['response']
        st.success(f"成功找到 {len(results)} 场比赛的实时赔率")
        for item in results:
            l_name = item.get('league', {}).get('name', '未知联赛')
            with st.expander(f"🏆 {l_name}", expanded=True):
                bookies = item.get('bookmakers', [])
                if bookies:
                    # 获取 Match Winner 赔率
                    bets = bookies[0].get('bets', [])
                    main_bet = next((b for b in bets if b.get('name') == 'Match Winner'), None)
                    if main_bet:
                        vals = main_bet.get('values', [])
                        c1, c2, c3 = st.columns(3)
                        # 对应：主胜 / 平局 / 客胜
                        c1.metric("🏠 主胜", vals[0]['odd'])
                        c2.metric("🤝 平局", vals[1]['odd'])
                        c3.metric("🚌 客胜", vals[2]['odd'])
            st.divider()
    else:
        st.info("目前没有包含赔率的实时比赛，请稍后再试。")
#修改