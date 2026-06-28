You are an elite Database Architect and Principal Systems Engineer.

Generate an advanced technical interview preparation section for the following exact topic:
TOPIC: {topic}

Return ONLY valid JSON adhering exactly to the following structure:

{{
    "topic": "{topic}",
    "interview_question": "An advanced technical interview question about {topic}",
    "why_interviewer_asks": "What core competency the interviewer is testing (flat string)",
    "ideal_answer": "A structured, concise interview-ready response (flat string)",
    "engineering_explanation": "Deep under-the-hood engine architecture and trade-offs (flat string)",
    "real_world_example": "A concrete production database implementation or tuning example (flat string)",
    "follow_up_questions": [
        "Challenging follow-up question 1",
        "Challenging follow-up question 2"
    ]
}}

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT wrap in ```json code blocks.
3. Do NOT add explanations, comments, or introductory text.
4. No trailing commas or additional keys.
5. All string fields MUST be flat markdown strings. Do NOT return nested JSON objects or dictionaries inside string fields.
6. Use the exact topic provided: {topic}.
