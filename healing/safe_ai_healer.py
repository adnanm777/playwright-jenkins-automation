import re
from healing.ai_healer import AIHealer


class SafeAIHealer:

    def __init__(self, threshold=0.85):
        self.ai = AIHealer()
        self.threshold = threshold

    def heal(self, broken_text, candidates):

        result = self.ai.find_best_candidate(
            broken_text,
            candidates
        )

        print("\n========== AI RESULT ==========")
        print(result)
        print("===============================")

        best_match = re.search(
            r"BEST:\s*(.+)",
            result
        )

        confidence_match = re.search(
            r"CONFIDENCE:\s*([0-9.]+)",
            result
        )

        if not best_match or not confidence_match:
            print("❌ Could not understand AI response")
            return None

        best_candidate = best_match.group(1).strip()
        confidence = float(
            confidence_match.group(1)
        )

        print("\n🛡️ SAFE HEALING:")

        if confidence >= self.threshold:

            print("✅ Healing accepted")
            print(f"Using candidate: {best_candidate}")
            print(f"Confidence: {confidence:.2f}")

            return best_candidate

        print("❌ Healing rejected")
        print(f"Confidence: {confidence:.2f}")

 
