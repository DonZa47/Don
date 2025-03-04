import streamlit as st
import pandas as pd

st.title("🐷🐷🐷Website Developing using Python🐷🐷")
st.header("🍖🍖Website Developing using Python🍖🍖")

st.image('./img/pic.jpg')
st.subheader("ธนดล จันทวงค์")
col1,col2,col3 = st.columns(3)
with col1:
    st.header("tuilpa")
    st.image("./img/fo1.jpg")

with col2:
    st.header("Helianthus annuus")
    st.image("./img/fo2.jpg")

with col3:
    st.header("Myostis")
    st.image("./img/fo3.jpg")
    
html_7 = """
<div style="background-color:#12c29e;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
dt = pd.read_csv("./data/iris-3.csv")
st.write(dt.head(10))
st.subheader("ข้อมูลส่วนสุดท้าย 10 แถว")
st.write(dt.tail(10))

dt1 =dt['petallength'].sum()
dt2 =dt['petalwidth'].sum()
dt3 =dt['sepallength'].sum()
dt4 =dt['sepalwidth'].sum()

dx = [dt1,dt2,dt3,dt4]
dx2 = pd.DataFrame(dx, index=["d1","d2","d3","d4"])

if st.button("แสดงการจินตทัศน์ข้อมูล"):
    st.bar_chart(dx2)
    st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_8 = """
<div style="background-color:#12c29e;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

pt_len = st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd = st.slider("กรุราเลือกข้อมูล petal.width")

sp_len = st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd = st.number_input("กรุณาเลือกข้อมูล sepal width")