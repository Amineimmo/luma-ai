import re
import re

def parse_flashcards(raw: str) -> list[dict]:
    matches = re.findall(
        r"(?ms)^\s*Q:\s*(.*?)\s*^\s*A:\s*(.*?)(?=^\s*Q:|\Z)",
        raw.strip()
    )

    return [
        {"question": question.strip(), "answer": answer.strip()}
        for question, answer in matches
        if question.strip() and answer.strip()
    ]

def parse_definitions(raw: str) -> list[dict]:
    defs = []
    pairs = raw.strip().split("\n\n")
    for pair in pairs:
        lines = pair.strip().split("\n")
        if len(lines) >= 2:
            term = lines[0].replace("TERM: ", "").strip()
            definition   = lines[1].replace("DEFINITION: ", "").strip()
            defs.append({"term": term, "definition": definition})
    return defs

def chunk_text(text: str, max_chars: int = 3000) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars]

def flashcards_to_string(flashcards: list[dict]) -> str:
    lines = []
    for card in flashcards:
        lines.append(f"Q: {card['question']}\nA: {card['answer']}")
    return "\n\n".join(lines)


def definitions_to_string(definitions: list[dict]) -> str:
    lines = []
    for item in definitions:
        lines.append(f"TERM: {item['term']}\nDEFINITION: {item['definition']}")
    return "\n\n".join(lines)