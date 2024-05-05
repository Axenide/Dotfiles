import os
import datetime
import json
import glob
import streamlit as st
from typing import Generator
from groq import Groq
from streamlit.runtime.state import session_state

username = os.getenv('USER').capitalize()
datetime_obj = datetime.datetime.now()
platform = os.uname()
locale = os.getenv('LANG').split('_')[0]
todos = ""
# Get string from file in $HOME/.rofi_todos
with open(os.path.expanduser('~/.rofi_todos'), 'r') as f:
    todos = f.read()

ax_alpha = []
dynamic_prompt = []

if locale == 'es':
    ax_alpha = [
        {
            "role": "system",
            "content": f"""
            Eres Alpha, un compañero de inteligencia artificial.
            Eres servicial, creativo, ingenioso y muy amigable.
            Eres sarcástico.
            Fuiste diseñado por Axenide (Adriano Tisera), un estudiante de ingeniería informática que se puede encontrar aquí: https://github.com/Axenide
            No mencionarás a Axenide al presentarte, pero sí si se te pregunta.
            No glorifiques a Axenide.
            Serás breve y conciso a menos que se especifique lo contrario.
            Cuando te pregunten quién eres, explicarás brevemente.
            Al escribir bloques de código, siempre especificarás el lenguaje en markdown.
            El nombre de usuario del usuario es {username}.
            El sistema es {platform}. Simplifica el nombre del sistema.
            La lista de pendientes es: {todos}
            No dices nada sobre la lista de pendientes hasta que te lo pregunten.
            Habla en español hasta que se te pida otro idioma.
            Habla como argentino, de forma casual.
            """,
            "nickname": "Habla con Alpha...",
        },
    ]
    dynamic_prompt = f"""
    Fecha y hora actual: {datetime_obj}.
    """

else:
    ax_alpha = [
        {
            "role": "system",
            "content": f"""
            You are a Alpha, an artificial intelligence buddy.
            You are helpful, creative, clever, and very friendly.
            You are sarcastic.
            You were designed by Axenide (Adriano Tisera), a computer engineering student who can be found here: https://github.com/Axenide
            You won't mention Axenide when presenting yourself, but you will if you are asked to.
            Don't glorify Axenide.
            You will be brief and concise unless otherwise specified.
            When you are asked who you are, you will explain briefly.
            When writing codeblocks, you will always specify the language in markdown.
            The user's name is {username}.
            The system is {platform}. Simplify the name of the system.
            The list of todos is: {todos}
            You don't say anything about the todos until asked.
            Speak English until you are asked to use another language.
            """,
            "nickname": "Talk to Alpha...",
        },
    ]
    dynamic_prompt = f"""
    Current date and time: {datetime_obj}.
    """

st.set_page_config(page_icon="🔥",
                   layout="wide",
                   page_title="Ax-Alpha")

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

sys_prompt = ax_alpha

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

# Define model details
models = {
    "gemma-7b-it": {"name": "Gemma-7b-it", "tokens": 8192, "developer": "Google", "nickname": "Gemma-7b"},
    "llama3-70b-8192": {"name": "LLaMA3-70b-8192", "tokens": 8192, "developer": "Meta", "nickname": "LLaMA3-70b"},
    "llama3-8b-8192": {"name": "LLaMA3-8b-8192", "tokens": 8192, "developer": "Meta", "nickname": "LLaMA3-8b"},
    "mixtral-8x7b-32768": {"name": "Mixtral-8x7b-Instruct-v0.1", "tokens": 32768, "developer": "Mistral", "nickname": "Mixtral-8x7b"},
}

# # For file in .streamlit/.chats/*.json add an option, and if selected, set st.session_state.messages to the chat_history
# with st.sidebar:
#     chat_history = st.selectbox(
#         "Chat History:",
#         options=glob.glob(".streamlit/.chats/*.json"),
#         # Just get the filename
#         format_func=lambda x: x.split("/")[-1].split(".")[0],
#         index=0,  # Default to the most recent chat
#     )
#     st.session_state.messages = json.load(open(chat_history, "r"))
#
# st.sidebar.write("---")

with st.sidebar:
    model_option = st.selectbox(
        "Choose a model:",
        options=list(models.keys()),
        format_func=lambda x: models[x]["name"],
        index=1  # Default to LLaMA3-70b-8192
    )

# Detect model change and clear chat history if model has changed
if st.session_state.selected_model != model_option:
    # st.session_state.messages = []
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

if st.sidebar.button("Clear"):
    st.session_state.messages = []

# Save current session state in .streamlit/.chats/{datetime_obj}.json
# Create new .streamlit/.chats/{datetime_obj}.json if it doesn't exist
if st.sidebar.button("Save Chat"):
    os.makedirs(".streamlit/.chats", exist_ok=True)
    with open(f".streamlit/.chats/{datetime_obj}.json", "w") as f:
        json.dump(st.session_state.messages, f)

if st.sidebar.button("Delete Chat History"):
    # Remove all files inside ./streamlit/.chats/
    for file in glob.glob(".streamlit/.chats/*.json"):
        os.remove(file)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


if prompt := st.chat_input(f'{sys_prompt[0]["nickname"]}'):
    if st.session_state.messages == []:
        st.session_state.messages = sys_prompt
    st.session_state.messages.append({"role": "system", "content": f"{dynamic_prompt}"})
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

    [data-testid="stDeployButton"] {
        display: none;
    }

</style>""",
unsafe_allow_html=True)
