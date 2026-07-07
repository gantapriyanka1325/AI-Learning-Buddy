import streamlit as st
import requests

st.set_page_config(page_title="AI Learning Buddy Maya", page_icon="🎓")

API_KEY = st.secrets["OPENROUTER_API_KEY"]

st.title("🎓 AI Learning Buddy Maya")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        else:
            prompt = topic

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "meta-llama/llama-3.1-8b-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"]
            st.success("Generated Successfully ✅")
            st.write(answer)
        else:
            st.error(response.text)
