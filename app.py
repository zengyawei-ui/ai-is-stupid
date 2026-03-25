import streamlit as st
import requests

# 1. 页面基础配置
st.set_page_config(page_title="足球情报站", layout="wide")
st.title("⚽️ 实时足球赔率监测站")

# 2. 从保险柜拿钥匙 (请确保 Secrets 里名字叫 MY_FOOTBALL_KEY)
MY_KEY = st.secrets["MY_FOOTBALL_KEY"]

# 3. 核心抓取函数
def fetch_live_odds():
    # 这里的 URL 和 Host 必须完全精确！
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

# 4. 界面逻辑：只有这一个按钮
if st.button("🎯 立即同步实时数据"):
    with st.spinner('正在搜寻全球赛场...'):
        data = fetch_live_odds()
        if data and data.get('response'):
            results = data['response']
            st.success(f"成功！已找到 {len(results)} 场实时比赛。")
            for item in results:
                # 提取联赛和球队
                l_name = item.get('league', {}).get('name', '未知联赛')
                home = item.get('teams', {}).get('home', {}).get('name', '主队')
                away = item.get('teams', {}).get('away', {}).get('name', '客队')
                
                with st.expander(f"🏆 {l_name}: {home} VS {away}"):
                    # 显示每一场比赛的博彩公司赔率数据
                    st.json(item.get('bookmakers', []))
        else:
            st.warning("⚠️ 目前暂无正在进行且有赔率更新的比赛，或 API 额度已满。")
