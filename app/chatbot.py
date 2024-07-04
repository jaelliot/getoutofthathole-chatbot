import streamlit as st  # type: ignore
import subprocess
import asyncio
from app.get_embedding_function import get_embedding_function
from app.query_data import query_rag

# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to populate the database
def populate_database():
    try:
        result = subprocess.run(['python', 'app/populate_database.py', '--reset'], capture_output=True, text=True)
        if result.returncode == 0:
            st.sidebar.success("Database populated successfully.")
        else:
            st.sidebar.error(f"Error populating database: {result.stderr}")
    except Exception as e:
        st.sidebar.error(f"Exception occurred while populating database: {str(e)}")

# Asynchronous function to query the AI backend
async def async_query_rag(prompt):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, query_rag, prompt)
    return response

# Populate the database when the app starts
populate_database()

# Apply CSS customization
local_css("styles/style.css")

# Sidebar content
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

# Main content
st.title("Puck Bot")
st.caption("A Streamlit chatbot powered by Cohere and Groq")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi there! How can I help you find the necessary resources to stay safe and informed?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Use asynchronous call to the AI backend
    response = asyncio.run(async_query_rag(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
