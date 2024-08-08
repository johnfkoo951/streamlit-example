import streamlit as st

st.set_page_config(page_title="CMDSPACE", page_icon="🍎", layout="wide")

def main():
    # Sidebar navigation using selectbox
    page = st.sidebar.selectbox(
        "페이지 선택",
        ["홈", "OpenAI", "DeepL", "VOC 분석", "연락처"]
    )

    # Page routing
    if page == "홈":
        st.title("홈 페이지")
    elif page == "OpenAI":
        st.title("OpenAI 페이지")
    elif page == "DeepL":
        st.title("DeepL 페이지")
    elif page == "VOC 분석":
        st.title("VOC 분석 페이지")
    elif page == "연락처":
        st.title("연락처 페이지")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2024 CMDSPACE by Yohan Koo")

if __name__ == "__main__":
    main()
