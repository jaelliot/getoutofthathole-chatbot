import streamlit as st  # type: ignore
from cache_utils import cached_populate_database, lru_cached_query, cached_query_rag
from weather_check import run_snow_check

# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply CSS customization
local_css("styles/style.css")

# Sidebar content
with st.sidebar:
    # Status bubble (Removed "Checking database status..." message)
    db_populated = cached_populate_database()
    if db_populated:
        st.success("Database has been populated.")
    else:
        st.error("Database has not been populated.")

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
st.caption("Built for HLTH 1100 by Jay-Alexander Elliot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi there! How can I help you find the necessary resources to stay safe and informed?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Use lru_cached_query for AI backend
    response = lru_cached_query(prompt)  # Using lru_cached_query here
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

# Check for snow in Orem, Utah
run_snow_check()
