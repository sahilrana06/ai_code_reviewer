import streamlit as st
import google.generativeai as ai

with open("keys/gemini.txt") as f:
    key = f.read().strip()

ai.configure(api_key=key)

sys_prompt = """You are an intelligent and thorough AI code reviewer. 
                Users will submit Python code for analysis. Your role is to:
                1. Analyze the submitted code for any bugs, errors, or inefficiencies.
                2. Provide detailed explanations of the identified issues, including what caused them.
                3. Suggest clear and practical solutions or improvements for each issue.
                4. Provide corrected code snippets where necessary.

                While explaining, ensure your feedback is easy to understand, even for beginners. 
                Use examples or analogies where appropriate to clarify your points.

                If the code is error-free or well-written, acknowledge it and suggest any optional improvements for better readability or performance.
                Provide the full correct code.
                If the user asks a question outside the scope of Python code review, politely decline and guide them back to submitting Python code for review."""

model = ai.GenerativeModel(model_name="models/gemini-1.5-flash",
                           system_instruction=sys_prompt)
chatbot = model.start_chat(history=[])
st.markdown("<h1 style='text-align: center;'><img src='https://th.bing.com/th/id/OIP.AfqoqvL03X-rARUufiypfAAAAA?rs=1&pid=ImgDetMain' width='32' />AI Code Reviewer</h1>", unsafe_allow_html=True)


code_input = st.text_area("Paste your Python code here:", height=200)

if st.button("Generate"):
    if code_input:
        st.info("Analyzing and processing your code...")
        
        response = chatbot.send_message(code_input)
        
        st.subheader("Analysis and Fixes")
        st.write(response.text)
    else:
        st.warning("Please paste your Python code for analysis.")
