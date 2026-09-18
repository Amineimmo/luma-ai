from dotenv import load_dotenv
from google import genai
import os
from prompts import summary_prompt, translation_prompt, flashcards_prompts, definitions_prompt,structured_translation_prompt
from utils import parse_flashcards, parse_definitions

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_summary(text: str, language: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=summary_prompt(text, language)
    )
    return response.candidates[0].content.parts[0].text


def get_flashcards(text: str, language: str) -> list[dict]:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=flashcards_prompts(text, language)  # ✅ fixed
    )
    return parse_flashcards(response.candidates[0].content.parts[0].text)


def get_definitions(text: str, language: str) -> list[dict]:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=definitions_prompt(text, language)
    )
    return parse_definitions(response.candidates[0].content.parts[0].text)


def translate_output(text: str, target_language: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=translation_prompt(text, target_language)
    )
    return response.candidates[0].content.parts[0].text

def translate_structured(text: str, target_language: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=structured_translation_prompt(text, target_language)
    )
    return response.candidates[0].content.parts[0].text