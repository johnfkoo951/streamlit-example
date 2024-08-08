import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image
from io import BytesIO
import base64

# Set page config at the very beginning of your script
st.set_page_config(page_title="2주뒤에 뵙겠습니다", page_icon="🏛️", layout="wide")

# Constants and configurations
CONFIG = {
    "openai_models": {
        "gpt-3.5-turbo": "간단한 작업을 위한 빠르고 저렴한 모델",
        "gpt-4": "복잡한 작업을 위한 더 강력한 모델",
        "gpt-4-32k": "대규모 작업을 위한 확장된 컨텍스트 모델"
    },
    "target_languages": ["EN-US", "KO", "DE", "FR", "ES", "IT", "JA"],
    "home_page_image": "https://example.com/cmdspace_logo.png",
}

# Custom CSS for light/dark mode support
custom_css = """
<style>
    :root {
        --sidebar-bg: #ece7df;
        --main-bg: #f2eee9;
        --font-color: #71554e;
        --selected-color: #e99897;
        --hover-color: rgba(233, 152, 151, 0.2);
    }

    [data-theme="dark"] {
        --sidebar-bg: #100f0f;
        --main-bg: #1c1b1a;
        --font-color: #cfcec4;
        --selected-color: #f38ba8;
        --hover-color: rgba(243, 139, 168, 0.2);
    }

    .stApp {
        background-color: var(--main-bg);
        color: var(--font-color);
        transition: all 0.3s ease-in-out;
    }

    .stSidebar .sidebar-content {
        background-color: var(--sidebar-bg);
    }

    .main .block-container {
        background-color: var(--main-bg);
    }

    .nav-link {
        color: var(--font-color) !important;
        background-color: transparent;
    }

    .nav-link:hover {
        background-color: var(--hover-color) !important;
    }

    .nav-link.active {
        background-color: var(--selected-color) !important;
        color: var(--main-bg) !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: var(--font-color);
    }

    .stButton > button {
        background-color: var(--selected-color);
        color: var(--main-bg);
    }

    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextArea > div > div > textarea {
        background-color: var(--main-bg);
        color: var(--font-color);
        border-color: var(--font-color);
    }
</style>
"""

# Helper functions
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

# Pages
def home_page():
    st.title("커맨드스페이스 AI 서비스")
    st.markdown("""
    ## 환영합니다
    
    이 앱은 구요한 교수가 제공하는 지식관리 및 생성형 AI 활용 서비스입니다.
    """)
    st.image(CONFIG["home_page_image"], use_column_width=True)

def generative_ai_page(sub_option):
    st.title("Generative AI")
    if sub_option == "ChatGPT":
        st.write("ChatGPT 관련 내용을 여기에 추가하세요.")
    elif sub_option == "DALL-E":
        st.write("DALL-E 관련 내용을 여기에 추가하세요.")
    elif sub_option == "Midjourney":
        st.write("Midjourney 관련 내용을 여기에 추가하세요.")

def obsidian_page(sub_option):
    st.title("Obsidian")
    if sub_option == "기초":
        st.write("Obsidian 기초 사용법을 여기에 추가하세요.")
    elif sub_option == "플러그인":
        st.write("Obsidian 플러그인 관련 내용을 여기에 추가하세요.")
    elif sub_option == "활용 사례":
        st.write("Obsidian 활용 사례를 여기에 추가하세요.")

def research_page(sub_option):
    st.title("Research")
    if sub_option == "방법론":
        st.write("연구 방법론에 대한 내용을 여기에 추가하세요.")
    elif sub_option == "논문 작성":
        st.write("논문 작성 가이드를 여기에 추가하세요.")
    elif sub_option == "데이터 분석":
        st.write("연구 데이터 분석 방법을 여기에 추가하세요.")

def knowledge_management_page(sub_option):
    st.title("Knowledge Management")
    if sub_option == "개념 및 이론":
        st.write("지식 관리의 개념과 이론을 여기에 추가하세요.")
    elif sub_option == "도구 소개":
        st.write("지식 관리 도구 소개를 여기에 추가하세요.")
    elif sub_option == "실천 사례":
        st.write("지식 관리 실천 사례를 여기에 추가하세요.")

def cmds_lab_page(sub_option):
    st.title("CMDS Lab")
    if sub_option == "연구 주제":
        st.write("CMDS Lab의 주요 연구 주제를 여기에 추가하세요.")
    elif sub_option == "팀 소개":
        st.write("CMDS Lab 팀원 소개를 여기에 추가하세요.")
    elif sub_option == "발표자료":
        st.write("CMDS Lab의 주요 발표 자료를 여기에 추가하세요.")

def contact_page():
    st.title("연락처")
    st.write("구요한 교수에게 연락하실 수 있는 방법입니다:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### SNS")
        st.markdown("- [Twitter](https://twitter.com/YohanKoo)")
        st.markdown("- [LinkedIn](https://www.linkedin.com/in/johankoo)")
    with col2:
        st.markdown("### 기타")
        st.markdown("- 이메일: professor@example.com")
        st.markdown("- 전화: 010-1234-5678")

# Main app
def main():
    st.markdown(custom_css, unsafe_allow_html=True)

    # Detect the theme and set the appropriate data attribute
    if st.get_option("theme.base") == "light":
        st.markdown('<div data-theme="light">', unsafe_allow_html=True)
    else:
        st.markdown('<div data-theme="dark">', unsafe_allow_html=True)

    with st.sidebar:
        st.title("2주뒤에 뵙겠습니다")
        
        selected = option_menu(
            menu_title="CMDSPACE",
            options=["Home", "Generative AI", "Obsidian", "Research", "Knowledge Management", "CMDS Lab", "Contact"],
            icons=['house-door', 'robot', 'journal-text', 'search', 'diagram-3', 'laptop', 'envelope'],
            menu_icon="command",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "transparent"},
                "icon": {"color": "inherit", "font-size": "20px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
                "nav-link-selected": {"background-color": "transparent"},
            }
        )

    # Submenus
    if selected == "Generative AI":
        with st.sidebar:
            ai_option = option_menu(
                menu_title=None,
                options=["ChatGPT", "DALL-E", "Midjourney"],
                icons=['chat-dots', 'image', 'palette'],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "transparent"},
                    "icon": {"color": "inherit", "font-size": "16px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding": "5px 10px"},
                    "nav-link-selected": {"background-color": "transparent"},
                }
            )
        generative_ai_page(ai_option)
    elif selected == "Obsidian":
        with st.sidebar:
            obsidian_option = option_menu(
                menu_title=None,
                options=["기초", "플러그인", "활용 사례"],
                icons=['book', 'plug', 'lightbulb'],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "transparent"},
                    "icon": {"color": "inherit", "font-size": "16px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding": "5px 10px"},
                    "nav-link-selected": {"background-color": "transparent"},
                }
            )
        obsidian_page(obsidian_option)
    elif selected == "Research":
        with st.sidebar:
            research_option = option_menu(
                menu_title=None,
                options=["방법론", "논문 작성", "데이터 분석"],
                icons=['clipboard-data', 'file-text', 'graph-up'],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "transparent"},
                    "icon": {"color": "inherit", "font-size": "16px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding": "5px 10px"},
                    "nav-link-selected": {"background-color": "transparent"},
                }
            )
        research_page(research_option)
    elif selected == "Knowledge Management":
        with st.sidebar:
            km_option = option_menu(
                menu_title=None,
                options=["개념 및 이론", "도구 소개", "실천 사례"],
                icons=['book', 'tools', 'check-circle'],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "transparent"},
                    "icon": {"color": "inherit", "font-size": "16px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding": "5px 10px"},
                    "nav-link-selected": {"background-color": "transparent"},
                }
            )
        knowledge_management_page(km_option)
    elif selected == "CMDS Lab":
        with st.sidebar:
            lab_option = option_menu(
                menu_title=None,
                options=["연구 주제", "팀 소개", "발표자료"],
                icons=['clipboard', 'people', 'file-earmark-slides'],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "transparent"},
                    "icon": {"color": "inherit", "font-size": "16px"}, 
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "padding": "5px 10px"},
                    "nav-link-selected": {"background-color": "transparent"},
                }
            )
        cmds_lab_page(lab_option)
    elif selected == "Home":
        home_page()
    elif selected == "Contact":
        contact_page()

    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2024 CMDSPACE by Yohan Koo")

    # Close the theme div
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
