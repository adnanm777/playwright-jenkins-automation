import os
from google import genai


class AIHealer:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable not found"
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def find_best_candidate(
        self,
        broken_text,
        candidates
    ):

        candidate_text = "\n".join(
            f"{i + 1}. {text}"
            for i, text in enumerate(candidates)
        )

        prompt = f"""
You are an AI locator healing assistant.

A Playwright locator has failed.

Broken text:
{broken_text}

Available DOM text candidates:
{candidate_text}

Choose the candidate that is most likely to be the
replacement for the broken text.

Return only this format:

BEST: <candidate text>
CONFIDENCE: <number between 0 and 1>
REASON: <short reason>
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text