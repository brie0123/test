import streamlit as st
import pymysql

conn,cur = None, None
data1, data2, data3, data4 = "","","",""
sql = ""

name = st.text_input("이름")
button = st.button('저장')

if button:
    conn = pymysql.connect(host='localhost', user='root', password='apple123!!',db='test',charset='utf-8')
    cur = conn.cursor()
    st.write(name)
    
    cur.execute(f'INSERT INTO test VALUSE(3, "{name}")')
    
    conn.commint()
    conn.close()
    
    st.write(':blue저장되었습니다. :sparkles:')