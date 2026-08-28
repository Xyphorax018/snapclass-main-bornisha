#src/ui/base_layout.py
import streamlit as st

def style_background_home():

    st.markdown("""

    <style>
        .stApp{
            background: #5865F2 !important;
        }

        .stApp div[data-testid="stColumn"]{
            background-color: #E0E3FF !important;
            padding: 2rem 2.6rem !important;
            border-radius: 5rem /5rem !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
            min-height: 260px !important;
        }
        .stApp div[data-testid="stColumn"] img{
            height: 90px !important;
            width: auto !important;
            object-fit: contain !important;
            margin: 0 auto !important;
        }
    </style>

    """,unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""

    <style>
        .stApp{
            background: #E0E3FF !important;
        }
    </style>

    """,unsafe_allow_html=True)


def style_base_layout():
#asdasd

    st.markdown("""

    <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@2004&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit&display=swap');        
        /*Hide Top Bar of streamlit*/
            #MainMenu, footer, header{
                visibility:hidden;
            }

            .block-container{ 
                padding-top:1.2rem !important; 
                padding-bottom:0rem !important;
            } 

            h1{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2.8rem !important;
                line-height: 1.1 !important;
                margin-top: 0rem !important;
                margin-bottom:0rem !important;
                letter-spacing: 0.02rem !important;
                text-align: center !important;
            }
            h1.dash-title{
                font-size: 1.6rem !important;
                line-height: 0.95 !important;
                text-align: left !important;
                color: #5865F2 !important;
                margin: 0 !important;
                white-space: nowrap !important;
}
            h2{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom:0rem !important;
            }
            
            h3, h4, p{
                font-family: 'Outfit', sans-serif;
            }
            button{
                border-radius: 999px !important;
                background: #5865F2 !important;
                color: white !important;
                padding: 10px 24px !important;
                border: None !important;
                overflow:hidden !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button[kind="secondary"]{
                border-radius: 999px !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 24px !important;
                border: None !important;
                overflow:hidden !important;
                transition: transform 0.25s ease-in-out !important;
            }
            
            button[kind="tertiary"]{
                border-radius: 999px !important;
                background: black !important;
                color: white !important;
                padding: 10px 24px !important;
                border: None !important;
                overflow:hidden !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button:hover{
                transform:scale(1.05)
            }

    </style>

    """,unsafe_allow_html=True)


