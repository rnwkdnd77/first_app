import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# NanumGothic 폰트 파일 경로 지정
font_path = "./fonts/NanumGothic-Regular.ttf"
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'  # NanumGothic 폰트 사용
plt.rcParams['axes.unicode_minus'] = False   # 마이너스 깨짐 방지

st.title("📈 Matplotlib 데이터 시각화 예시")  # 페이지 제목

# 샘플 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='사인 곡선')  # 한글 라벨
ax.set_title('Matplotlib 그래프 예시 (한글 지원)', fontsize=16)  # 한글 제목
ax.set_xlabel('X축 (시간)', fontsize=12)  # 한글 X축
ax.set_ylabel('Y축 (값)', fontsize=12)    # 한글 Y축
ax.legend()

st.pyplot(fig)  # Streamlit에 그래프 표시

st.info("NanumGothic 폰트를 직접 불러와 한글이 정상적으로 표시됩니다.")  # 정보