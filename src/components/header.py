#src/component/header.py
import streamlit as st


def header_home():
    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
    <div style='display:flex; flex-direction:column; align-item:center; justify-content:center; margin-bottom:2px; margin-top:10px;'>
        <img src='{logo_url}' style='height:65px; margin-bottom: 4px;';/>
        <h1 style='text-align:center; color:#E0E3FF; margin-top:0px; width:100%;'>SNAP<br/><span style='margin-left:0.45em; display:inline-block;'> CLASS</span></h1>
    </div>
    """,unsafe_allow_html=True)
