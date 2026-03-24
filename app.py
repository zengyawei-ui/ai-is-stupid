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
    url = "https://v3.football.api-sports.io/odds"
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
                # 84行：获取赔率列表
                bets = bookies[0].get('bets', [])
                # 85行：查找 Match Winner 盘口
                main_bet = next((b for b in bets if b.get('name') == 'Match Winner'), None)
                
                # --- ⚠️ 关键增加：必须判断 main_bet 是否存在 ---
                if main_bet:
                    # 87行：你的字典推导式逻辑（修正后）
                    vals = {v['value']: v['odd'] for v in main_bet.get('values', [])}
                    
                    # 89行开始：展示界面
                    c1, c2, c3 = st.columns(3)
                    c1.metric("🏠 主胜", vals.get('Home', 'N/A'))
                    c2.metric("🤝 平局", vals.get('Draw', 'N/A'))
                    c3.metric("🚌 客胜", vals.get('Away', 'N/A'))
                else:
                    st.write("⚠️ 暂无 Match Winner 赔率")

               # 1. 这个 st.divider() 要和上面的 with st.expander(...) 对齐
            # 它的作用是每显示完一场比赛，画一条分割线
            st.divider()
            
    # 2. 这个 else 要和上面的 if data and data.get('response'): 对齐
    # 它的作用是：如果没有找到比赛，提示用户
    else:
        st.info("目前没有包含赔率的实时比赛，请稍后再试。")

# 3. 这个 st.caption 放在最左边，完全不缩进
# 它的作用是：在网页最底部留个小注脚
st.caption("数据来源：API-Football | 仅供参考")

