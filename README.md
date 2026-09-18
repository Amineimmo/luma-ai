# Lumi

> Turn university PDFs into concise, review-ready study materials.

## Overview

**Lumi** is a Streamlit study assistant built for university students who need to get through dense course PDFs more efficiently.

Upload a PDF, choose **English, French, or Arabic**, and Lumi generates three study resources from the document:

- A concise summary
- Flashcards for active recall
- Key definitions for quick revision

The generated material can also be translated into the selected language and downloaded as text files for later review.

## What it does

- 📄 **PDF-based studying** — upload a university course PDF and extract its text.
- 📝 **Concise summaries** — turn long course material into a shorter revision-oriented summary.
- 🧠 **Flashcards** — generate question-and-answer cards with hidden answers for self-testing.
- 📚 **Key definitions** — extract important concepts and their definitions.
- 🌍 **Multilingual output** — generate study material in **English, French, or Arabic**.
- 🔄 **Translation support** — translate generated study content while preserving the structure needed by the UI.
- 📊 **Generation progress** — show progress while study materials are being generated.
- 👀 **Interactive flashcards** — reveal answers when you're ready instead of displaying everything at once.
- 💾 **Downloadable study packs** — save generated content as text files.
- ⚠️ **Error handling** — display useful error states when processing or generation fails.
- 🌑 **Dark theme** — use a dark Streamlit interface for a focused study experience.

## How it works

Lumi follows a simple pipeline:

```text
University PDF
     │
     ▼
PDF text extraction
     │
     ▼
Gemini processing
     │
     ├──► Summary
     ├──► Flashcards
     └──► Key definitions
             │
             ▼
       Optional translation
             │
             ▼
      Interactive study UI
             │
             ▼
       Downloadable files