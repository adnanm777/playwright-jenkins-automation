
from healing.ai_healer import AIHealer
import re


ai = AIHealer()

broken_text = "XYZ completely different text"

candidates = [
    "Build your own cheap computer",
    "Build your own computer",
    "Simple Computer",
    "Register"
]

result = ai.find_best_candidate(
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

if best_match and confidence_match:

    best_candidate = best_match.group(1).strip()
    confidence = float(
        confidence_match.group(1)
    )

    print("\n🛡️ SAFE HEALING:")

    if confidence >= 0.85:

        print("✅ Healing accepted")
        print(f"Using candidate: {best_candidate}")
        print(f"Confidence: {confidence:.2f}")

    else:

        print("❌ Healing rejected")
        print(f"Confidence: {confidence:.2f}")

else:

    print("❌ Could not understand AI response")
