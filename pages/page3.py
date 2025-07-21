import streamlit as st
import pandas as pd

st.title("📊 학생별 과목 점수 비교 시각화")  # 페이지 제목

# 파일 업로드 위젯
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.success("파일 업로드 성공!")  # 성공 메시지

    # 데이터프레임 미리보기
    st.subheader("데이터 미리보기")
    st.dataframe(df)

    # 필요한 컬럼 확인
    required_columns = {'이름', '수학', '영어', '과학'}
    if required_columns.issubset(df.columns):
        st.subheader("학생별 과목 점수 비교")
        # 학생별로 수학, 영어, 과학 점수 시각화 (막대그래프)
        st.bar_chart(df.set_index('이름')[['수학', '영어', '과학']])
        st.info("학생별로 수학, 영어, 과학 점수를 막대그래프로 비교합니다.")  # 안내 메시지

        st.subheader("과목별 학생 점수 비교")
        # 과목별로 학생 점수 시각화 (라인차트)
        for subject in ['수학', '영어', '과학']:
            st.line_chart(df.set_index('이름')[subject], use_container_width=True)
            st.caption(f"{subject} 점수의 학생별 비교 (라인차트)")  # 각 과목별 설명
    else:
        st.error("필요한 컬럼(이름, 수학, 영어, 과학)이 모두 포함된 파일을 업로드하세요.")  # 에러 메시지
else:
    st.info("CSV 파일을 업로드하면 학생별, 과목별 점수를 비교할 수 있습니다.")  #