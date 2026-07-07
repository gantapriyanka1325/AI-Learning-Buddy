import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Learning Buddy Maya",
    page_icon="🎓"
)

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

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

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.success("Generated Successfully ✅")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {e}")
