from app.ai.schemas.daily_schema import DailyBrief


class TelegramFormatter:

    def format(self, brief: DailyBrief) -> str:
        message = []

        message.append("🚀 *Daily Preparation Brief*")
        message.append("")

        # 1. Executive Communication
        message.append("## 💼 Executive Communication")
        for vocab in brief.executive_communication.vocabulary:
            message.append(f"• *{vocab.word}* ({vocab.pronunciation}): {vocab.meaning}")
        message.append(f"*Phrase:* \"{brief.executive_communication.professional_phrase}\"")
        message.append(f"*Principle:* {brief.executive_communication.communication_principle}")
        message.append("")

        # 2. Operating Systems
        message.append("## 💻 Operating Systems")
        message.append(f"*Topic:* {brief.operating_systems.topic}")
        message.append(f"*Q:* {brief.operating_systems.interview_question}")
        message.append(f"*Ideal Answer:* {brief.operating_systems.ideal_answer}")
        message.append(f"*Deep Dive:* {brief.operating_systems.engineering_explanation}")
        message.append("")

        # 3. DBMS
        message.append("## 🗄️ DBMS")
        message.append(f"*Topic:* {brief.dbms.topic}")
        message.append(f"*Q:* {brief.dbms.interview_question}")
        message.append(f"*Ideal Answer:* {brief.dbms.ideal_answer}")
        message.append("")

        # 4. Computer Networks
        message.append("## 🌐 Computer Networks")
        message.append(f"*Topic:* {brief.computer_networks.topic}")
        message.append(f"*Q:* {brief.computer_networks.interview_question}")
        message.append(f"*Ideal Answer:* {brief.computer_networks.ideal_answer}")
        message.append("")

        # 5. Backend Engineering
        message.append("## ⚙️ Backend Engineering")
        message.append(f"*Topic:* {brief.backend.topic}")
        message.append(f"*Q:* {brief.backend.question}")
        message.append(f"*A:* {brief.backend.answer}")
        message.append("")

        # 6. AI Engineering
        message.append("## 🤖 AI Engineering")
        message.append(f"*Topic:* {brief.ai_engineering.topic}")
        message.append(f"*Q:* {brief.ai_engineering.question}")
        message.append(f"*A:* {brief.ai_engineering.answer}")
        message.append("")

        # 7. DSA
        message.append("## 🧠 DSA & Problem Solving")
        message.append(f"*Problem:* {brief.dsa.problem} ({brief.dsa.pattern})")
        message.append(f"*Complexity:* {brief.dsa.complexity}")
        message.append("")

        # 8. Engineering Insight
        message.append("## 💡 Engineering Wisdom")
        message.append(f"*{brief.engineering_insight.title}*")
        message.append(brief.engineering_insight.description)

        # 9. Personal Coaching
        if hasattr(brief, "personal_coaching") and brief.personal_coaching:
            message.append("")
            message.append("## 🎯 Personal Coaching")
            message.append(brief.personal_coaching)

        return "\n".join(message)