from difflib import SequenceMatcher
from playwright.sync_api import Page


class GenericLocatorHealer:

    def __init__(self, page: Page):
        self.page = page

    def find_by_text(self, broken_text: str):

        print("\n🔍 Searching text candidates...")

        candidates = self.page.locator(
            "a, button, input, label, h1, h2, h3, span"
        )

        best_text = None
        best_score = 0

        checked_texts = set()

        for i in range(candidates.count()):

            element = candidates.nth(i)

            try:
                text = element.inner_text().strip()
            except Exception:
                continue

            if not text:
                continue

            if text in checked_texts:
                continue

            checked_texts.add(text)

            score = SequenceMatcher(
                None,
                broken_text.lower(),
                text.lower()
            ).ratio()

            if score > best_score:

                best_score = score
                best_text = text

            if score >= 0.5:

                print(
                    f"Candidate: {text[:80]} "
                    f"| Score: {score:.2f}"
                )

        # Confidence threshold

        if best_text and best_score >= 0.80:

            return best_text, best_score

        print(
            f"\n⚠️ Confidence too low: "
            f"{best_score:.2f}"
        )

        return None, best_score

    def find_by_role(self, broken_name: str):

        print("\n🔍 Searching button/link candidates...")

        elements = self.page.locator(
            "button, a, input[type='button'], input[type='submit']"
        )

        best_element = None
        best_score = 0

        checked_texts = set()

        for i in range(elements.count()):

            element = elements.nth(i)

            try:
                text = element.inner_text().strip()
            except Exception:
                continue

            if not text:
                continue

            if text in checked_texts:
                continue

            checked_texts.add(text)

            score = SequenceMatcher(
                None,
                broken_name.lower(),
                text.lower()
            ).ratio()

            if score > best_score:

                best_score = score
                best_element = element

            if score >= 0.5:

                print(
                    f"Candidate: {text[:80]} "
                    f"| Score: {score:.2f}"
                )

        if best_element and best_score >= 0.80:

            return best_element, best_score

        print(
            f"\n⚠️ Confidence too low: "
            f"{best_score:.2f}"
        )

        return None, best_score