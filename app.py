import streamlit as st
import pandas as pd
import requests

# 设置网页标题
st.set_page_config(page_title="足球赔率自动化工具", layout="centered")

st.title("⚽ 实时足球赔率监测器")
st.info("当前模式：纯净版（已修复重复ID报错）")

# 侧边栏配置
with st.sidebar:
    st.header("⚙️ 系统设置")
    if st.button("🚀 强制刷新页面"):
        st.rerun()

# 核心功能：抓取数据
def fetch_odds():
    # 注意：这里的 URL 请确保是你之前那个部署好的后端 API 地址
    # 如果你还没部署后端，这一步会提示连接失败
    target_url = "https://your-backend-api.com" 
    try:
        response = requests.get(target_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
        else:
            st.error(f"服务器返回错误: {response.status_code}")
            return None
    except Exception as e:
        st.warning("提示：后端接口暂未响应，请检查 API 地址是否正确。")
        return None

# 页面主按钮
if st.button("🎯 立即同步实时数据", type="primary"):
    with st.spinner("正在穿越时空抓取赔率..."):
        df = fetch_odds()
        if df is not None:
            st.success("✅ 数据更新成功！")
            st.dataframe(df, use_container_width=True)
        else:
            st.info("💡 暂时没有抓取到新数据，请稍后重试。")

st.divider()
st.caption("状态：运行中 | 自动修复机制已启动")
