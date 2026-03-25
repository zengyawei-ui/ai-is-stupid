import streamlit as st
import requests

# 1. 基础配置
st.set_page_config(page_title="足球情报站", layout="wide")
st.title("⚽️ 实时足球赔率监测站")

# 2. 从“保险柜”获取钥匙
MY_KEY = st.secrets["MY_FOOTBALL_KEY"]

# 3. 数据获取函数
def fetch_live_odds():
    # 这里的地址必须是 /odds 才能抓到赔率！
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
        st.error(f"连接服务器失败: {e}")
        return None

# 4. 界面逻辑
if st.button("🎯 立即同步实时数据"):
    with st.spinner('正在搜寻全球赛场...'):
        data = fetch_live_odds()
        if data and data.get('response'):
            results = data['response']
            st.success(f"成功找到 {len(results)} 场实时比赛！")
            for item in results:
                l_name = item.get('league', {}).get('name', '未知联赛')
                home = item.get('teams', {}).get('home', {}).get('name', '主队')
                away = item.get('teams', {}).get('away', {}).get('name', '客队')
                with st.expander(f"🏆 {l_name}: {home} VS {away}"):
                    # 显示每一场比赛的博彩公司赔率
                    st.json(item.get('bookmakers', []))
        else:
            st.warning("目前没有正在进行的比赛，或 API 额度已用完。")
