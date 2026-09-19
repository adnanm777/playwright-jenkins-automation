from difflib import SequenceMatcher
from playwright.sync_api import Page


class LocatorHealer:

    def __init__(self, page: Page):
        self.page = page

    def heal_alt_text(self, broken_alt: str):

        print("\n🔍 Searching DOM for possible replacements...")

        images = self.page.locator("img[alt]")

        best_alt = None
        best_score = 0

        for i in range(images.count()):

            alt = images.nth(i).get_attribute("alt")

            if not alt:
                continue

            score = SequenceMatcher(
                None,
                broken_alt.lower(),
                alt.lower()
            ).ratio()

            print(
                f"Candidate: {alt} | "
                f"Score: {score:.2f}"
            )

            if score > best_score:

                best_score = score
                best_alt = alt

        if best_alt and best_score >= 0.5:

            return best_alt, best_score

        return None, best_score
