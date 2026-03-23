import streamlit as st
import requests

# 1. 页面配置
st.set_page_config(page_title="AI也会笨 - 私人数据站", layout="wide")
st.title("🤖 AI也会笨 - 实时足球数据站")

# 2. API 配置 (请确保这里的 Key 是正确的)
MY_KEY = "c9d1c77ce8msh35384666f22e8fdp17865ejsn9a531f8f3c7b"

# 3. 定义获取数据的函数
def fetch_data():
    # 这里使用了获取“即时赔率”的接口，你可以根据需要修改 endpoint
    url = "https://v3.football.api-sports.io"
    headers = {
        'x-rapidapi-key': MY_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        st.error(f"❌ 获取数据失败: {e}")
        return None

# 4. 侧边栏温馨提示
st.sidebar.title("📌 账户信息")
st.sidebar.info("💡 温馨提示：M-Pesa 每日转账限额为 500,000 KES，请合理安排。")
st.sidebar.markdown("---")

# 5. 主页面交互
if st.button("🎯 点击获取实时信号"):
    with st.spinner('正在连接 API 抓取最新盘口...'):
        data = fetch_data()
        
    if data and data.get('response'):
        results = data['response']
        st.success(f"✅ 成功找到 {len(results)} 场实时比赛信号！")
        
        # 遍历每一场比赛
        for item in results:
            # 提取球队名称
            home_name = item['fixture']['status']['long'] # 状态
            league_name = item['league']['name']
            
            # 由于赔率接口数据结构深，我们安全地提取球队名（假设是 fixture 模式）
            # 注意：不同的 endpoint 返回结构略有不同，这里做了通用兼容处理
            st.markdown(f"### 🏆 {league_name}")
            
            bookies = item.get('bookmakers', [])
            if bookies:
                # 取第一家博彩公司
                first_b = bookies[0]
                st.caption(f"📊 数据源: {first_b['name']}")
                
                # 寻找胜负平 (Match Winner) 盘口
                all_bets = first_b.get('bets', [])
                main_bet = next((b for b in all_bets if b['name'] == 'Match Winner'), None)
                
                if main_bet:
                    # 漂亮的三列排版显示赔率
                    c1, c2, c3 = st.columns(3)
                    vals = main_bet['values']
                    
                    try:
                        # 自动显示主、平、客的赔率
                        c1.metric(label=f"🏠 {vals[0]['value']}", value=vals[0]['odd'])
                        c2.metric(label=f"🤝 {vals[1]['value']}", value=vals[1]['odd'])
                        c3.metric(label=f"🚌 {vals[2]['value']}", value=vals[2]['odd'])
                    except (IndexError, KeyError):
                        st.warning("⚠️ 赔率数据格式不全")
                else:
                    st.info("💡 该场比赛暂无胜负平赔率")
            else:
                st.warning("⚠️ 暂无实时盘口数据")
            
            st.markdown("---") # 每一场比赛后的分割线
    else:
        st.info("📭 目前没有符合条件的实时信号，请稍后再试。")

# 底部声明
st.caption("数据实时更新自 API-Sports | 由 AI也会笨 强力驱动")
