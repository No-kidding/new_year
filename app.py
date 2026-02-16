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
            "“你已经很努力了，允许自己慢一点。”",
            "“别把周末活成加班的续集。”",
            "“勇敢一点，想见的人就去见。”",
            "“少一点内耗，多一点去感受。”",
        ],
        "comments": [
            "你不是机器，你是会发光的人（偶尔也会没电）。",
            "休息不是偷懒，是把自己充回 100%。",
            "喜欢这件事，晚一点也没关系，但别一直拖着。",
            "你很清醒：生活不是 KPI，快乐也不是绩效。",
        ],
        "tendency": ["life", "life", "romance", "life"],
    },
    {
        "id": "q2",
        "question": "哪种瞬间最容易让你觉得“啊，活着真好”？",
        "options": [
            "冬天热饮第一口，手心跟着暖起来 ☕",
            "在路上：地铁窗、夜风、街灯，刚好都顺眼 🌙",
            "运动后出汗的那一刻，身体很诚实 🏃",
            "跟重要的人一起吃饭，话不多也不尴尬 🍜",
        ],
        "comments": [
            "你对幸福的要求很克制，但很准确。",
            "你天生会把普通日子拍得像电影。",
            "你不是爱运动，你是爱运动后的轻松。",
            "这题的正确答案，是“有人在旁边”。",
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
            "你太懂了：把复杂的事讲清楚，真的很费心力。",
            "你这种“稳稳的可靠”，很容易让人安心。",
            "认真不是卷，是你对自己有要求。",
            "这句是成年人最高级的边界感：不被工作吞掉。",
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
            "会做饭的人自带“生活会变好”的滤镜。",
            "你会越来越会说“我需要什么”，这是成长。",
            "稳稳地走，比突然燃一把更厉害。",
            "你缺的不是远方，是一个出发的理由。",
        ],
        "tendency": ["life", "romance", "life", "life"],
    },
    {
        "id": "q5",
        "question": f"如果把 2026 送给 {TARGET_NAME} 一张“心愿券”，你更想写什么？",
        "options": [
            "“忙的时候也别忘了吃饭、喝水、睡觉。”",
            "“愿你被理解，也被偏爱；被照顾，也被尊重。”",
            "“我们一起把普通日子，过得更有趣一点。”",
            "“愿你工作顺利，心里也一直有光。”",
        ],
        "comments": [
            "你给出的不是大道理，是很具体的温柔。",
            "你在认真爱人：不控制，只祝福。",
            "喜欢这种提议：不宏大，但足够长久。",
            "你很会：把“盼你开心”说得不肉麻。",
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
            "很高级的浪漫：不轰轰烈烈，也不忽冷忽热。",
            "你要的是并肩，而不是捆绑。",
            "你喜欢耐心的关系——慢慢来，更长久。",
            "你们会很有默契：懂彼此的幼稚，也懂彼此的成熟。",
        ],
        "tendency": ["romance", "romance", "romance", "all"],
    },
]

# ============ 数据：关卡二（抽签）===========
career_signs = [
    {
        "level": "上上签 · 稳稳拿捏",
        "text": f"{TARGET_NAME} 今年会遇到更懂配合的同事与更清晰的节奏。\n辛苦被看见，努力有回响。\n加班会少一点点，但成就感会多很多。",
    },
    {
        "level": "上签 · 体面推进",
        "text": "很多事不需要“硬扛”，会有人愿意一起把它做完。\n你会更擅长说“不”，也更擅长保护自己的时间。",
    },
    {
        "level": "吉签 · 忙而不乱",
        "text": "项目会多一点，会议也会多一点。\n但你会更会取舍：把精力花在值得的人和事上。",
    },
    {
        "level": "妙签 · 换个角度就顺了",
        "text": "今年的好运来自“沟通”两个字。\n把话说清楚，把边界立起来，事情就会更顺。",
    },
    {
        "level": "温柔签 · 别忘了你自己",
        "text": "工作会占据生活一部分，但不该占据全部。\n你会学会休息——然后更有力气发光。",
    },
]

life_signs = [
    {
        "level": "上上签 · 日子会更甜",
        "text": "你会拥有更多“刚刚好”的小确幸：好吃的晚饭、好看的天空、好听的歌。\n生活不需要很大声，也能很动人。",
    },
    {
        "level": "上签 · 身心都轻一点",
        "text": "睡眠会变好，运动会更规律。\n你会慢慢把自己照顾得更好",
    },
    {
        "level": "福签 · 出门见世界",
        "text": "今年适合小旅行：城市漫步、短途看海、周末去山里。\n不必远，只要出发。",
    },
    {
        "level": "妙签 · 热爱回归",
        "text": "你会捡回一个搁置已久的爱好：拍照、做饭、读书、看展、滑雪……\n它会在你疲惫时托住你。",
    },
    {
        "level": "玄学签 · 好运从整理开始",
        "text": "收拾房间、清空相册、换一条床单。\n你会发现：当你把生活理顺，运气也会跟着顺。",
    },
]

romance_signs = [
    {
        "level": "上上签 · 心动有回声",
        "text": f"{TARGET_NAME} 会被更好地理解与偏爱。\n那些不说出口的小情绪，也会有人温柔接住。",
    },
    {
        "level": "上签 · 默契升级",
        "text": "你们会更懂彼此：一个眼神就知道在想什么。\n争执会更少，拥抱会更多。",
    },
    {
        "level": "喜签 · 小浪漫更耐久",
        "text": "不是烟花式的轰动，而是日常里的用心：\n记得你喜欢的口味，留一盏晚归的灯。",
    },
    {
        "level": "实在签 · 认真生活就是浪漫",
        "text": "真正的浪漫，是在忙碌里还愿意为对方腾出时间。\n是说“我在”，也是做到“我在”。",
    },
    {
        "level": "温柔签 · 你值得被爱",
        "text": "今年请多接纳自己一点。\n当你更喜欢自己，你也会更容易遇到喜欢你的人。",
    },
]

category_names = {"career": "💼 职场节奏签", "life": "🍃 生活状态签", "romance": "💌 心动默契签"}


# ============ 顶部标题 ============
st.markdown('<div class="main-title">辞岁 小结 · 新年 好运</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="sub-title">这不是考核，也不需要完美。<br>这是一个送给 <b>{TARGET_NAME}</b> 的小冒险，你也可以顺便把自己抱一抱。</div>',
    unsafe_allow_html=True,
)
st.markdown("---")
render_progress()
st.markdown("")


# ============ Stage 1：年度灵魂拷问 ============
if st.session_state.stage == 1:
    st.markdown("## 📝 第一关：年度灵魂拷问")
    st.caption(f"问几句不尖锐的真话，留一点不张扬的温柔给 {TARGET_NAME}。")
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
            st.info(f"📋 已完成 {len(st.session_state.quiz_answers)}/{len(questions)} 题，全部答完即可进入下一关")

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
        st.caption(f"三支签：给 {TARGET_NAME} 的职场节奏、生活状态、心动默契。慢慢点，抽到哪支都算数。")
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
            st.success("✅ 第二关完成！接下来生成专属祝福。")
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
        st.caption(f"把这段话留给 {TARGET_NAME}；也把最后一点温柔留给你们自己。")
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
            "career": "💼 把节奏掌握好的人",
            "life": "🍃 认真把日子过好的人",
            "romance": "💌 心很柔软、也很坚定的人",
            "all": "🌟 稳稳发光的人",
        }
        tendency_blessings = {
            "career": f"""
<div class="blessing-text">
<b>{TARGET_NAME}</b>，始终如一的你：<br><br>
时光微澜，你在复杂与纷扰中，将一切打理得安稳妥帖。你的坚持与温柔，如同“采菊东篱下，悠然见南山”的清澈宁静。<br><br>
2026 年，愿你：<br>
- 在忙碌间也能抽空照顾好自己，三餐有滋味，夜眠有安稳<br>
- 学会温柔设界，为自己多一点松弛与自在<br>
- 你的努力有人懂，你的小小苦恼，也被用心呵护<br>
- 在四季流转里，有人与共，也能独自从容<br><br>
请记得：山高路远，总有人为你点灯，也欢迎你偶尔停下来依靠。
</div>
<div class="blessing-wish">愿你脚步从容，内心有光，前路有人同行，烦恼有人听——如诗中所言：“山一程，水一程，身向远方心自安。”</div>
""",
            "life": f"""
<div class="blessing-text">
<b>{TARGET_NAME}</b>，细心生活的你：<br><br>
新的一年，愿你于日常琐碎中，也能拾到小小欢喜。一茶一饭，一窗光影，都成为温暖时光。<br>
“人间烟火气，最抚凡人心。”<br><br>
愿你：<br>
- 让生活不止是清单，更是一场悠然的旅行<br>
- 在自我关照里，懂得温柔与自己和解<br>
- 热爱能被持久地点亮，疲惫时有人给你靠岸<br>
- 无论晴雨，都有人为你撑伞，有风景共赏<br><br>
日子可以细水流长，也会悄然生花。
</div>
<div class="blessing-wish">愿你清风徐来，温柔常在——“岁月悠悠，且以温柔共赴。”</div>
""",
            "romance": f"""
<div class="blessing-text">
<b>{TARGET_NAME}</b>，温柔且坚定的你：<br><br>
你用心经营每一份情感，善于聆听，也懂得回应。你的温柔，像“云中谁寄锦书来”的惦念，微小却长久。<br><br>
2026 年，愿你：<br>
- 所思有人懂，所爱有回响<br>
- 每一次心动，都被认真安放，每句未说的话，都有人细细领会<br>
- 忙碌生活中，依旧能保留爱的仪式感<br>
- 在独处时自得其乐，在相对时彼此照亮<br><br>
浪漫无需张扬，用心生活便已动人。
</div>
<div class="blessing-wish">愿你所感所盼，都能温柔落地；“人间烟火处，有你也有我。”</div>
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
    🎊 新年快乐，{TARGET_NAME}！🎊
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
  div[style*="font-size:1.1rem"] {{
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
                st.info("💡 可以直接截屏保存这一页，发给 TA 就好。")

