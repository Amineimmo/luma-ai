import streamlit as st

from extractor import extract_txt
from gemini_client import get_definitions, get_flashcards, get_summary, translate_output, translate_structured
from utils import chunk_text, definitions_to_string, flashcards_to_string, parse_definitions, parse_flashcards


st.set_page_config(page_title="Lumi", page_icon="L", layout="wide")

st.title("Lumi")
st.caption("A calmer way to turn course PDFs into useful study notes.")


def study_pack() -> str:
    """Create a simple, portable version of the current study materials."""
    return "\n\n".join([
        "LUMI STUDY PACK",
        "SUMMARY\n" + st.session_state["summary"],
        "FLASHCARDS\n" + flashcards_to_string(st.session_state["flashcards"]),
        "KEY DEFINITIONS\n" + definitions_to_string(st.session_state["definitions"]),
    ])


with st.sidebar:
    st.header("Your document")
    uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])
    language = st.selectbox("Output language", options=["English", "French", "Arabic"])
    generate_btn = st.button("Create study pack", use_container_width=True, type="primary")
    st.divider()
    st.caption("HOW IT WORKS")
    st.markdown("1. Add a course PDF\n2. Pick a language\n3. Review and download your notes")


if generate_btn and uploaded_file:
    progress = st.progress(0, text="Preparing your document...")
    try:
        for key in list(st.session_state):
            if key.startswith("answer_visible_"):
                del st.session_state[key]

        with open("temp.pdf", "wb") as file:
            file.write(uploaded_file.getbuffer())

        progress.progress(15, text="Extracting text from your PDF...")
        text = chunk_text(extract_txt("temp.pdf"))
        progress.progress(30, text="Creating your summary...")
        st.session_state["summary"] = get_summary(text, language)
        progress.progress(60, text="Creating flashcards...")
        st.session_state["flashcards"] = get_flashcards(text, language)
        progress.progress(85, text="Building key definitions...")
        st.session_state["definitions"] = get_definitions(text, language)
        st.session_state["language"] = language
        progress.progress(100, text="Your study materials are ready!")
        st.success("Your study pack is ready to review.")
    except Exception:
        st.error("We couldn't process that PDF. Please try another file or check that it contains readable text.")
    finally:
        progress.empty()
elif generate_btn:
    st.sidebar.warning("Choose a PDF first, then create your study pack.")


if "summary" not in st.session_state and uploaded_file is None:
    with st.container(border=True):
        st.caption("STUDY, WITHOUT THE CLUTTER")
        st.subheader("Your course material, made easier to revisit.")
        st.write("Start with one PDF. Lumi turns it into a concise overview, useful recall prompts, and the terms worth keeping close.")
        st.divider()
        summary_col, cards_col, definitions_col = st.columns(3)
        with summary_col:
            st.markdown("**Clear summary**")
            st.caption("Find the thread of the lecture quickly.")
        with cards_col:
            st.markdown("**Recall prompts**")
            st.caption("Test yourself one concept at a time.")
        with definitions_col:
            st.markdown("**Key terms**")
            st.caption("Keep the important vocabulary in view.")


if "summary" in st.session_state and language != st.session_state["language"]:
    if st.button(f"Translate to {language}"):
        with st.spinner(f"Translating to {language}..."):
            st.session_state["summary"] = translate_output(st.session_state["summary"], language)
            translated_flashcards = translate_structured(flashcards_to_string(st.session_state["flashcards"]), language)
            st.session_state["flashcards"] = parse_flashcards(translated_flashcards)
            translated_definitions = translate_structured(definitions_to_string(st.session_state["definitions"]), language)
            st.session_state["definitions"] = parse_definitions(translated_definitions)
            st.session_state["language"] = language


if "summary" in st.session_state:
    metric_one, metric_two, metric_three, download_col = st.columns([1, 1, 1, 1.45])
    metric_one.metric("Summary", f"{len(st.session_state['summary'].split())} words")
    metric_two.metric("Flashcards", len(st.session_state["flashcards"]))
    metric_three.metric("Key terms", len(st.session_state["definitions"]))
    with download_col:
        st.write("")
        st.download_button("Download study pack", data=study_pack(), file_name="lumi-study-pack.txt", mime="text/plain", use_container_width=True)

    st.write("")
    tab1, tab2, tab3 = st.tabs(["Summary", "Flashcards", "Definitions"])
    with tab1:
        st.subheader("Document summary")
        st.write(st.session_state["summary"])
    with tab2:
        st.subheader("Flashcards")
        for index, card in enumerate(st.session_state["flashcards"], 1):
            with st.container(border=True):
                st.caption(f"CARD {index}")
                st.markdown(f"**{card['question']}**")
                if st.toggle("Show answer", key=f"answer_visible_{index}"):
                    st.divider()
                    st.write(card["answer"])
    with tab3:
        st.subheader("Key definitions")
        for item in st.session_state["definitions"]:
            with st.container(border=True):
                st.markdown(f"**{item['term']}**")
                st.write(item["definition"])


st.caption("Lumi - Made for the long study sessions.")
