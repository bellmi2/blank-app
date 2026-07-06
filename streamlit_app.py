import random
import streamlit as st

st.set_page_config(page_title="영어 단어 게임", page_icon="🧠", layout="wide")

st.title("🇬🇧 영어 단어 게임")
st.caption("상단 중앙의 영어 단어를 보고 한글 뜻을 입력해보세요.")

word_data = {
    "apple": "사과",
    "library": "도서관",
    "travel": "여행",
    "friend": "친구",
    "study": "공부",
    "happy": "행복한",
    "weather": "날씨",
    "music": "음악",
    "family": "가족",
    "coffee": "커피",
}

if "words" not in st.session_state:
    items = list(word_data.items())
    random.shuffle(items)
    st.session_state.words = items
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.session_state.feedback = ""
    st.session_state.completed = False

if st.session_state.index >= len(st.session_state.words):
    st.session_state.completed = True

def check_answer(user_answer: str) -> None:
    if st.session_state.completed:
        return

    english, korean = st.session_state.words[st.session_state.index]
    st.session_state.attempts += 1
    normalized_input = user_answer.strip().replace(" ", "")
    normalized_answer = korean.replace(" ", "")

    if normalized_input == normalized_answer:
        st.session_state.score += 1
        st.session_state.feedback = f"✅ 정답이에요! '{english}'는 '{korean}'입니다."
    else:
        st.session_state.feedback = f"❌ 틀렸어요. 정답은 '{korean}'입니다."

    st.session_state.index += 1
    if st.session_state.index >= len(st.session_state.words):
        st.session_state.completed = True

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        f"<div style='text-align:center; font-size:4rem; font-weight:700; margin: 20px 0;'>{st.session_state.words[st.session_state.index][0] if not st.session_state.completed else '게임 완료!'}</div>",
        unsafe_allow_html=True,
    )

st.divider()

with st.expander("게임 설명", expanded=True):
    st.write(
        "- 영어 단어를 보고 한글 뜻을 맞춰보세요.\n"
        "- 맞을 때마다 점수가 올라갑니다.\n"
        "- 전체 단어를 모두 맞추면 게임이 완료됩니다."
    )

if st.session_state.completed:
    st.success("🎉 모든 단어를 완료했습니다!")
    st.balloons()
    st.write(f"전체 시도: {st.session_state.attempts}회")
    st.write(f"맞힌 단어: {st.session_state.score}개 / {len(st.session_state.words)}개")
    if st.button("다시 시작하기"):
        items = list(word_data.items())
        random.shuffle(items)
        st.session_state.words = items
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.attempts = 0
        st.session_state.feedback = ""
        st.session_state.completed = False
else:
    with st.form(key="guess_form"):
        user_answer = st.text_input("한글 뜻을 입력하세요", value="", placeholder="예: 사과")
        submitted = st.form_submit_button("정답 확인")

    if submitted:
        check_answer(user_answer)

    if st.session_state.feedback:
        st.info(st.session_state.feedback)

    st.write(f"진행: {st.session_state.index + 1} / {len(st.session_state.words)}")
    st.progress((st.session_state.index) / len(st.session_state.words))
    st.write(f"현재 점수: {st.session_state.score}")

st.divider()

with st.sidebar:
    st.header("게임 정보")
    st.write("- 문제 수: 10")
    st.write("- 맞힌 개수: ", st.session_state.score)
    st.write("- 시도 횟수: ", st.session_state.attempts)
    st.write("- 다음 단어를 맞혀보세요!")
