import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:  # Fixed typo here
        return None
    return r.json()

# ----LOAD ASSETS----
lottie_coding = load_lottieurl("https://lottie.host/a3bde22d-d1f0-41f8-a8b8-1ce2d3341d97/s5l6eC6liR.json")  # Fixed syntax here

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Favour :wave:")
    st.title("A Software Engineering Enthusiast")
    st.write("I am passionate about utilizing my technical skills to build software that can improve access to education in Africa.")
    st.write("[Learn More >](https://www.linkedin.com/in/umejesi-favour)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("What I do")
    st.write("##")
    st.write(
        """
        As a Computer Science major at Grambling State University, I am currently pursuing an undergraduate certificate in Data Analytics. My interests span Software Engineering and Data Science, driven by a passion for leveraging technology to create a positive societal impact. I aspire to utilize my technical skills to develop software that addresses environmental challenges and promotes sustainability. Ultimately, I aim to harness technology to improve the education system in Africa.

        As Albert Einstein once said, "The measure of intelligence is the ability to change." I believe that through innovative solutions, we can drive meaningful change in our communities.

        Feel free to contact me if you’re interested in collaborating on projects. Email: umejesif@gmail.com
        """
    )
    st.write("[Learn More>](https://github.com/KingOz-stack/KingOz-stack)")
        
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
