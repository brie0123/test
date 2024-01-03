import pandas as pd
import streamlit as st
from datetime import datetime as dt
import datetime


# 버튼
button = st.button('버튼을 눌러보세요')

if button:
    st.write(':blue[버튼]이 눌렸습니다. :sparkles:')
    
    
# 파일 다운로드 버튼
# 샘플 데이터 생성

dataframe = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

st.download_button(
    label='CSV로 다운로드',
    data=dataframe.to_csv(),
    file_name='sample.csv',
    mime='text/csv'
)


# 체크박스
agree = st.checkbox('동의 하십니까?')

if agree:
    st.write('동의 해주셔서 감사합니다 :100:')
    
# 라디오 선택 버튼
mbti = st.radio(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ','ENFP','선택지 없음')
)

if mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자]')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가]')
else:
    st.write('당신에 대해 :red[알고 싶어요]:grey_exclamation:')
    
# 슬라이더
values = st.slider(
    '범위의 값을 다음과 같이 지정',
    0.0,100.0,(25.0,75.0))
st.write('선택 범위:', values)


# start_time = st.slider(
#     '약속시간 잡기',
#     min_value=datetime[2020, 1, 1, 0, 0],
#     max_value=datetime[2020, 1, 7, 23, 0],
#     value=datetime[2020, 1, 3, 12, 0],
#     step=datetime.timedelta(hours=1),
#     format='MM/DD/YY - hh:mm'
# )

# st.write('선택한 약속 시간: ',start_time)



# # 텍스트 입력
# title = st.text_input(
#     label='do you have somewhere to travel in mind?',
#     placeholder='please input the place you want to visit'
# )
# st.write('the place you chose: :violet[{title}]')

# 숫자 입력
number = st.number_input(
    label = '나이를 입력해주세요',
    min_value=10,
    max_value=100,
    value=10,
    step=5'
)

st.write('당신이 입력하신 나이는:', number)