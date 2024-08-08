import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image
from io import BytesIO
import base64

# Set page config at the very beginning of your script
st.set_page_config(page_title="CMDSPACE", page_icon="🏛️", layout="wide")

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

# Custom CSS for Apple-style UI with full-width layout
# 스타일을 수정하거나 새로운 클래스를 추가하려면 이 부분을 편집하세요
apple_style_css = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #f5f5f7;
        color: #1d1d1f;
    }
    .stApp {
        padding: 2rem;
    }
    .main-content {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
    }
    h2 {
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .stButton > button {
        background-color: #0071e3;
        color: white;
        font-size: 1rem;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #0077ed;
    }
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 1px solid #d2d2d7;
        padding: 0.5rem;
        font-size: 1rem;
    }
    @media (max-width: 768px) {
        .stApp {
            padding: 1rem;
        }
        h1 {
            font-size: 2rem;
        }
        h2 {
            font-size: 1.5rem;
        }
    }
        /* Your existing CSS styles here */

    /* Custom styles for option menu */
    .nav-link {
        font-size: 1.2rem !important;
        padding: 0.5rem 1rem !important;
    }
    .nav-link.active {
        background-color: #0071e3 !important;
        color: white !important;
        font-weight: bold !important;
    }
</style>
"""

# Helper functions
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

# Pages
# 각 페이지 함수는 해당 페이지의 내용을 정의합니다
# 새로운 페이지를 추가하려면 아래 형식을 따라 새로운 함수를 만드세요

def home_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("커맨드스페이스 AI 서비스")
    st.markdown("""
    ## 환영합니다
    
    이 앱은 구요한 교수가 제공하는 지식관리 및 생성형 AI 활용 서비스입니다.
    """)
    st.image(CONFIG["home_page_image"], use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def openai_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("OpenAI 도구")
    selected_model = st.selectbox("OpenAI 모델 선택", list(CONFIG["openai_models"].keys()))
    st.write(f"모델 설명: {CONFIG['openai_models'][selected_model]}")
    prompt = st.text_area("프롬프트 입력:", height=200)
    if st.button("텍스트 생성"):
        if prompt:
            # OpenAI API 호출 로직 구현
            # TODO: OpenAI API 연동 코드 추가
            st.write("생성된 텍스트:")
            st.write("여기에 생성된 텍스트가 표시됩니다.")
        else:
            st.warning("프롬프트를 입력해주세요.")
    st.markdown('</div>', unsafe_allow_html=True)

def deepl_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("DeepL 번역")
    text = st.text_area("번역할 텍스트 입력:", height=200)
    target_lang = st.selectbox("대상 언어 선택:", CONFIG["target_languages"])
    if st.button("번역"):
        if text:
            # DeepL API 호출 로직 구현
            # TODO: DeepL API 연동 코드 추가
            st.write("번역된 텍스트:")
            st.write("여기에 번역된 텍스트가 표시됩니다.")
        else:
            st.warning("번역할 텍스트를 입력해주세요.")
    st.markdown('</div>', unsafe_allow_html=True)

def voc_analysis_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("고객의 소리(VOC) 분석")
    voc_data = st.text_area("VOC 데이터 입력:", height=300)
    if st.button("분석"):
        if voc_data:
            # VOC 분석 로직 구현
            # TODO: VOC 분석 알고리즘 구현
            st.subheader("분석 결과:")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 주요 문제점")
                st.write("1. 문제점 1")
                st.write("2. 문제점 2")
            with col2:
                st.markdown("### 개선 방안")
                st.write("1. 개선 방안 1")
                st.write("2. 개선 방안 2")
        else:
            st.warning("VOC 데이터를 입력해주세요.")
    st.markdown('</div>', unsafe_allow_html=True)

def contact_page():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

# 새로운 페이지를 추가하려면 아래와 같은 형식의 함수를 만드세요:
#"""
#def new_page():
#    st.markdown('<div class="main-content">', unsafe_allow_html=True)
#    st.title("새로운 페이지 제목")
#    # 페이지 내용 구현
#    st.markdown('</div>', unsafe_allow_html=True)
#"""

# Main app
def main():
    st.markdown(apple_style_css, unsafe_allow_html=True)

    # Sidebar navigation using streamlit_option_menu
    with st.sidebar:
        st.title("CMDSPACE")
        selected = option_menu(
            menu_title=None,
            options=["홈", "OpenAI", "DeepL", "VOC 분석", "연락처"],
            icons=['house', 'cloud', 'translate', 'chat-square-text', 'person-lines-fill'],
            menu_icon="cast",
            default_index=0,
        )

    # Page routing
    if selected == "홈":
        home_page()
    elif selected == "OpenAI":
        openai_page()
    elif selected == "DeepL":
        deepl_page()
    elif selected == "VOC 분석":
        voc_analysis_page()
    elif selected == "연락처":
        contact_page()

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2024 CMDSPACE by Yohan Koo")

if __name__ == "__main__":
    main()
