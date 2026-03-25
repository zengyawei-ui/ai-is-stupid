import streamlit as st
import requests

# 1. 从“保险柜”拿钥匙（这样 GitHub 上就看不到你的真钥匙了）
# 确保你在 Streamlit 的 Advanced Settings 里填的是这个名字
MY_KEY = st.secrets["MY_FOOTBALL_KEY"]

# 2. 基础配置
st.set_page_config(page_title="AI Soccer Odds")
st.title("⚽️ 实时足球赔率监测站")

# 3. 数据获取函数
def fetch_live_odds():
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
        st.error(f"获取数据失败: {e}")
        return None

# 4. 界面逻辑
if st.button("🎯 立即同步实时赔率"):
    with st.spinner('正在调取全球数据...'):
        data = fetch_live_odds()
        if data and data.get('response'):
            results = data['response']
            st.success(f"成功找到 {len(results)} 场实时比赛赔率！")
            
            for item in results:
                l_name = item.get('league', {}).get('name', '未知联赛')
                fixture = item.get('fixture', {})
                home = item.get('teams', {}).get('home', {}).get('name', '主队')
                away = item.get('teams', {}).get('away', {}).get('name', '客队')
                
                with st.expander(f"🏆 {l_name}: {home} vs {away}"):
                    st.write("实时赔率数据已更新（详细数据见下方日志）")
                    st.json(item.get('bookmakers', []))
        else:
            st.warning("目前没有正在进行的比赛或 API 额度已用完。")
