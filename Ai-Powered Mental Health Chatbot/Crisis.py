from typing import List

# FIX: Was `KRISIS_KEYWORDS: List[str] = [...]` but written as
#      `KRISIS_KEYWORDS = List[str] = [...]` (double assignment = SyntaxError).
#      Also renamed to CRISIS_KEYWORDS for clarity; old name kept as alias.
CRISIS_KEYWORDS: List[str] = [
    "suicide", "suicidal", "kill myself", "want to die", "end my life",
    "can't go on", "no reason to live",
    "hopeless", "worthless", "alone", "depressed"
]
KRISIS_KEYWORDS = CRISIS_KEYWORDS  # backward-compat alias

SAFETY_MESSAGE = (
    "It sounds like you're going through a really tough time."
    " Remember that you're not alone, and there are people who care about you and want to help."
    " It might be helpful to reach out to a trusted friend, family member, or mental health professional to talk about how you're feeling. You're important, "
    "and there are resources available to support you.\n\n"
    "Please consider reaching out to a mental health professional or contacting a helpline:\n\n"
    "**India:** 9152987821 (iCall) | 1800-599-0019 (Vandrevala Foundation)\n\n"
    "**USA:** 988 (Suicide & Crisis Lifeline)\n\n"
    "**UK:** 116 123 (Samaritans)\n\n"
)


def contains_crisis_keywords(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)
