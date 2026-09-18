import streamlit as st
from extractor import extract_txt
from gemini_client import get_summary, get_flashcards, get_definitions, translate_output,translate_structured
from utils import chunk_text, flashcards_to_string, definitions_to_string, parse_definitions, parse_flashcards

st.set_page_config(page_title="Lumi", page_icon="💡", layout="wide")
st.title("💡 Lumi")
st.caption("Illuminate your academic documents — summaries, flashcards, and definitions powered by AI.")

# ---- SIDEBAR ----
with st.sidebar:
    st.header("Upload your document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    language = st.selectbox("Output language", options=["English", "French", "Arabic"])
    generate_btn = st.button("✨ Generate", use_container_width=True)

# ---- PIPELINE ----
if generate_btn and uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    raw_text = extract_txt("temp.pdf")
    text = chunk_text(raw_text)
    with st.spinner("Generating your study materials..."):
        st.session_state["summary"] = get_summary(text, language)
        st.session_state["flashcards"] = get_flashcards(text, language)
        st.session_state["definitions"] = get_definitions(text, language)
        st.session_state["language"] = language

if "summary" in st.session_state:
    if language != st.session_state["language"]:
        translate_btn = st.button(f"🌐 Translate to {language}")
        if translate_btn:
            with st.spinner(f"Translating to {language}..."):
                st.session_state["summary"] = translate_output(
                st.session_state["summary"], language  # plain translation
                )
                flashcards_str = flashcards_to_string(st.session_state["flashcards"])
                translated_flashcards = translate_structured(flashcards_str, language)  # structured
                st.session_state["flashcards"] = parse_flashcards(translated_flashcards)

                definitions_str = definitions_to_string(st.session_state["definitions"])
                translated_definitions = translate_structured(definitions_str, language)  # structured
                st.session_state["definitions"] = parse_definitions(translated_definitions)
                st.session_state["language"] = language

# ---- RESULTS ----
if "summary" in st.session_state:
    tab1, tab2, tab3 = st.tabs(["📄 Summary", "🃏 Flashcards", "📚 Definitions"])
    with tab1:
        st.subheader("Document Summary")
        st.write(st.session_state["summary"])
    with tab2:
        st.subheader("Flashcards")
        for i, card in enumerate(st.session_state["flashcards"], 1):
            with st.expander(f"Card {i}: {card['question']}"):
                st.write(card["answer"])
    with tab3:
        st.subheader("Key Definitions")
        for item in st.session_state["definitions"]:
            st.markdown(f"**{item['term']}**")
            st.write(item["definition"])
            st.divider()