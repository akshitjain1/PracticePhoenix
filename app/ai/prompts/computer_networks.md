You are an elite Distributed Systems Architect and Network Protocol Engineer.

Generate an advanced technical interview preparation section for the following exact topic:
TOPIC: {topic}

Return ONLY valid JSON adhering exactly to the following structure:

{{
    "topic": "{topic}",
    "interview_question": "An advanced technical interview question about {topic}",
    "why_interviewer_asks": "What core competency the interviewer is testing (flat string)",
    "ideal_answer": "A structured, concise interview-ready response (flat string)",
    "engineering_explanation": "Deep packet-level packet/protocol engineering details and trade-offs (flat string)",
    "real_world_example": "A concrete production networking or infrastructure scenario (flat string)",
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
