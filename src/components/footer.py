#src/component/footer.py
import streamlit as st


def footer_home():
    logo_url="https://i.ibb.co/4r5X1FY/apnacollege.png"
    st.markdown(f"""
    <div style="margin-top: 0.5rem; display:flex; gap: 6px; justify-content:center; items-align: center">
        <p style="font-weight:bold; color:white; opacity:0.8;">Created with ❤️</p>
        
    </div>
    """,unsafe_allow_html=True)
