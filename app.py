import uuid
from pathlib import Path

import streamlit as st

from graph.graph_builder import workflow


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

LOGO_PATH = BASE_DIR / "assets" / "logo.jpeg"


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Aevora",
    page_icon=str(LOGO_PATH),
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
       ====================================================== */

    .stApp {
        background-color: #000000;
        color: #ffffff;
    }

    html,
    body,
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
    }

    header[data-testid="stHeader"] {
        background-color: #000000;
    }

    footer {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }


    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 1px solid #1c1c1c;
    }


    /* ======================================================
       SIDEBAR BUTTONS
       ====================================================== */

    div.stButton > button {

        background-color: #000000;

        color: #d7d7d7;

        border: 1px solid #202020;

        border-radius: 10px;

        min-height: 40px;

        transition: all 0.2s ease;
    }


    div.stButton > button:hover {

        background-color: #151515;

        color: #ffffff;

        border-color: #3a3a3a;
    }


    /* ======================================================
       MAIN WELCOME
       ====================================================== */

    .welcome-title {

        text-align: center;

        color: #ffffff;

        font-size: 40px;

        font-weight: 700;

        letter-spacing: -1px;

        margin-top: 15px;
    }


    .welcome-subtitle {

        text-align: center;

        color: #626262;

        font-size: 14px;

        margin-top: 8px;

        margin-bottom: 35px;
    }


    /* ======================================================
       AI PANEL
       ====================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {

        background-color: #050505 !important;

        border: 1px solid #242424 !important;

        border-radius: 20px !important;

        box-shadow:
            0 20px 70px rgba(0, 0, 0, 0.8) !important;
    }


    /* ======================================================
       PANEL TITLE
       ====================================================== */

    .panel-title {

        color: #ffffff;

        font-size: 20px;

        font-weight: 650;

        margin-top: 5px;
    }


    .panel-subtitle {

        color: #666666;

        font-size: 12px;

        margin-top: 4px;
    }


    /* ======================================================
       STATUS
       ====================================================== */

    .status {

        color: #777777;

        font-size: 11px;

        margin-top: 15px;

        margin-bottom: 15px;
    }


    /* ======================================================
       CHAT MESSAGES
       ====================================================== */

    div[data-testid="stChatMessage"] {

        background-color: transparent !important;

        border: none !important;

        padding-left: 4px;

        padding-right: 4px;

        margin-bottom: 8px;
    }


    /* ======================================================
       CHAT INPUT
       ====================================================== */

    div[data-testid="stChatInput"] {

        background-color: transparent !important;

        border-top: none !important;

        padding-top: 10px;
    }


    div[data-testid="stChatInput"] > div {

        background-color: #0c0c0c !important;

        border: 1px solid #282828 !important;

        border-radius: 15px !important;

        box-shadow: none !important;
    }


    div[data-testid="stChatInput"] textarea {

        background-color: transparent !important;

        color: #ffffff !important;

        font-size: 13px !important;
    }


    div[data-testid="stChatInput"] textarea::placeholder {

        color: #555555 !important;
    }


    div[data-testid="stChatInput"] textarea:focus {

        border-color: #414141 !important;
    }


    /* ======================================================
       DIVIDER
       ====================================================== */

    hr {

        border-color: #1b1b1b !important;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    .footer {

        text-align: center;

        color: #3f3f3f;

        font-size: 9px;

        margin-top: 15px;
    }


    /* ======================================================
       ACTIVE CHAT TITLE
       ====================================================== */

    .chat-title {

        color: #ffffff;

        font-size: 21px;

        font-weight: 600;

        margin-top: 15px;

        margin-bottom: 4px;
    }


    .chat-caption {

        color: #555555;

        font-size: 11px;

        margin-bottom: 15px;
    }


    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "chat_sessions" not in st.session_state:

    st.session_state.chat_sessions = {}


# ============================================================
# CREATE FIRST CHAT
# ============================================================

if "current_chat_id" not in st.session_state:

    first_chat_id = str(uuid.uuid4())

    st.session_state.chat_sessions[first_chat_id] = {

        "thread_id": first_chat_id,

        "title": "New Chat",

        "messages": []
    }

    st.session_state.current_chat_id = first_chat_id


# ============================================================
# CURRENT CHAT
# ============================================================

current_chat_id = st.session_state.current_chat_id

current_chat = st.session_state.chat_sessions[
    current_chat_id
]

current_thread_id = current_chat["thread_id"]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # --------------------------------------------------------
    # BRAND
    # --------------------------------------------------------

    st.markdown(
        "## Aevora"
    )

    st.caption(
        "LangGraph AI Assistant"
    )

    st.divider()


    # --------------------------------------------------------
    # NEW CHAT
    # --------------------------------------------------------

    if st.button(
        "＋  New Chat",
        use_container_width=True
    ):

        new_chat_id = str(uuid.uuid4())

        st.session_state.chat_sessions[
            new_chat_id
        ] = {

            "thread_id": new_chat_id,

            "title": "New Chat",

            "messages": []
        }

        st.session_state.current_chat_id = new_chat_id

        st.rerun()


    st.write("")


    # --------------------------------------------------------
    # CONVERSATIONS
    # --------------------------------------------------------

    st.caption(
        "RECENT CONVERSATIONS"
    )


    for chat_id, chat in (
        st.session_state.chat_sessions.items()
    ):

        if st.button(
            chat["title"],
            key=f"chat_{chat_id}",
            use_container_width=True
        ):

            st.session_state.current_chat_id = chat_id

            st.rerun()


# ============================================================
# MAIN LAYOUT
# ============================================================

main_column, ai_column = st.columns(
    [2.15, 1],
    gap="large"
)


# ============================================================
# MAIN WORKSPACE
# ============================================================

with main_column:

    # ========================================================
    # EMPTY CHAT
    # ========================================================

    if len(current_chat["messages"]) == 0:

        st.write("")
        st.write("")
        st.write("")
        st.write("")


        # ----------------------------------------------------
        # LARGE CENTER LOGO
        # ----------------------------------------------------

        logo_col1, logo_col2, logo_col3 = st.columns(
            [1, 2, 1]
        )

        with logo_col2:

            st.image(
                str(LOGO_PATH),
                width=460
            )


        # ----------------------------------------------------
        # WELCOME
        # ----------------------------------------------------

        st.markdown(
            '<div class="welcome-title">'
            'How can I help you?'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="welcome-subtitle">'
            'Ask anything, explore ideas, write code, '
            'or learn something new.'
            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # ACTIVE CHAT
    # ========================================================

    else:

        st.markdown(
            '<div class="chat-title">'
            + current_chat["title"]
            + '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="chat-caption">'
            'LangGraph conversation'
            '</div>',
            unsafe_allow_html=True
        )


        st.divider()


        # ----------------------------------------------------
        # DISPLAY CHAT
        # ----------------------------------------------------

        for message in current_chat["messages"]:

            with st.chat_message(
                message["role"]
            ):

                st.markdown(
                    message["content"]
                )


# ============================================================
# AI ASSISTANT PANEL
# ============================================================

with ai_column:

    with st.container(
        border=True
    ):

        # ----------------------------------------------------
        # PANEL LOGO
        # ----------------------------------------------------

        panel_logo_col1, panel_logo_col2, panel_logo_col3 = (
            st.columns([1, 2, 1])
        )


        with panel_logo_col2:

            st.image(
                str(LOGO_PATH),
                width=140
            )


        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        st.markdown(
            '<div class="panel-title">'
            'How can I help you today?'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="panel-subtitle">'
            'Your intelligent AI assistant'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="status">'
            '● AI Assistant Online'
            '</div>',
            unsafe_allow_html=True
        )


        st.divider()


        # ----------------------------------------------------
        # QUICK ACTIONS
        # ----------------------------------------------------

        st.caption(
            "QUICK ACTIONS"
        )


        # ----------------------------------------------------
        # LEARN
        # ----------------------------------------------------

        if st.button(
            "✦  Learn something",
            use_container_width=True,
            key="quick_learn"
        ):

            st.session_state.quick_prompt = (
                "Explain a complex concept "
                "from first principles."
            )

            st.rerun()


        # ----------------------------------------------------
        # CODE
        # ----------------------------------------------------

        if st.button(
            "⌘  Help me write code",
            use_container_width=True,
            key="quick_code"
        ):

            st.session_state.quick_prompt = (
                "Help me understand and improve "
                "my Python code."
            )

            st.rerun()


        # ----------------------------------------------------
        # ANALYZE
        # ----------------------------------------------------

        if st.button(
            "⌁  Analyze a problem",
            use_container_width=True,
            key="quick_analyze"
        ):

            st.session_state.quick_prompt = (
                "Break down a problem and "
                "explain the reasoning step by step."
            )

            st.rerun()


        # ----------------------------------------------------
        # EXPLORE AI
        # ----------------------------------------------------

        if st.button(
            "◎  Explore AI",
            use_container_width=True,
            key="quick_ai"
        ):

            st.session_state.quick_prompt = (
                "Explain how LangGraph works "
                "with a practical example."
            )

            st.rerun()


        st.divider()


        # ----------------------------------------------------
        # CURRENT CONVERSATION
        # ----------------------------------------------------

        st.caption(
            "CURRENT CONVERSATION"
        )


        st.write(
            current_chat["title"]
        )


        st.caption(
            "Thread ID"
        )


        st.code(
            current_thread_id,
            language=None
        )


        # ----------------------------------------------------
        # FOOTER
        # ----------------------------------------------------

        st.markdown(
            '<div class="footer">'
            'LangGraph · Hugging Face · Streamlit'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# QUICK PROMPT
# ============================================================

quick_prompt = st.session_state.pop(
    "quick_prompt",
    None
)


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Ask Aevora anything..."
)


# ============================================================
# QUICK ACTION INPUT
# ============================================================

if quick_prompt:

    user_input = quick_prompt


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if user_input:

    # --------------------------------------------------------
    # CREATE CHAT TITLE
    # --------------------------------------------------------

    if current_chat["title"] == "New Chat":

        current_chat["title"] = (
            user_input[:32]
            + (
                "..."
                if len(user_input) > 32
                else ""
            )
        )


    # --------------------------------------------------------
    # SAVE USER MESSAGE
    # --------------------------------------------------------

    current_chat["messages"].append(
        {
            "role": "user",

            "content": user_input
        }
    )


    # --------------------------------------------------------
    # LANGGRAPH CONFIG
    # --------------------------------------------------------

    config = {

        "configurable": {

            "thread_id": current_thread_id
        }
    }


    # --------------------------------------------------------
    # INVOKE LANGGRAPH
    # --------------------------------------------------------

    result = workflow.invoke(
        {
            "message": user_input
        },
        config=config
    )


    # --------------------------------------------------------
    # GET AI RESPONSE
    # --------------------------------------------------------

    ai_response = result["response"]


    # --------------------------------------------------------
    # SAVE AI RESPONSE
    # --------------------------------------------------------

    current_chat["messages"].append(
        {
            "role": "assistant",

            "content": ai_response
        }
    )


    # --------------------------------------------------------
    # REFRESH
    # --------------------------------------------------------

    st.rerun()