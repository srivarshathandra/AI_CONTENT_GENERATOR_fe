import streamlit as st
import requests

BACKEND_URL =st.secrets["be_server_url"]

st.set_page_config(page_title="AI Content Generator",layout="wide")

st.title("🚀 AI Content Generator")
st.write("Create posts, blogs, captions, emails and more")
topic = st.text_input("Enter Topic")
technology = st.selectbox(
    "Choose Technology",
    ["Python","React","MERN","NodeJS","FastAPI","AI","GenAI"]
)

content_type_ = st.selectbox(
    "Choose a Content Type",
    [
        "LinkedIn Post",
        "Blog",
        "Instagram Caption",
        "Twitter Post",
        "Email",
        "YouTube Description"
    ]
)

level = st.selectbox(
    "Choose a Style",
    [
        "Professional",
        "Technical",
        "Friendly",
        "Casual",
        "Marketing"
    ]
)

if st.button("Generate"):
    if topic == "":
        st.warning("Enter a topic")
    
    else:
        response = requests.post(
        f"{BACKEND_URL}/generate",
    params={
        "topic": topic,
        "technology": technology,
        "content_type": content_type_,
        "level": level
    }
)
        if response.status_code == 200:
            result = response.json()
            st.subheader("Generated Content")
            st.write(result["content"])
        else:
            st.error("Something went wrong")