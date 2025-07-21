import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.title("🎈 My new app")  # 페이지 제목

st.header("헤더 예시")  # 큰 제목

st.subheader("서브헤더 예시")  # 작은 제목

st.text("텍스트 예시입니다.")  # 일반 텍스트

st.markdown("**마크다운 텍스트**: *이탤릭*, [링크](https://streamlit.io)")  # 마크다운 지원

st.code("print('Hello, Streamlit!')", language='python')  # 코드 블록

st.latex(r"\int_0^1 x^2 dx")  # LaTeX 수식

st.write("write 함수는 다양한 타입을 자동으로 렌더링합니다.")  # write 함수

st.divider()  # 구분선

st.button("버튼 예시")  # 버튼

st.checkbox("체크박스 예시")  # 체크박스

st.radio("라디오 버튼 예시", ["옵션 1", "옵션 2"])  # 라디오 버튼

st.selectbox("셀렉트박스 예시", ["A", "B", "C"])  # 셀렉트박스

st.multiselect("멀티셀렉트 예시", ["X", "Y", "Z"])  # 멀티셀렉트

st.slider("슬라이더 예시", 0, 100, 50)  # 슬라이더

st.number_input("숫자 입력 예시", min_value=0, max_value=10, value=5)  # 숫자 입력

st.text_input("텍스트 입력 예시")  # 텍스트 입력

st.text_area("텍스트 영역 예시")  # 텍스트 영역

st.date_input("날짜 입력 예시")  # 날짜 입력

st.time_input("시간 입력 예시")  # 시간 입력

st.file_uploader("파일 업로드 예시")  # 파일 업로더

st.image("https://static.streamlit.io/examples/dog.jpg", caption="이미지 예시")  # 이미지

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오

st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오

st.progress(70)  # 진행률 표시줄

st.metric(label="온도", value="25°C", delta="+2°C")  # 메트릭(지표)

st.success("성공 메시지 예시")  # 성공 메시지

st.info("정보 메시지 예시")  # 정보 메시지

st.warning("경고 메시지 예시")  # 경고 메시지

st.error("에러 메시지 예시")  # 에러 메시지

import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)  # 데이터프레임 표시

st.table(df)  # 테이블 표시

import numpy as np
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)  # 라인 차트

st.bar_chart(chart_data)  # 바 차트

st.area_chart(chart_data)  # 영역 차트

st.map(pd.DataFrame({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.4, -122.41, -122.42]
}))  # 지도 표시