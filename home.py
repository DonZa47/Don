import streamlit as st
import pandas as pd

st.title("🐷🐷🐷Website Developing using Python🐷🐷")
st.header("🍖🍖Website Developing using Python🍖🍖")

st.image('./img/pic.jpg')
st.subheader("ธนดล จันทวงค์")
col1,col2,col3 = st.columns(3)
html_7 = """
<div style="background-color:#12c29e;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
dt = pd.read_csv("./data/iris-3.csv")
st.write(dt.head(10))

with col1:
    st.header("tuilpa")
    st.image("./img/fo1.jpg")

with col2:
    st.header("Helianthus annuus")
    st.image("./img/fo2.jpg")

with col3:
    st.header("Myostis")
    st.image("./img/fo3.jpg")