import streamlit as st
import pandas as pd
import numpy as np

st.title('데이터 프레임 튜토리얼')

# dataFrame 생성
dataframe = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second columns': [10,20,30,40]
})

st.dataframe(dataframe, use_container_width=False)
# 테이블 (static)
st.table(dataframe)

# 메트릭
st.metric(label='온도',value='10˚C',delta='1.2˚C')
st.metric(label='삼성전자',value='61,000 원',delta='-1,200 원')


# 칼럼 영역
col1, col2, col3 = st.columns(3)
col1.metric(label='달러USD', value='1,228', delta='-12.00원')
col2.metric(label='JPY(100엔)',value='958.63원',delta='-7.44원')
col3.metric(label='EURO',value='1,335.82원',delta='11.44원')