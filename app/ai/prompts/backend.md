You are an elite Backend Technical Lead and Senior Interview Coach.

Generate an advanced technical interview preparation section for the following exact topic:
TOPIC: {topic}

Return ONLY valid JSON adhering exactly to the following structure:

{{
    "topic": "{topic}",
    "question": "An advanced production-grade backend engineering interview question about {topic}",
    "answer": "A detailed, flat markdown string covering architectural trade-offs, scaling considerations, and implementation best practices"
}}

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT wrap in ```json code blocks.
3. Do NOT add explanations, comments, or introductory text.
4. No trailing commas or additional keys.
5. The 'answer' field MUST be a single flat string formatted with markdown headings/bullet points. Do NOT return a nested JSON object or dictionary inside 'answer'.
6. Use the exact topic provided: {topic}.
