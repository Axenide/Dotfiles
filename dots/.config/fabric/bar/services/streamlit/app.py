import os
import streamlit as st
from typing import Generator
from groq import Groq

st.set_page_config(page_icon="🔥",
                   layout="wide",
                   page_title="Ax-Alpha")

username = os.getenv('USER').capitalize()

st.write("<h1 style='text-align: center;'><span style='font-size: 72pt; opacity: 0.5;'>🔥</span></h1>", unsafe_allow_html=True)

st.write(
    """
    <p style='text-align: center;'>
    <span style='
    font-family: Empires;
    font-size: 48pt;
    font-weight: 600;
    position: relative;
    bottom: 110px;
    text-shadow:
    0px -2px 0px #000,
    0px -1px 0px #000,
    0px 0px 0px #000,
    0px 1px 0px #000,
    0px 2px 0px #000,
    0px 3px 0px #000,
    0px 4px 0px #000,
    0px 5px 0px #000,
    -2px -2px 0px #000,
    -2px -1px 0px #000,
    -2px 0px 0px #000,
    -2px 1px 0px #000,
    -2px 2px 0px #000,
    -2px 3px 0px #000,
    -2px 4px 0px #000,
    -2px 5px 0px #000,
    2px -2px 0px #000,
    2px -1px 0px #000,
    2px 0px 0px #000,
    2px 1px 0px #000,
    2px 2px 0px #000,
    2px 3px 0px #000,
    2px 4px 0px #000,
    2px 5px 0px #000;
    '>
    <span style='color: #db4740; font-style: italic;'>Ax</span><span style='color: #47423e;'>-</span>Alpha</span>
    </p>
    """,
    unsafe_allow_html=True)

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

# Define model details
models = {
    "gemma-7b-it": {"name": "Gemma-7b-it", "tokens": 8192, "developer": "Google", "nickname": "Gemma-7b"},
    "llama2-70b-4096": {"name": "LLaMA2-70b-chat", "tokens": 4096, "developer": "Meta", "nickname": "LLaMA2"},
    "llama3-70b-8192": {"name": "LLaMA3-70b-8192", "tokens": 8192, "developer": "Meta", "nickname": "LLaMA3-70b"},
    "llama3-8b-8192": {"name": "LLaMA3-8b-8192", "tokens": 8192, "developer": "Meta", "nickname": "LLaMA3-8b"},
    "mixtral-8x7b-32768": {"name": "Mixtral-8x7b-Instruct-v0.1", "tokens": 32768, "developer": "Mistral", "nickname": "Mixtral-8x7b"},
}

with st.sidebar:
    model_option = st.selectbox(
        "Choose a model:",
        options=list(models.keys()),
        format_func=lambda x: models[x]["name"],
        index=2  # Default to LLaMA3-70b-8192
    )

# Detect model change and clear chat history if model has changed
if st.session_state.selected_model != model_option:
    st.session_state.messages = []
    st.session_state.selected_model = model_option

max_tokens_range = models[model_option]["tokens"]

with st.sidebar:
    # Adjust max_tokens slider dynamically based on the selected model
    max_tokens = st.slider(
        "Max Tokens:",
        min_value=512,  # Minimum value to allow some flexibility
        max_value=max_tokens_range,
        # Default value or max allowed if less
        value=min(32768, max_tokens_range),
        step=512,
        help=f"Adjust the maximum number of tokens (words) for the model's response. Max for selected model: {max_tokens_range}"
    )

st.sidebar.write("---")

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


if prompt := st.chat_input(f'Talk to {models[model_option]["nickname"]}...'):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Fetch response from Groq API
    try:
        chat_completion = client.chat.completions.create(
            model=model_option,
            messages=[
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.messages
            ],
            max_tokens=max_tokens,
            stream=True
        )

        # Use the generator function with st.write_stream
        with st.chat_message("assistant"):
            chat_responses_generator = generate_chat_responses(chat_completion)
            full_response = st.write_stream(chat_responses_generator)
    except Exception as e:
        st.error(e, icon="🚨")

    # Append the full response to session_state.messages
    if isinstance(full_response, str):
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response})
    else:
        # Handle the case where full_response is not a string
        combined_response = "\n".join(str(item) for item in full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": combined_response})

# st.markdown(
#     """
#     <style>
#     *, :root {
#         font-family: 'Iosevka Nerd Font';
#     }
#     header {display: none;}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.markdown("""
<style>
	[data-testid="stDecoration"] {
		display: none;
	}

    [data-testid="stAppViewContainer"] {
        border: 1px solid #1b1d1d;
        border-radius: 8px;
    }

    [data-testid="stHeader"] {
        border-top: 1px solid #1b1d1d;
        border-left: 1px solid #1b1d1d;
        border-right: 1px solid #1b1d1d;
        border-radius: 8px 8px 0px 0px;
    }

</style>""",
unsafe_allow_html=True)
