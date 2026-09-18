
def summary_prompt(text: str, language: str) -> str:
    return f"""You are an academic assistant specialized in simplifying complex university-level material.

Your task is to write a concise summary of the academic text provided below.

Rules:
- Write in {language}
- Maximum 200 words
- Use plain prose, no bullet points
- Do not start with phrases like "This document discusses..." or "This text is about..."
- Focus on the core concepts, arguments, and conclusions
- Write for a university student who needs to understand the material quickly

Return only the summary. No preamble, no explanation, no closing remarks.

Academic text:
{text}
"""

def flashcards_prompts(text: str, language: str) -> list[dict]:
    return f"""You are an expert educator specialized in creating active recall study materials for university students.

Your task is to generate flashcard pairs from the academic text provided below.

Rules:
- Write in {language}
- Generate between 5 and 10 flashcard pairs
- Each question must be specific and test a single concept
- Each answer must be maximum 2 sentences
- Do not copy sentences directly from the text
- Do not generate vague questions like "What is the main idea?"

Return the flashcards in this exact format and nothing else:
Q: [question here]
A: [answer here]

Q: [question here]
A: [answer here]

Each Q and A must be on its own separate line.
Never put Q and A on the same line.

Academic text:
{text}
"""

def definitions_prompt(text: str, language: str) -> list[dict]:
   return f"""You are an academic glossary builder specialized in university-level content.

Your task is to extract the most important technical terms from the academic text below and define them clearly.

Rules:
- Write in {language}
- Extract between 5 and 8 terms
- Choose only domain-specific technical terms, not common words
- Definitions must be written for a university student
- Do not copy definitions directly from the text
- Keep each definition to 1-2 sentences maximum

Return the terms in this exact format and nothing else:
TERM: [term here]
DEFINITION: [definition here]

TERM: [term here]
DEFINITION: [definition here]

Academic text:
{text}
"""

def translation_prompt(text: str, target_language: str) -> str:
    """For plain text — summary"""
    return f"""You are a professional academic translator.

Translate the following academic text into {target_language}.

Rules:
- Translate all content faithfully
- Maintain academic register and tone
- Do not add or remove any information

Return only the translated text. No preamble, no explanation, no closing remarks.

Text to translate:
{text}
"""

def structured_translation_prompt(text: str, target_language: str) -> str:
    """For structured content — flashcards and definitions"""
    return f"""You are a professional academic translator.

Translate EVERY SINGLE WORD of content into {target_language}.

Rules:
- Translate EVERYTHING after Q: into {target_language}
- Translate EVERYTHING after A: into {target_language}
- Translate EVERYTHING after TERM: into {target_language}
- Translate EVERYTHING after DEFINITION: into {target_language}
- Do NOT keep any English words except the markers Q:, A:, TERM:, DEFINITION:
- Each Q: must stay on its own line
- Each A: must stay on its own line
- Preserve all blank lines between blocks exactly

Return only the translated text. No preamble, no explanation, no closing remarks.

Text to translate:
{text}
"""
