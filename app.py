import random

import streamlit as st

st.set_page_config(
    page_title="🧧 给欧阳闻笳的 新年 小冒险",
    page_icon="🎆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============ 全局常量 ============
TARGET_NAME = "欧阳闻笳"

# ============ 自定义样式 ============
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700&display=swap');

    /* ====== 强制浅色主题：覆盖 Streamlit 深色模式 ====== */
    :root {
        color-scheme: light only !important;
    }
    html, body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    [data-testid="stMain"],
    .main,
    .main > div,
    section.main > div {
        background-color: #fffdf6 !important;
        color: #333 !important;
    }
    /* Streamlit 所有文本元素强制深色字 */
    .stApp p,
    .stApp span,
    .stApp label,
    .stApp li,
    .stApp div,
    .stApp [data-testid="stMarkdownContainer"],
    .stApp [data-testid="stMarkdownContainer"] p,
    .stApp [data-testid="stMarkdownContainer"] span,
    .stApp [data-testid="stCaptionContainer"] p,
    .stApp [data-testid="stCaptionContainer"] span {
        color: #434343 !important;
    }
    /* 标题强制深色 */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
        color: #262626 !important;
    }
    /* 分割线 */
    .stApp hr {
        border-color: #f0d9d0 !important;
        opacity: 0.6;
    }
    /* radio 选项文字 */
    .stApp .stRadio label span p,
    .stApp .stRadio > div > label > div > p,
    .stApp [role="radiogroup"] label {
        color: #434343 !important;
    }
    /* caption 文字（灰色） */
    .stApp [data-testid="stCaptionContainer"] p {
        color: #8c8c8c !important;
    }
    /* info/success/warning 框内文字 */
    .stApp [data-testid="stAlert"] p {
        color: #333 !important;
    }
    /* iframe 容器强制全宽 */
    .stApp iframe {
        width: 100% !important;
        min-width: 100% !important;
    }

    /* ====== 隐藏侧边栏与顶部控件 ====== */
    [data-testid="stSidebar"] { display: none; }
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stHeader"] { display: none; }
    footer { display: none; }

    /* ====== 收拢内容宽度 ====== */
    .block-container {
        padding-top: 2.2rem;
        padding-bottom: 2.2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 920px;
    }

    /* ====== 移动端适配 ====== */
    @media (max-width: 768px) {
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            padding-left: 0.75rem;
            padding-right: 0.75rem;
            max-width: 100%;
        }
        .main-title { font-size: 1.8rem !important; margin-bottom: 0.3rem; }
        .sub-title { font-size: 0.9rem !important; margin-bottom: 1rem; padding: 0 0.5rem; }
        .card { padding: 1rem !important; margin: 0.5rem 0 !important; }
        .comment-box { padding: 0.8rem 1rem !important; font-size: 0.9rem !important; margin: 0.6rem 0 !important; }
        .sign-container { padding: 1rem 0.8rem !important; margin: 0.5rem 0 !important; }
        .jar-emoji { font-size: 3rem !important; }
        .sign-result { padding: 1rem !important; margin: 0.8rem 0 !important; }
        .sign-level { font-size: 1rem !important; padding: 0.2rem 0.8rem !important; white-space: normal; word-wrap: break-word; }
        .blessing-card { padding: 1.5rem 1rem !important; margin: 1rem 0 !important; }
        .blessing-name { font-size: 1.3rem !important; }
        .blessing-level { font-size: 0.95rem !important; padding: 0.35rem 1rem !important; white-space: normal; word-wrap: break-word; }
        .blessing-text { font-size: 0.95rem !important; padding: 0 0.5rem !important; line-height: 1.8 !important; }
        .blessing-wish { font-size: 1rem !important; padding: 0.7rem 0.8rem !important; }
        .sign-summary { padding: 0.8rem 1rem !important; font-size: 0.9rem !important; }
        .final-emoji { font-size: 2rem !important; }
        .stButton>button { font-size: 0.95rem !important; padding: 0.5rem 1rem !important; }
        h1, h2, h3 { font-size: 1.3rem !important; }
        h2 { font-size: 1.2rem !important; }
        h3 { font-size: 1.1rem !important; }
    }

    /* ====== 自定义组件样式 ====== */
    .main-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        color: #d4380d !important;
        margin-bottom: 0.2rem;
        letter-spacing: 0.02em;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.08);
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .sub-title {
        text-align: center;
        font-size: 1.05rem;
        color: #8c8c8c !important;
        margin-top: 0;
        margin-bottom: 1.8rem;
        line-height: 1.7;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .sub-title b {
        color: #d4380d !important;
    }

    .welcome-box {
        background: linear-gradient(135deg, #fff1f0 0%, #fff7e6 100%) !important;
        border-radius: 18px;
        padding: 2rem;
        border: 1px solid #ffccc7;
        margin: 1rem 0;
        color: #434343 !important;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }

    .card {
        background: linear-gradient(135deg, #fff1f0 0%, #fff7e6 100%) !important;
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid #ffccc7;
        margin: 1rem 0;
        color: #434343 !important;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .comment-box {
        background: #fffbe6 !important;
        border: 1px solid #ffe58f;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin: 0.8rem 0;
        font-size: 1rem;
        color: #434343 !important;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .comment-box b {
        color: #d48806 !important;
    }

    .sign-container {
        background: linear-gradient(135deg, #fff1f0 0%, #fff7e6 100%) !important;
        border-radius: 16px;
        padding: 1.6rem 1.2rem;
        border: 1px solid #ffccc7;
        margin: 0.7rem 0;
        text-align: center;
        height: 100%;
        color: #434343 !important;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .sign-result {
        background: linear-gradient(135deg, #fffbe6 0%, #fff1f0 100%) !important;
        border-radius: 16px;
        padding: 1.5rem;
        border: 2px solid #faad14;
        margin: 1rem 0;
        text-align: center;
        color: #434343 !important;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .sign-level {
        font-size: 1.2rem;
        font-weight: 800;
        color: #cf1322 !important;
        background: #fff1f0 !important;
        display: inline-block;
        padding: 0.25rem 1.1rem;
        border-radius: 999px;
        border: 1px solid #ffa39e;
        margin: 0.5rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .jar-emoji {
        font-size: 4.2rem;
        display: block;
        text-align: center;
        margin: 0.3rem 0 0.6rem 0;
        cursor: pointer;
        transition: transform 0.3s;
    }
    .jar-emoji:hover { transform: scale(1.08); }

    .blessing-card {
        background: linear-gradient(135deg, #fff1f0 0%, #fff7e6 50%, #f6ffed 100%) !important;
        border-radius: 20px;
        padding: 2.2rem;
        border: 2px solid #ffccc7;
        margin: 1.2rem 0;
        text-align: center;
        box-shadow: 0 8px 32px rgba(255, 77, 79, 0.10);
        color: #434343 !important;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .blessing-name {
        font-size: 1.6rem;
        font-weight: 900;
        color: #d4380d !important;
        margin-bottom: 0.8rem;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .blessing-level {
        font-size: 1.1rem;
        color: #cf1322 !important;
        background: linear-gradient(135deg, #fff1f0, #fffbe6) !important;
        display: inline-block;
        padding: 0.45rem 1.2rem;
        border-radius: 999px;
        border: 1px solid #ffa39e;
        margin: 0.6rem 0 0 0;
        font-weight: 800;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .blessing-text {
        font-size: 1.12rem;
        color: #434343 !important;
        line-height: 2;
        margin: 1.2rem 0;
        text-align: left;
        padding: 0 0.8rem;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .blessing-text b {
        color: #d4380d !important;
    }
    .blessing-wish {
        font-size: 1.2rem;
        color: #d4380d !important;
        font-weight: 900;
        margin-top: 1.2rem;
        padding: 0.9rem 1rem;
        background: rgba(255, 77, 79, 0.06) !important;
        border-radius: 12px;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .sign-summary {
        background: #fffbe6 !important;
        border-radius: 12px;
        padding: 0.9rem 1.2rem;
        margin: 0.5rem 0;
        border: 1px solid #ffe58f;
        text-align: left;
        color: #434343 !important;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .sign-summary-title {
        font-weight: 900;
        color: #d48806 !important;
        margin-bottom: 0.2rem;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .final-emoji {
        font-size: 3rem;
        text-align: center;
        display: block;
        margin: 0.8rem 0 0.4rem 0;
    }

    .stButton>button {
        background: linear-gradient(135deg, #ff4d4f 0%, #ff7a45 100%) !important;
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-size: 1.05rem;
        font-weight: 800;
        width: 100%;
        transition: all 0.25s;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 18px rgba(255, 77, 79, 0.30);
    }
</style>
""",
    unsafe_allow_html=True,
)

# ============ 初始化 session state ============
defaults = {
    "stage": 1,  # 1=灵魂拷问，2=抽签，3=祝福
    "quiz_answers": {},
    "quiz_submitted": False,
    "quiz_done": False,
    "quiz_tendency": {"career": 0, "life": 0, "romance": 0, "all": 0},
    "sign_results": [],
    "sign_drawn": {"career": False, "life": False, "romance": False},
    "sign_done": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# 兼容旧 session：如果之前停在 stage=0，直接跳到第一关
if st.session_state.stage < 1:
    st.session_state.stage = 1


def goto_stage(stage: int) -> None:
    st.session_state.stage = stage
    st.rerun()


def reset_game() -> None:
    for k in list(defaults.keys()):
        if k in st.session_state:
            del st.session_state[k]
    st.rerun()


def render_progress() -> None:
    """单页流程进度条（替代侧边栏导航）。"""
    current = st.session_state.stage
    steps = [
        (1, "📝 第一关 · 灵魂拷问"),
        (2, "🎰 第二关 · 新年三签"),
        (3, "🎆 终章 · 专属祝福"),
    ]
    cols = st.columns(3)
    for (stage, label), col in zip(steps, cols):
        with col:
            if current == stage:
                st.markdown(f"**{label}**")
            else:
                st.caption(label)


# ============ 数据：关卡一（灵魂拷问）===========
questions = [
    {
        "id": "q1",
        "question": "过去一年，你最想对自己说的一句话是？",
        "options": [
            '"你已经很努力了，允许自己慢一点。"',
            '"别把周末活成加班的续集。"',
            '"勇敢一点，想见的人就去见。"',
            '"少一点内耗，多一点去感受。"',
        ],
        "comments": [
            "你不是机器人，你是会发光的人——偶尔没电很正常，插上充电器就好（充电器 = 吃好喝好睡饱）。",
            "你的周末不应该有工作的味道！下次周六闹钟响了请把手机扔枕头底下，翻个身继续睡。",
            "有句话说得好：种一棵树最好的时间是十年前，其次是现在。想见的人？现在就发消息。",
            "大脑内耗这件事吧，你越想越乱，不如出门买杯奶茶，回来发现——好了，想不起来刚才在纠结啥了。",
        ],
        "tendency": ["life", "life", "romance", "life"],
    },
    {
        "id": "q2",
        "question": '哪种瞬间最容易让你觉得"啊，活着真好"？',
        "options": [
            "冬天热饮第一口，手心跟着暖起来 ☕",
            "在路上：地铁窗、夜风、街灯，刚好都顺眼 🌙",
            "运动后出汗的那一刻，身体很诚实 🏃",
            "跟重要的人一起吃饭，话不多也不尴尬 🍜",
        ],
        "comments": [
            "一杯热饮就能拯救你的世界——你的快乐成本也太低了吧！（省钱体质实锤）",
            "别人看到地铁窗是自己的倒影，你看到的是人间值得。文艺青年，系统已标记。",
            '说白了就是：运动的时候在想"好累要死"，运动完在想"我怎么这么厉害"——人类的快乐就是这么朴实无华。',
            "不用说话也不尴尬——恭喜，这说明你找到了对的人。吃饭都能当约会。",
        ],
        "tendency": ["life", "life", "life", "romance"],
    },
    {
        "id": "q3",
        "question": "关于同行牛马人，你最真实的心声是？",
        "options": [
            "白天是流程与会议，晚上是脑子自动关机 🗂️",
            "能忙也能扛：认真就很酷（但也想被认真地对待）🧾",
            "偶尔会累，但仍然想把事情做漂亮一点 📌",
            "工作是工作，我还要把生活过成生活 🧡",
        ],
        "comments": [
            "白天开会的你 vs 晚上瘫沙发的你，像是同一具身体里住着两个灵魂——一个在工作，一个已经飞走了。",
            '你是那种嘴上说"好累啊"但手里活一点没停的人吧？系统替你的同事说一句：谢谢你，靠谱怪。',
            '完美主义本义不是"我要卷"，而是"丑的东西我看不下去"——好吧，这也是一种天赋。',
            '你已经学会了成年人最稀缺的技能：到点下班不愧疚。请收下系统颁发的"边界感大师"证书。',
        ],
        "tendency": ["career", "career", "career", "all"],
    },
    {
        "id": "q4",
        "question": "今年你最想解锁的一项小技能是？",
        "options": [
            "做一道拿手菜，能端上桌也能端得住 🍳",
            "学会更好地表达：温柔也要有力度 🗣️",
            "把运动坚持下来：不求狠，只求稳 🧘",
            "安排一次说走就走的小旅行：不远也很好 🚆",
        ],
        "comments": [
            '从"番茄炒蛋到底先放番茄还是鸡蛋"开始，你就已经踏上了大厨之路。加油，厨神在向你招手（先别着急，灭火器准备好了吗）。',
            '温柔地说出"不行"这件事确实很难——但你可以先从温柔地说"我再想想"开始，已经很厉害了。',
            "运动这件事跟存钱一样：开始很痛苦，坚持一段时间后……依然很痛苦，但看到效果那一刻真的值。",
            '小旅行的精髓不在"远不远"，在于出发那一刻心里想的是"管他呢"——这三个字价值连城。',
        ],
        "tendency": ["life", "romance", "life", "life"],
    },
    {
        "id": "q5",
        "question": f'如果把 2026 送给 {TARGET_NAME} 一张"心愿券"，你更想写什么？',
        "options": [
            '"忙的时候也别忘了吃饭、喝水、睡觉。"',
            '"愿你被理解，也被偏爱；被照顾，也被尊重。"',
            '"我们一起把普通日子，过得更有趣一点。"',
            '"愿你工作顺利，心里也一直有光。"',
        ],
        "comments": [
            "你给出的不是大道理，是很具体的唠叨——但这种唠叨比任何情话都管用。（别怀疑，这就是爱。）",
            "你在认真爱人：不控制，只祝福。系统建议把这句话裱起来，挂在床头。",
            "喜欢这种调调：不许愿一夜暴富，只想把每一天过得有滋有味。你是懂生活的。",
            '你很会：把"盼你开心"说得不肉麻还很高级——文案鬼才，哪个公司挖你去写广告了？',
        ],
        "tendency": ["romance", "romance", "romance", "career"],
    },
    {
        "id": "q6",
        "question": "最后一题：你希望你们的关系更像什么？",
        "options": [
            "像一盏灯：不刺眼，但一直在 🕯️",
            "像一条路：并肩走，各自也能奔跑 🛤️",
            "像一杯热茶：淡淡的，但回甘很久 🍵",
            "像一场游戏：认真玩，偶尔也耍赖 🎮",
        ],
        "comments": [
            "低调而持久的浪漫——你不要烟花，你要篝火。高级。",
            "你要的是队友，不是保姆也不是老板。恭喜，你已经想通了 99% 的人还没想通的事。",
            "回甘型选手——慢热但一旦爱上就很稳。你不是不浪漫，你只是不爱说。",
            "懂了懂了：你要的是有人陪你一起打怪升级，偶尔还能互相坑一下的那种。神仙关系！",
        ],
        "tendency": ["romance", "romance", "romance", "all"],
    },
]

# ============ 数据：关卡二（抽签）===========
career_signs = [
    {
        "level": "上上签 · 稳稳拿捏",
        "text": f"{TARGET_NAME} 今年职场运势拉满：同事越来越靠谱，节奏越来越清晰。\n加班？偶尔的。成就感？管够的。\n总之就是：老板看你的眼神都带光。",
    },
    {
        "level": "上签 · 体面推进",
        "text": '今年你会解锁一项新技能：优雅地说"不"。\n不再硬扛，因为会有人抢着帮你。\n（对，就是那种让你怀疑"是不是在做梦"的好运。）',
    },
    {
        "level": "吉签 · 忙而不乱",
        "text": "项目多一点，会也多一点——但你的取舍能力也在偷偷升级。\n该花精力的花精力，该摸鱼的……嗯，高效休息。\n忙，但忙得明白。",
    },
    {
        "level": "妙签 · 换个角度就顺了",
        "text": '今年你的外挂叫"沟通力+10"。\n以前觉得难搞的事，换个说法就通了。\n以前觉得难搞的人……好吧，多喝热水，保持微笑。',
    },
    {
        "level": "温柔签 · 别忘了你自己",
        "text": "温馨提醒：你不是公司的一块砖，不需要哪里需要哪里搬。\n今年你会发现一个真理：休息好了，反而效率更高。\n（这不是偷懒，这是科学。）",
    },
]

life_signs = [
    {
        "level": "上上签 · 日子会更甜",
        "text": "今年你的幸运值疯狂上涨：好吃的晚饭、好看的天空、好听的歌，全都自动找上门。\n别人叫小确幸，你叫日常配置。\n生活不需要很大声，你的甜自己会冒泡。",
    },
    {
        "level": "上签 · 身心都轻一点",
        "text": '今年你的身体会跟你和解：睡眠变好，运动变规律。\n以前是"明天再说"，今年是"现在就去"。\n不是突然自律了，是终于学会心疼自己了。',
    },
    {
        "level": "福签 · 出门见世界",
        "text": '今年适合一起出发：吹海风、看群山、走陌生的街道。\n不一定要很远，但一定要有人在旁边说"快看那个"。\n山河路远？有人陪就不远。',
    },
    {
        "level": "妙签 · 热爱回归",
        "text": "希望可以一起经历那些热爱：拍照、潜水、做饭、读书、看展、当然还有滑雪……\n它会在你疲惫时托住你。",
    },
    {
        "level": "治愈签 · 日常自有温柔",
        "text": "泡一杯热茶、买一束花、整理衣橱、清理手机里的旧照片。\n如果有机会一起把日子打理好，幸运和好事就慢慢靠近了。",
    },
]

romance_signs = [
    {
        "level": "上上签 · 心动有回声",
        "text": f"{TARGET_NAME} 今年的感情运势是：你发出的信号，全部被精准接收。\n不说出口的小情绪？有人秒懂。\n偶尔的小脾气？有人觉得可爱。（赢麻了属于是。）",
    },
    {
        "level": "上签 · 默契升级",
        "text": '你们的默契今年会进化到"一个眼神就够了"的程度。\n吵架？越来越少。拥抱？越来越多。\n别人在羡慕，你们在享受。',
    },
    {
        "level": "喜签 · 小浪漫更耐久",
        "text": "比起烟花式的惊天动地，你们更适合细水长流那一款：\n记住对方爱吃什么、怕冷还是怕热、今天心情好不好。\n这种浪漫不炸裂，但保质期特别长。",
    },
    {
        "level": "实在签 · 认真生活就是浪漫",
        "text": '真正的浪漫不是朋友圈里的九宫格，\n而是忙到飞起还记得说一句"吃了吗"。\n是说"我在"，更是做到"我在"——靠谱，就是最高级的情话。',
    },
    {
        "level": "温柔签 · 你值得被爱",
        "text": "今年请大胆展示你的可爱值，不要藏着掖着。\n地球这么大，总有颗小行星等着跟你撞个满怀。\n（撞完之后发现：嘿，你也在这儿啊。）",
    },
]

category_names = {"career": "💼 职场节奏签", "life": "🍃 生活状态签", "romance": "💌 心动默契签"}


# ============ 顶部标题 ============
st.markdown('<div class="main-title">辞岁 小结 · 新年 好运</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="sub-title">这不是考试，没有标准答案，答错了也不扣分。<br>这是一个送给 <b>{TARGET_NAME}</b> 的新年小冒险——请放松，深呼吸，然后随便选。</div>',
    unsafe_allow_html=True,
)
st.markdown("---")
render_progress()
st.markdown("")


# ============ Stage 1：年度灵魂拷问 ============
if st.session_state.stage == 1:
    st.markdown("## 📝 第一关：年度灵魂拷问")
    st.caption("放心，不是真的拷问——就是几个灵魂小问题，答完你会更了解自己（也可能更迷茫，但没关系）。")
    st.markdown("---")

    if not st.session_state.quiz_submitted:
        for i, q in enumerate(questions):
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"### Q{i+1}：{q['question']}")
            key = f"quiz_{q['id']}"
            choice = st.radio(
                "选择你的答案：",
                q["options"],
                key=key,
                index=None,
                label_visibility="collapsed",
            )
            if choice is not None:
                idx = q["options"].index(choice)
                st.session_state.quiz_answers[q["id"]] = idx
                st.markdown(
                    f'<div class="comment-box">💬 <b>系统悄悄话：</b>{q["comments"][idx]}</div>',
                    unsafe_allow_html=True,
                )
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")
        all_answered = len(st.session_state.quiz_answers) == len(questions)
        if not all_answered:
            st.info(f"📋 已完成 {len(st.session_state.quiz_answers)}/{len(questions)} 题——别磨蹭啦，好运不等人！")

        if st.button("✅ 提交并进入第二关", disabled=not all_answered, use_container_width=True):
            tendency = {"career": 0, "life": 0, "romance": 0, "all": 0}
            for q in questions:
                ans_idx = st.session_state.quiz_answers.get(q["id"])
                if ans_idx is None:
                    continue
                t = q["tendency"][ans_idx]
                tendency[t] += 1
            st.session_state.quiz_tendency = tendency
            st.session_state.quiz_done = True
            st.session_state.quiz_submitted = True
            st.balloons()
            goto_stage(2)

    else:
        st.success("✅ 第一关已完成！")
        if st.button("继续第二关 →", use_container_width=True):
            goto_stage(2)
        if st.button("🔄 重新答题", use_container_width=True):
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.session_state.quiz_done = False
            st.session_state.quiz_tendency = {"career": 0, "life": 0, "romance": 0, "all": 0}
            st.rerun()


# ============ Stage 2：新年三签 ============
if st.session_state.stage == 2:
    if not st.session_state.quiz_done:
        st.warning("⚠️ 先完成第一关才能抽签哦～")
        if st.button("返回第一关", use_container_width=True):
            goto_stage(1)
    else:
        st.markdown("## 🎰 第二关：新年三签")
        st.caption("三支签，三个维度，一个都不能少。友情提示：这里没有下下签，放心大胆抽，手气差也差不到哪去。")
        st.markdown("---")

        all_done = all(st.session_state.sign_drawn.values())
        if not all_done:
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown('<div class="sign-container">', unsafe_allow_html=True)
                st.markdown('<span class="jar-emoji">💼</span>', unsafe_allow_html=True)
                st.markdown("**职场节奏签**")
                if st.session_state.sign_drawn["career"]:
                    st.markdown("✅ 已抽")
                else:
                    if st.button("🎋 抽一签", key="draw_career"):
                        career_t = st.session_state.quiz_tendency.get("career", 0)
                        weights = [30, 25, 20, 15, 10] if career_t >= 2 else [22, 22, 22, 18, 16]
                        result = random.choices(career_signs, weights=weights, k=1)[0]
                        st.session_state.sign_results.append(("career", result))
                        st.session_state.sign_drawn["career"] = True
                        st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="sign-container">', unsafe_allow_html=True)
                st.markdown('<span class="jar-emoji">🍃</span>', unsafe_allow_html=True)
                st.markdown("**生活状态签**")
                if st.session_state.sign_drawn["life"]:
                    st.markdown("✅ 已抽")
                else:
                    if st.button("🎋 抽一签", key="draw_life"):
                        life_t = st.session_state.quiz_tendency.get("life", 0)
                        weights = [28, 24, 20, 16, 12] if life_t >= 3 else [22, 22, 22, 18, 16]
                        result = random.choices(life_signs, weights=weights, k=1)[0]
                        st.session_state.sign_results.append(("life", result))
                        st.session_state.sign_drawn["life"] = True
                        st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

            with col3:
                st.markdown('<div class="sign-container">', unsafe_allow_html=True)
                st.markdown('<span class="jar-emoji">💌</span>', unsafe_allow_html=True)
                st.markdown("**心动默契签**")
                if st.session_state.sign_drawn["romance"]:
                    st.markdown("✅ 已抽")
                else:
                    if st.button("🎋 抽一签", key="draw_romance"):
                        rom_t = st.session_state.quiz_tendency.get("romance", 0)
                        weights = [30, 25, 20, 15, 10] if rom_t >= 3 else [22, 22, 22, 18, 16]
                        result = random.choices(romance_signs, weights=weights, k=1)[0]
                        st.session_state.sign_results.append(("romance", result))
                        st.session_state.sign_drawn["romance"] = True
                        st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.sign_results:
            st.markdown("### 📜 你抽到的签")
            for cat, result in st.session_state.sign_results:
                st.markdown(
                    f"""
<div class="sign-result">
  <div style="font-size:0.95rem; color:#8c8c8c !important; margin-bottom:0.4rem; word-wrap:break-word; overflow-wrap:break-word;">{category_names.get(cat, cat)}</div>
  <div class="sign-level">{result['level']}</div>
  <div style="font-size:1.05rem; color:#434343 !important; line-height:1.85; margin-top:0.8rem; word-wrap:break-word; overflow-wrap:break-word;">
    {result['text'].replace(chr(10), '<br>')}
  </div>
</div>
<style>
@media (max-width: 768px) {{
  .sign-result div[style*="font-size:1.05rem"] {{
    font-size: 0.9rem !important;
    line-height: 1.6 !important;
  }}
  .sign-result div[style*="font-size:0.95rem"] {{
    font-size: 0.85rem !important;
  }}
}}
</style>
""",
                    unsafe_allow_html=True,
                )

        all_done = all(st.session_state.sign_drawn.values())
        if all_done:
            st.session_state.sign_done = True
            st.markdown("---")
            st.success("✅ 第二关完成！你的运势已收集完毕，接下来是最后的大招——专属祝福。")
            if st.button("🎆 进入终章", use_container_width=True):
                goto_stage(3)
            if st.button("🔄 重新抽签", use_container_width=True):
                st.session_state.sign_results = []
                st.session_state.sign_drawn = {"career": False, "life": False, "romance": False}
                st.session_state.sign_done = False
                st.rerun()


# ============ Stage 3：专属祝福 ============
if st.session_state.stage == 3:
    if not st.session_state.sign_done:
        st.warning("⚠️ 先把第二关抽签完成，祝福才会完整出现哦～")
        if st.button("返回第二关", use_container_width=True):
            goto_stage(2)
    else:
        st.snow()
        st.markdown('<p class="final-emoji">🎆🧧🎇</p>', unsafe_allow_html=True)
        st.markdown("## 🎆 你的专属新年祝福")
        st.caption("前方高能预警：一大波走心文字正在靠近。建议准备好纸巾（感动用的，不是伤心用的）。")
        st.markdown("---")

        # 签文回顾
        if st.session_state.sign_results:
            st.markdown("### 📜 签文回顾")
            for cat, result in st.session_state.sign_results:
                st.markdown(
                    f"""
<div class="sign-summary">
  <div class="sign-summary-title">{category_names.get(cat, cat)}：{result['level']}</div>
</div>
""",
                    unsafe_allow_html=True,
                )
            st.markdown("")

        tendency = st.session_state.get("quiz_tendency", {})
        max_key = max(tendency, key=tendency.get) if tendency else "all"
        tendency_titles = {
            "career": "💼 职场上闷声干大事的狠人",
            "life": "🍃 把普通日子过出花来的高手",
            "romance": "💌 嘴上不说但心里全是你的人",
            "all": "🌟 什么都想要而且真的都能行的人",
        }
        tendency_blessings = {
            "career": f"""
<div class="blessing-text">
<b>{TARGET_NAME}</b>，始终如一的你：<br><br>
时光微澜，你在复杂与纷扰中，将一切打理得安稳妥帖。说白了就是——别人还在手忙脚乱，你已经面不改色地全搞定了。很厉害，但也很心疼你。<br><br>
2026 年，愿你：<br>
- 三餐有滋味，夜眠有安稳（特别是不要再凌晨一点还回消息了行不行）<br>
- 温柔设界，该说"我不行"的时候别硬撑<br>
- 你的努力有人懂，你的小小苦恼有人用心呵护<br>
- 四季流转里有人与共，偶尔也能理直气壮地偷个懒<br><br>
请记得：山高路远，总有人为你点灯。偶尔停下来不是认输，是给自己充电——毕竟，充满电的你才最闪。
</div>
<div class="blessing-wish">愿你脚步从容，内心有光，前路有人同行，烦恼有人听——"山一程，水一程，身向远方心自安。"</div>
""",
            "life": f"""
<div class="blessing-text">
<b>{TARGET_NAME}</b>，细心生活的你：<br><br>
你是那种去超市都能逛出幸福感的人——挑一瓶好看的酱油都觉得日子有盼头。这不是矫情，这是天赋。<br>
"人间烟火气，最抚凡人心。"你活成了这句话本身。<br><br>
愿你：<br>
- 生活不止是待办清单，更是一场随心的旅行（偶尔走错路也是风景）<br>
- 跟自己和解，不苛求完美——你已经够好了，真的<br>
- 热爱永远在线，疲惫时有人给你靠岸<br>
- 晴天一起出门浪，雨天一起窝着看电影<br><br>
日子嘛，不需要轰轰烈烈，细水长流就很了不起。
</div>
<div class="blessing-wish">愿你清风徐来，温柔常在——"岁月悠悠，且以温柔共赴。"</div>
""",
            "romance": f"""
<div class="blessing-text">
<b>{TARGET_NAME}</b>，温柔且坚定的你：<br><br>
你是那种不会说很多甜言蜜语、但默默把所有事都记在心里的人。别人觉得你高冷，了解你的人知道——你只是嘴笨，心一点不笨。<br><br>
2026 年，愿你：<br>
- 所思有人懂，所爱有回响（发的消息不用等太久就能收到回复那种）<br>
- 心动有人安放，小情绪有人接住——哪怕是"今天有点烦"这种，也有人认真在听<br>
- 忙碌中依然保留爱的仪式感：哪怕只是一句晚安，也认认真真的<br>
- 独处时自得其乐，在一起时互相发光<br><br>
浪漫不需要花里胡哨，用心过好每一天就已经很了不起了。
</div>
<div class="blessing-wish">愿你所感所盼，都能温柔落地——"人间烟火处，有你也有我。"</div>
""",
            "all": f"""
<div class="blessing-text">
<b>{TARGET_NAME}</b>，自带光芒的你：<br><br>
你在风雨中沉静前行，也始终保有善良与温情。“纵有疾风起，人生不言弃。”<br><br>
2026 年，愿你：<br>
- 顺利自在，身心安泰，所求所愿皆有回响<br>
- 人海茫茫，有人懂你欢喜，也能容你孤独<br>
- 拥有把平凡日子过得有趣的能力，把温暖留给值得的人<br>
- 心中常有诗意，眼里偶有星光<br><br>
愿你被这世界温柔以待，但也懂得温柔待己。
</div>
<div class="blessing-wish">愿你身在远方，心有归处，如“山河远阔，人间烟火，皆甘露。”</div>
""",
        }
        title = tendency_titles.get(max_key, tendency_titles["all"])
        blessing_html = tendency_blessings.get(max_key, tendency_blessings["all"])

        st.markdown(
            f"""
<div class="blessing-card">
  <div class="blessing-name">🧧 致 {TARGET_NAME}</div>
  <div class="blessing-level">{title}</div>
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(blessing_html, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown(
            f"""
<div style="text-align:center; padding:1.5rem 0 0.5rem 0;">
  <div style="font-size:2.1rem; font-weight:900; color:#d4380d !important; word-wrap:break-word; overflow-wrap:break-word;">
    🎊 新年快乐，{TARGET_NAME}！
  </div>
  <div style="font-size:1.05rem; color:#c4956a !important; margin-top:1.2rem; font-style:italic; letter-spacing:0.1em;">
    —— 姜楠
  </div>
</div>
<style>
@media (max-width: 768px) {{
  div[style*="font-size:2.1rem"] {{
    font-size: 1.5rem !important;
  }}
  div[style*="font-size:1.05rem"] {{
    font-size: 0.95rem !important;
  }}
}}
</style>
""",
            unsafe_allow_html=True,
        )

        st.markdown("### 🎇 小小烟花")

        # ---- 纯 CSS 烟花动画，不需要 JavaScript / iframe / canvas ----
        # 直接通过 st.markdown 嵌入，100% 兼容所有移动浏览器
        st.markdown('''
<style>
.fw-sky {
  width: 100%;
  height: 340px;
  background: linear-gradient(to bottom, #060620 0%, #0d1b3e 60%, #111845 100%);
  border-radius: 14px;
  position: relative;
  overflow: hidden;
  margin: 0.5rem 0;
}
/* 小星星背景 */
.fw-sky::before {
  content: "";
  position: absolute;
  width: 100%; height: 100%;
  background-image:
    radial-gradient(1px 1px at 10% 15%, rgba(255,255,255,0.6), transparent),
    radial-gradient(1px 1px at 25% 50%, rgba(255,255,255,0.5), transparent),
    radial-gradient(1px 1px at 45% 10%, rgba(255,255,255,0.4), transparent),
    radial-gradient(1px 1px at 60% 65%, rgba(255,255,255,0.5), transparent),
    radial-gradient(1px 1px at 75% 30%, rgba(255,255,255,0.6), transparent),
    radial-gradient(1px 1px at 90% 70%, rgba(255,255,255,0.4), transparent),
    radial-gradient(1px 1px at 35% 80%, rgba(255,255,255,0.3), transparent),
    radial-gradient(1px 1px at 85% 85%, rgba(255,255,255,0.5), transparent),
    radial-gradient(1px 1px at 55% 40%, rgba(255,255,255,0.3), transparent),
    radial-gradient(1px 1px at 5% 90%, rgba(255,255,255,0.4), transparent);
  animation: fw-twinkle 3s ease-in-out infinite alternate;
}
@keyframes fw-twinkle { 0%{opacity:0.5} 100%{opacity:1} }

/* 每个烟花=上升线 + 爆炸球 */
.fw-rocket {
  position: absolute;
  bottom: 0;
  width: 2px;
  background: linear-gradient(to top, transparent, var(--fw-c));
  animation: fw-rise var(--fw-dur) ease-in infinite;
  animation-delay: var(--fw-delay);
  opacity: 0;
}
@keyframes fw-rise {
  0%   { height: 0; opacity: 0; bottom: 0; }
  10%  { opacity: 1; }
  45%  { height: var(--fw-h); opacity: 1; bottom: calc(100% - var(--fw-h) - var(--fw-top)); }
  50%  { height: 0; opacity: 0; bottom: calc(100% - var(--fw-top)); }
  100% { height: 0; opacity: 0; }
}

.fw-burst {
  position: absolute;
  width: 6px; height: 6px;
  border-radius: 50%;
  top: var(--fw-top);
  left: var(--fw-left);
  transform: translate(-50%, -50%);
  animation: fw-boom var(--fw-dur) ease-out infinite;
  animation-delay: var(--fw-delay);
  opacity: 0;
}
@keyframes fw-boom {
  0%   { opacity: 0; transform: translate(-50%,-50%) scale(0);
         box-shadow: 0 0 0 0 var(--fw-c); }
  45%  { opacity: 0; transform: translate(-50%,-50%) scale(0); }
  50%  { opacity: 1; transform: translate(-50%,-50%) scale(1);
         box-shadow:
           0 0 6px 2px var(--fw-c),
           0 -30px 0 0px var(--fw-c),  0 30px 0 0px var(--fw-c),
           30px 0 0 0px var(--fw-c),   -30px 0 0 0px var(--fw-c),
           21px -21px 0 0px var(--fw-c), -21px 21px 0 0px var(--fw-c),
           21px 21px 0 0px var(--fw-c),  -21px -21px 0 0px var(--fw-c),
           0 -55px 0 0px var(--fw-c2),  0 55px 0 0px var(--fw-c2),
           55px 0 0 0px var(--fw-c2),   -55px 0 0 0px var(--fw-c2),
           39px -39px 0 0px var(--fw-c2), -39px 39px 0 0px var(--fw-c2),
           39px 39px 0 0px var(--fw-c2),  -39px -39px 0 0px var(--fw-c2),
           15px -50px 0 0px var(--fw-c), -15px 50px 0 0px var(--fw-c),
           50px -15px 0 0px var(--fw-c), -50px 15px 0 0px var(--fw-c);
  }
  80%  { opacity: 0.6; transform: translate(-50%,-50%) scale(1.3);
         box-shadow:
           0 0 8px 0 transparent,
           0 -60px 0 -1px var(--fw-c),  0 65px 0 -1px var(--fw-c),
           60px 5px 0 -1px var(--fw-c),  -60px 5px 0 -1px var(--fw-c),
           42px -37px 0 -1px var(--fw-c), -42px 43px 0 -1px var(--fw-c),
           42px 43px 0 -1px var(--fw-c),  -42px -37px 0 -1px var(--fw-c),
           0 -100px 0 -1px var(--fw-c2), 0 105px 0 -1px var(--fw-c2),
           100px 5px 0 -1px var(--fw-c2), -100px 5px 0 -1px var(--fw-c2),
           71px -66px 0 -1px var(--fw-c2), -71px 76px 0 -1px var(--fw-c2),
           71px 76px 0 -1px var(--fw-c2),  -71px -66px 0 -1px var(--fw-c2),
           25px -90px 0 -1px var(--fw-c), -25px 95px 0 -1px var(--fw-c),
           90px -20px 0 -1px var(--fw-c), -90px 25px 0 -1px var(--fw-c);
  }
  100% { opacity: 0; transform: translate(-50%,-50%) scale(1.5);
         box-shadow: 0 0 0 0 transparent; }
}

/* 祝福文字浮动 */
.fw-text {
  position: absolute;
  bottom: 18px;
  width: 100%;
  text-align: center;
  color: #ffd666 !important;
  font-size: 1.1rem;
  font-weight: 700;
  text-shadow: 0 0 12px rgba(255,214,102,0.5);
  letter-spacing: 0.15em;
  animation: fw-glow 2s ease-in-out infinite alternate;
  z-index: 10;
}
@keyframes fw-glow { 0%{opacity:0.7;text-shadow:0 0 8px rgba(255,214,102,0.3)} 100%{opacity:1;text-shadow:0 0 18px rgba(255,214,102,0.7)} }
@media (max-width: 768px) {
  .fw-sky { height: 260px; }
  .fw-text { font-size: 0.9rem; bottom: 12px; }
}
</style>

<div class="fw-sky">
  <!-- 烟花1：红色 左侧 -->
  <div class="fw-rocket" style="left:18%;--fw-c:#ff4d4f;--fw-h:120px;--fw-top:60px;--fw-dur:3.2s;--fw-delay:0s;"></div>
  <div class="fw-burst" style="--fw-left:18%;--fw-top:60px;--fw-c:#ff4d4f;--fw-c2:#ff7a45;--fw-dur:3.2s;--fw-delay:0s;"></div>

  <!-- 烟花2：金色 中间偏右 -->
  <div class="fw-rocket" style="left:55%;--fw-c:#ffc53d;--fw-h:140px;--fw-top:45px;--fw-dur:3.8s;--fw-delay:0.6s;"></div>
  <div class="fw-burst" style="--fw-left:55%;--fw-top:45px;--fw-c:#ffc53d;--fw-c2:#ffa940;--fw-dur:3.8s;--fw-delay:0.6s;"></div>

  <!-- 烟花3：粉色 右侧 -->
  <div class="fw-rocket" style="left:80%;--fw-c:#ff85c0;--fw-h:110px;--fw-top:70px;--fw-dur:3.5s;--fw-delay:1.2s;"></div>
  <div class="fw-burst" style="--fw-left:80%;--fw-top:70px;--fw-c:#ff85c0;--fw-c2:#b37feb;--fw-dur:3.5s;--fw-delay:1.2s;"></div>

  <!-- 烟花4：蓝色 中间偏左 -->
  <div class="fw-rocket" style="left:35%;--fw-c:#69b1ff;--fw-h:130px;--fw-top:50px;--fw-dur:4.0s;--fw-delay:1.8s;"></div>
  <div class="fw-burst" style="--fw-left:35%;--fw-top:50px;--fw-c:#69b1ff;--fw-c2:#5cdbd3;--fw-dur:4.0s;--fw-delay:1.8s;"></div>

  <!-- 烟花5：绿色 右偏 -->
  <div class="fw-rocket" style="left:68%;--fw-c:#95de64;--fw-h:100px;--fw-top:80px;--fw-dur:3.3s;--fw-delay:2.4s;"></div>
  <div class="fw-burst" style="--fw-left:68%;--fw-top:80px;--fw-c:#95de64;--fw-c2:#fff566;--fw-dur:3.3s;--fw-delay:2.4s;"></div>

  <!-- 烟花6：紫色 左偏 -->
  <div class="fw-rocket" style="left:10%;--fw-c:#b37feb;--fw-h:95px;--fw-top:90px;--fw-dur:3.6s;--fw-delay:2.8s;"></div>
  <div class="fw-burst" style="--fw-left:10%;--fw-top:90px;--fw-c:#b37feb;--fw-c2:#ff85c0;--fw-dur:3.6s;--fw-delay:2.8s;"></div>

  <!-- 烟花7：橙色 中间 -->
  <div class="fw-rocket" style="left:45%;--fw-c:#ff7a45;--fw-h:150px;--fw-top:35px;--fw-dur:4.2s;--fw-delay:0.3s;"></div>
  <div class="fw-burst" style="--fw-left:45%;--fw-top:35px;--fw-c:#ff7a45;--fw-c2:#ffc53d;--fw-dur:4.2s;--fw-delay:0.3s;"></div>

  <!-- 烟花8：青色 右边 -->
  <div class="fw-rocket" style="left:90%;--fw-c:#5cdbd3;--fw-h:105px;--fw-top:75px;--fw-dur:3.9s;--fw-delay:1.5s;"></div>
  <div class="fw-burst" style="--fw-left:90%;--fw-top:75px;--fw-c:#5cdbd3;--fw-c2:#69b1ff;--fw-dur:3.9s;--fw-delay:1.5s;"></div>

  <div class="fw-text">✨ 新年快乐 · 烟花为你而绽放 ✨</div>
</div>
''', unsafe_allow_html=True)

        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 重新开始整个游戏", use_container_width=True):
                reset_game()
        with col2:
            if st.button("📸 截图分享", use_container_width=True):
                st.info('💡 直接截屏保存这一页就好啦～发给 TA 的时候记得配一句"这是我专门给你整的"（装作很随意的样子）。')

