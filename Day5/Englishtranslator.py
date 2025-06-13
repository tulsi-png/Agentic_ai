import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
import os

# --- Gemini API Key Configuration ---
# Replace "your-gemini-api-key" with your actual Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDtgwOZNPWmJ3cU-RV09cOnnAJAuj8JTxE"

# --- Initialize the Gemini Chat LLM ---
try:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)
except Exception as e:
    st.error(f"Failed to initialize Gemini model: {e}")
    st.stop()

# --- Create the Prompt Template ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English to French."),
    ("user", "Translate this sentence to French:\n\n{sentence}")
])

# --- Define the Chain ---
chain: Runnable = prompt | llm

# --- Streamlit UI ---
st.set_page_config(page_title="English to French Translator", page_icon="🌍")
st.title("🌍 English to French Translator")
st.write("Enter a sentence in English and click **Translate** to see the French version.")

# --- Input ---
input_sentence = st.text_input("Enter English sentence:")

# --- Translate Button ---
if st.button("Translate"):
    if not input_sentence.strip():
        st.warning("Please enter a valid sentence.")
    else:
        try:
            # Run the chain
            result = chain.invoke({"sentence": input_sentence})
            # Show the result
            st.success("Translation complete!")
            st.subheader("🇫🇷 Translated Sentence:")
            st.write(result.content)
        except Exception as e:
            st.error(f"Translation failed: {e}")
