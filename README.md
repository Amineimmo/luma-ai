# 💡 Lumi — Illuminate Your Academic Documents

> Transform complex academic PDFs into concise summaries, active recall flashcards, and key terminology definitions — in English, French, and Arabic.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square)
![Gemini](https://img.shields.io/badge/Gemini-3.5_Flash_Lite-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🎯 The Problem

University students — especially in multilingual environments — spend hours decoding dense lecture notes before exams. Existing tools are either English-only, paywalled, or too generic to be useful for academic content.

**Lumi solves this in under 30 seconds.**

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **Smart Summary** | Concise prose summary focused on core concepts and conclusions |
| 🃏 **Flashcard Generation** | Active recall Q&A pairs for exam preparation |
| 📚 **Key Term Definitions** | Domain-specific terminology explained for university students |
| 🌐 **Multilingual Output** | English, French, and Arabic — switch anytime without re-uploading |
| ⚡ **Fast Processing** | Powered by Gemini 3.5 Flash Lite for low-latency responses |

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| PDF Extraction | PyMuPDF |
| AI Model | Google Gemini 3.5 Flash Lite |
| Language | Python 3.9+ |
| API | Google AI Studio |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com)

### 1. Clone the repository
```bash
git clone https://github.com/Amineimmo/lumi-ai.git
cd lumi-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

---

## 📖 How to Use

1. **Upload** any academic PDF using the sidebar
2. **Select** your output language (English, French, or Arabic)
3. **Click** Generate — Lumi processes your document in seconds
4. **Browse** results across 3 tabs: Summary, Flashcards, Definitions
5. **Switch language** anytime using the translate button — no re-upload needed

---

## 📁 Project Structure

```
lumi-ai/
├── app.py              # Streamlit UI and pipeline orchestration
├── extractor.py        # PDF text extraction via PyMuPDF
├── gemini_client.py    # Google Gemini API wrapper
├── prompts.py          # Prompt engineering templates
├── utils.py            # Text chunking and response parsers
├── requirements.txt    # Python dependencies
├── .env                # API key — not tracked by Git
└── .gitignore
```

---

## 🌍 Multilingual Support

Lumi supports academic content output in three languages:

- 🇬🇧 **English**
- 🇫🇷 **French**
- 🇸🇦 **Arabic**

Language selection works both before generation and as a live switch after results are displayed — with no need to re-upload your document.

---

## 🏗️ Architecture

```
PDF Upload
    ↓
extractor.py  →  raw text extraction via PyMuPDF
    ↓
utils.py      →  text chunking (3000 char limit)
    ↓
gemini_client.py  →  3 parallel prompt calls:
    ├── prompts.py  →  Summary prompt    →  plain text
    ├── prompts.py  →  Flashcards prompt →  parsed to list[dict]
    └── prompts.py  →  Definitions prompt→  parsed to list[dict]
    ↓
app.py  →  Streamlit tabs render results
    ↓
(on demand) Translation call  →  reparse  →  rerender
```

---

## 🏆 Built For

**ML Empowerment Build Challenge 3.0** — Devpost

Tracks targeted:
- ✅ Machine Learning / AI
- ✅ Education
- ✅ Social Good
- ✅ Beginner-Friendly

---

## 👨‍💻 Author

**Mohamed Amine Bouhassoune**
First-year IT & AI Engineering Student
ENSA Agadir, Université Ibn Zohr — Morocco

Built solo in 1 day.

[![GitHub](https://img.shields.io/badge/GitHub-Amineimmo-black?style=flat-square&logo=github)](https://github.com/Amineimmo)

---

## 📄 License

MIT License — free to use, modify, and distribute.
