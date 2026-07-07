import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Learning Buddy Maya", page_icon="🎓")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")
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
    if topic == "":
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

        try:
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(str(e))
