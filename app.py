import streamlit as st
import requests

BACKEND_URL = st.secrets["be_server_url"]

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

    if not topic.strip():
        st.warning("Please enter a topic")

    else:

        try:

            st.write("Backend:", BACKEND_URL)

            with st.spinner("Generating content..."):

                response = requests.post(
                    f"{BACKEND_URL}/generate",
            params={
                    "topic": topic,
                    "technology": technology,
                    "content_type_": content_type_,
                    "level": level
                    },
                    timeout=60)

            if response.status_code == 200:

                result = response.json()

                st.subheader("Generated Content")

                st.write(result.get("content","No content returned"))

            else:

                st.error(
                    f"Backend Error: {response.status_code}"
                )

                st.write(response.text)

        except requests.exceptions.Timeout:

            st.error(
                "Request timed out. Backend may be waking up."
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to backend."
            )

        except Exception as e:

            st.error(
                f"Unexpected Error: {e}"
            )