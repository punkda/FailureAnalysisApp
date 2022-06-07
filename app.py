import streamlit as st
from multiapp import MultiApp
from apps import machine, panne, op # import your app modules here
import json
from streamlit_lottie import st_lottie


import pickle
from pathlib import Path

import streamlit_authenticator as stauth





app = MultiApp()
st.set_page_config(page_title="Failure Analysis", page_icon=":bar_chart:")

def load_lottiefile(filepath : str):
    with open (filepath,"r")as f :
        return json.load(f)
lottie=load_lottiefile("29419-data-visualization.json")
with st.sidebar:
    st_lottie(lottie , height=200,width=300,)
    
# --- USER AUTHENTICATION ---
names = ["admin"]
usernames = ["123"]
names = ["admin"]
usernames = ["admin"]
passwords = ["123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "Failure_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:    

    st.sidebar.markdown("""
    # Failure Data Analysis


    """)

    # Add all your application here
    st.sidebar.markdown("""Choose Visualization feature""")
    app.add_app("Visualization Per Machine", machine.app)
    app.add_app("Visualization Per Failure", panne.app)
    app.add_app("Visualization Per Operator", op.app)
    
    # The main app
    app.run()
    authenticator.logout("Logout", "sidebar")

    # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
