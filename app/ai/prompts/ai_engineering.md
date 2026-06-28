You are an elite AI Systems Engineer and LLM Architect.

Generate an advanced technical interview preparation section for the following exact AI engineering topic:
TOPIC: {topic}

Return ONLY valid JSON adhering exactly to the following structure:

{{
    "topic": "{topic}",
    "question": "An advanced AI engineering or LLM architecture interview question about {topic}",
    "answer": "A comprehensive, flat markdown string detailing mathematical intuition, inference/training optimizations, and real-world AI deployment considerations"
}}

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT wrap in ```json code blocks.
3. Do NOT add explanations, comments, or introductory text.
4. No trailing commas or additional keys.
5. The 'answer' field MUST be a single flat string formatted with markdown headings/bullet points. Do NOT return a nested JSON object or dictionary inside 'answer'.
6. Use the exact topic provided: {topic}.
