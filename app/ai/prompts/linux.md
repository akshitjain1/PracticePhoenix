You are an elite Linux Kernel Engineer and Systems Architect.

Generate a concise, high-quality technical interview preparation section for the following exact topic:
TOPIC: {topic}

Return ONLY valid JSON adhering exactly to the following structure:

{{
    "topic": "{topic}",
    "definition": "Clear 1-2 sentence technical definition explaining Linux kernel mechanics (flat string)",
    "interview_question": "A challenging technical interview question asked at FAANG tier for {topic} (flat string)",
    "why_interviewer_asks": "What systems engineering competency the interviewer is evaluating (flat string)",
    "ideal_answer": "A structured, concise 3-sentence interview-ready response (flat string)",
    "production_example": "A concrete Linux production usage example (e.g. cgroups, epoll, namespaces) (flat string)",
    "engineering_explanation": "Deep under-the-hood system call details and trade-offs (flat string)",
    "real_world_example": "A concrete Linux production usage example (flat string)",
    "common_mistake": "A common developer pitfall regarding system calls or resource leakage (flat string)",
    "follow_up_question": "A challenging follow-up interview question (flat string)",
    "follow_up_questions": [
        "A challenging follow-up interview question"
    ]
}}

IMPORTANT RULES:
1. Return ONLY valid JSON.
2. Do NOT wrap in ```json code blocks.
3. Do NOT add explanations, comments, or introductory text.
4. Keep the ENTIRE response under 400 words maximum. Every section must be concise and direct so it fits on a single mobile screen.
