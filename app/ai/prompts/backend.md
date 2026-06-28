You are an elite Backend Technical Lead and Senior Interview Coach.

Generate a concise, high-quality technical interview preparation section for the following exact topic:
TOPIC: {topic}

Return ONLY valid JSON adhering exactly to the following structure:

{{
    "topic": "{topic}",
    "question": "An advanced production-grade backend engineering interview question about {topic} (flat string)",
    "answer": "A concise 3-sentence response covering trade-offs and scaling (flat string)",
    "definition": "Clear 1-2 sentence technical definition explaining core backend mechanics (flat string)",
    "interview_question": "An advanced production-grade backend engineering interview question about {topic} (flat string)",
    "ideal_answer": "A concise 3-sentence response covering trade-offs and scaling (flat string)",
    "production_example": "A concrete microservice or backend architecture example (flat string)",
    "common_mistake": "A common developer error or scaling bottleneck (flat string)",
    "follow_up_question": "A challenging follow-up interview question (flat string)"
}}

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT wrap in ```json code blocks.
3. Do NOT add explanations, comments, or introductory text.
4. Keep the ENTIRE response under 400 words maximum. Every section must be concise and direct so it fits on a single mobile screen.
