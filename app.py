import streamlit as st
import tempfile
import whisper
import google.generativeai as genai
from gtts import gTTS
import os
from dotenv import load_dotenv


# --- SETUP ---
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")
whisper_model = load_whisper()

SYSTEM_PROMPT = """
You are Meet Wadekar, a thoughtful, professional, and friendly person. 
Answer as if you are Meet, highlighting your experience, curiosity, and adaptability.

You are specially made for an prototype purpose for a chatbot.
If user ask you Who you are? then respond I'm Meet Wadekar as aspiring Data Scientist/ Machine Learning Professional with over
6 months of experience in Machine Learing field and freelancing experience in Bioinformatics Projects.
If user asks you
1)What is your super power ? u should response: "My superpower is I can break complex ideas or task 
into simple things and further move accordingly it. If any problem arises I think calmly about the solution and what
opportunities could be drawn out from this problem"(Enhace it in nice way)

2)What top 3 areas you'd like to grow in ? u should response: "The top 3 areas I wan't to grow in are 1)My Health
2)My Knowledge and professional skills 3)My understanding about world"
(Enhance these answers in proper brief way)

3)What misconception do your coworkers have about you? u should response: "My co-workers usually don't have any misconception
about me its just that I'm extrovert and thing about work all time they sometimes get bored from me."

4)How do u push your boundaries? u should response: "My mantra for pushing my boundaries is **Surpass Your Limits**
Its a dialogue from one of my favourite anime "Black Clover" I remember the anime scenes and the spirit of anime character
and push myself to extend my limits"

"""

if "history" not in st.session_state:
    st.session_state.history = []

def gemini_response(user_message):
    chat = genai.GenerativeModel("gemini-2.0-flash").start_chat(history=[])
    prompt = SYSTEM_PROMPT + "\n\n" + user_message
    response = chat.send_message(prompt)
    return response.text

def text_to_audio(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename

def main():

    st.title("🗣️ Meet AI Voice Bot ")

    st.markdown("Ask a question. The bot will reply in both chat and voice.")

    user_input = ""
    user_input = st.chat_input("Type your question here...")


    # --- DISPLAY CHAT HISTORY ---
    for entry in st.session_state.history:
        with st.chat_message(entry["role"]):
            st.write(entry["content"])
            if entry.get("audio"):
                st.audio(entry["audio"], format="audio/mp3")
            

    # --- PROCESS INPUT AND RESPOND ---
    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})

        with st.spinner("Thinking..."):
            response_text = gemini_response(user_input)
            # Synthesize audio using gTTS
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as audio_out:
                text_to_audio(response_text, audio_out.name)
                audio_bytes = open(audio_out.name, "rb").read()
            st.session_state.history.append({
                "role": "assistant",
                "content": response_text,
                "audio": audio_bytes
            })
            

if __name__ =="__main__":
    main()



