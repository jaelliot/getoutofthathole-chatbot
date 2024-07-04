import streamlit as st  # type: ignore
import subprocess
from get_embedding_function import get_embedding_function
from query_data import query_rag
from markdown_utils import strip_markdown  # Import the Markdown cleaning function

def populate_database():
    try:
        # Run the populate_database.py script
        result = subprocess.run(['python', 'populate_database.py', '--reset'], capture_output=True, text=True)
        if result.returncode == 0:
            st.sidebar.success("Database populated successfully.")
        else:
            st.sidebar.error(f"Error populating database: {result.stderr}")
    except Exception as e:
        st.sidebar.error(f"Exception occurred while populating database: {str(e)}")

# Populate the database when the app starts
populate_database()

with st.sidebar:
    st.title("Useful Information")
    st.markdown("""
    - **Source Code:** [View the source code](https://github.com/UVU-Portfolio/getoutofthathole-chatbot)
    - **Streamlit Documentation:** [View the documentation](https://docs.streamlit.io/)
    - **Cohere Documentation:** [View the documentation](https://docs.cohere.com/)
    - **Groq Documentation:** [View the documentation](https://groq.com/)
    - **Mistral Documentation:** [View the documentation](https://docs.mistral.ai/)
    - **Railway.app Documentation:** [View the documentation](https://docs.railway.app/)
    """)

st.title("Puck Bot")
st.caption("A Streamlit chatbot powered by Cohere and Groq")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi there! How can I help you find the resources you need to stay safe and informed?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Use custom AI backend
    response = query_rag(prompt)
    # Clean response for display
    clean_response = strip_markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": clean_response})
    st.chat_message("assistant").write(clean_response)
