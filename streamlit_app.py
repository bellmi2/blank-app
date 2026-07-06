import streamlit as st

st.set_page_config(page_title="Streamlit 요소 데모", page_icon="✨", layout="wide")

st.title("🎉 Streamlit 요소 데모")
st.caption("이 페이지는 자주 쓰는 Streamlit 위젯과 레이아웃 요소를 한 번에 보여줍니다.")

with st.sidebar:
    st.header("사이드바")
    name = st.text_input("이름", value="홍길동")
    theme = st.selectbox("테마", ["라이트", "다크", "시스템"])
    notify = st.checkbox("알림 받기", value=True)

st.markdown("## 기본 텍스트")
st.header("헤더")
st.subheader("서브헤더")
st.text("이것은 일반 텍스트입니다.")
st.code("print('Hello, Streamlit!')", language="python")

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader("입력 폼")
    message = st.text_area("메모", placeholder="여기에 내용을 입력해보세요.", height=120)
    age = st.number_input("나이", min_value=0, max_value=120, value=25)
    st.info(f"이름: {name} / 나이: {age}")

with col2:
    st.subheader("선택 위젯")
    animal = st.radio("좋아하는 동물", ["강아지", "고양이", "토끼"])
    tools = st.multiselect("사용할 도구", ["Python", "Streamlit", "Pandas", "Plotly"])
    st.success(f"선택한 동물: {animal}")
    st.write("선택한 도구:", tools)

st.divider()

st.subheader("슬라이더와 버튼")
score = st.slider("완성도", 0, 100, 75)
if st.button("버튼 클릭"):
    st.balloons()
    st.toast("버튼을 눌렀습니다!")

st.progress(score / 100)
st.metric("현재 점수", f"{score}점", "상승")

with st.expander("추가 정보"):
    st.write("이 예제는 여러 가지 Streamlit 요소를 한 화면에서 확인할 수 있도록 구성했습니다.")

tab1, tab2 = st.tabs(["소개", "샘플 데이터"])
with tab1:
    st.write("Streamlit은 데이터 앱을 빠르게 만들 수 있는 Python 라이브러리입니다.")
with tab2:
    sample_data = [
        {"이름": "Alice", "점수": 90},
        {"이름": "Bob", "점수": 85},
        {"이름": "Charlie", "점수": 92},
    ]
    st.dataframe(sample_data)
