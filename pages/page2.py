import streamlit as st
import pandas as pd

st.title("📂 학생 성적 분석 및 시각화")  # 페이지 제목

# 파일 업로드 위젯
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.success("파일 업로드 성공!")  # 성공 메시지

    # 데이터프레임 미리보기
    st.subheader("데이터 미리보기")
    st.dataframe(df)

    # 학생별 과목 평균 계산 (이름, 수학, 영어, 과학 컬럼이 있다고 가정)
    required_columns = {'이름', '수학', '영어', '과학'}
    if required_columns.issubset(df.columns):
        # 과목 평균 계산
        df['평균'] = df[['수학', '영어', '과학']].mean(axis=1)

        st.subheader("학생별 과목 평균")
        st.bar_chart(df.set_index('이름')['평균'])  # 학생별 평균 시각화

        st.info("학생별 과목 평균을 막대그래프로 시각화합니다.")  # 안내 메시지
    else:
        st.error("필요한 컬럼(이름, 수학, 영어, 과학)이 모두 포함된 파일을 업로드하세요.")  # 에러 메시지
else:
    st.info("CSV 파일을 업로드하면 학생별 과목 평균을 볼 수 있습니다.")  #