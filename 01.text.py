import streamlit as st

st.title('hello')

st.title('별: :star2:')

st.header('헤더를 입력할 수 있어요 :sparkles:')

st.subheader('this is subheader :sunglasses:')

st.caption('and this is caption')

sample_code = """
def function():
print('안녕하세요')
"""

st.code(sample_code, language='python')



st.text('일반 텍스트')

st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
st.markdown('텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파랑색]** 볼드체로 설정할 수 있습니다.])')
st.markdown(':green[$\sqrt{x^2+y^2}=1$]와 같이 latex 문법의 수식 표현도 가능합니다. :pencil:')

st.latex('\sqrt{x^2+y^2}=1')