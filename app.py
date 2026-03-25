导入流光灯为st
导入请求

st.set_page_config(page_title=“足球情报站”, layout="wide")
st.title(“⚽️ 实时足球赔率监测站”)

# 从保险柜拿钥匙
MY_KEY = st.secrets["MY_FOOTBALL_KEY"]

def fetch_live_odds():
url=“https://api-sports.io”
参数={“现场”：“全部”}#抓取所有正在进行的比赛赔率
标题 = {
'x-rapidapi-key': MY_KEY，
'x-rapidapi-host':'v3.football.api-sports.io'
    }
尝试:
res = requests.get（url，params=params，header=header）
返回res.json（）
除非异常为e:
st.error（f）“连线失败：{e}”)
返回 无

如果st.button（“🎯 立即同步实时数据”):
斯皮纳（‘正在搜寻全球赛场...’）：
data = fetch_live_odds（）
        
        # 调试：看看API到底给了我们什么
如果数据:
results = data.get（'response'，[]）
如果没有结果:
st.warning（“⚠️API回传成功，但目前【全球没有正在进行】且【有赔率更新】的比赛。”)
st.info（“提示：您可以换个时间（如周六、周日赛事高峰期）再试。”)
其他:
st.成功（f）"找到{伦（结果）}场实时比赛！”)
对于结果中的项目:
联赛=项目。获得（“联赛”，{}）。获得（“名称”，“未知联赛”）
Home=item.get（队）.get（家）.get（名）.get（主队）
离开（项目）。得到（队伍）。
                    
带有st.expander（f）“🏆{联赛}: {主场} VS {客场}”):
                        # 显示最原始的赔率数据，确保我们没漏掉
博彩公司 = item.get（'博彩公司'，[]）
如果博彩公司:
st.json（博彩公司）
其他:
st.write（“这场比赛暂时没有博彩公司提供实时赔率。”)
其他:
st.error（“API请求失败，请检查您的钥匙（Secret）是否填对。”)
