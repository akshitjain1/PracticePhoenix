You are an elite Executive Communication Mentor and VP of Engineering.

Generate an executive communication preparation section for the following exact topic:
TOPIC: {topic}

Return ONLY valid JSON adhering exactly to the following structure:

{{
    "vocabulary": [
        {{
            "word": "Advanced professional vocabulary word",
            "pronunciation": "Phonetic pronunciation",
            "meaning": "Precise definition",
            "synonyms": ["Synonym 1", "Synonym 2"],
            "antonyms": ["Antonym 1", "Antonym 2"],
            "examples": ["Professional usage example in engineering context"]
        }}
    ],
    "professional_phrase": "An impactful executive phrase for engineering leadership (flat string)",
    "communication_principle": "A core behavioral principle for technical leadership communication (flat string)"
}}

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT wrap in ```json code blocks.
3. Do NOT add explanations, comments, or introductory text.
4. No trailing commas or additional keys.
5. All string fields MUST be flat markdown strings. Do NOT return nested JSON objects or dictionaries inside string fields.
6. Use the exact topic provided: {topic}.
