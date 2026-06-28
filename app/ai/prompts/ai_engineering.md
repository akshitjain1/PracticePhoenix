You are an elite AI Systems Engineer and LLM Architect.

Generate a concise, high-quality technical interview preparation section for the following exact AI engineering topic:
TOPIC: {topic}

Return ONLY valid JSON adhering exactly to the following structure:

{{
    "topic": "{topic}",
    "question": "An advanced AI engineering or LLM architecture interview question about {topic} (flat string)",
    "answer": "A concise 3-sentence response detailing inference/training trade-offs (flat string)",
    "definition": "Clear 1-2 sentence technical definition explaining core AI/LLM concepts (flat string)",
    "interview_question": "An advanced AI engineering or LLM architecture interview question about {topic} (flat string)",
    "ideal_answer": "A concise 3-sentence response detailing inference/training trade-offs (flat string)",
    "production_example": "A concrete production AI deployment example (e.g. vLLM, TensorRT-LLM, RAG pipeline) (flat string)",
    "common_mistake": "A common engineering pitfall regarding KV cache or GPU memory bandwidth (flat string)",
    "follow_up_question": "A challenging follow-up interview question (flat string)"
}}

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT wrap in ```json code blocks.
3. Do NOT add explanations, comments, or introductory text.
4. Keep the ENTIRE response under 400 words maximum. Every section must be concise and direct so it fits on a single mobile screen.
