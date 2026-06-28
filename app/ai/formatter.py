from app.ai.schemas.daily_schema import DailyBrief


class TelegramFormatter:

    def format(self, brief: DailyBrief) -> str:
        message = []

        message.append("🚀 *Daily Preparation Brief* | PracticePhoenix v2.0")
        message.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        message.append("🌅 *WELCOME DASHBOARD*")
        message.append(f"🔥 *Day Number:* {brief.welcome_dashboard.day_number} | *Current Streak:* {brief.welcome_dashboard.current_streak} Days")
        message.append(f"📊 *Curriculum Progress:* {brief.welcome_dashboard.curriculum_progress:.1f}% Completed")
        message.append(f"⏱️ *Estimated Study Duration:* {brief.welcome_dashboard.estimated_study_time} Minutes ({brief.welcome_dashboard.difficulty})")
        message.append(f"🎯 *Today's Focus:* {brief.welcome_dashboard.todays_focus}")
        message.append("")

        message.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        message.append("📰 *1. ENGINEERING NEWS*")
        message.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        message.append(f"• *Summary:* {brief.news_section.summary}")
        message.append(f"• *Why it matters:* {brief.news_section.why_it_matters}")
        message.append(f"• *Interview relevance:* {brief.news_section.interview_relevance}")
        message.append("")

        message.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        message.append("📖 *2. READ ALOUD ARTICULATION*")
        message.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        message.append(f"• *Technical Paragraph:* \"{brief.read_aloud_section.paragraph}\"")
        if brief.read_aloud_section.pronunciation_words:
            message.append("• *Target Pronunciation Words:*")
            for pw in brief.read_aloud_section.pronunciation_words:
                message.append(f"  - {pw.word} [{pw.pronunciation}]")
        message.append(f"• *Speaking Challenge:* {brief.read_aloud_section.speaking_challenge}")
        message.append("")

        message.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        message.append("## 💼 Executive Communication")
        for vocab in brief.executive_communication.vocabulary:
            message.append(f"• *{vocab.word}* ({vocab.pronunciation}): {vocab.meaning}")
        message.append(f"*Phrase:* \"{brief.executive_communication.professional_phrase}\"")
        message.append(f"*Principle:* {brief.executive_communication.communication_principle}")
        if getattr(brief.executive_communication, "interview_sentence", ""):
            message.append(f"*Interview Sentence:* \"{brief.executive_communication.interview_sentence}\"")
        if getattr(brief.executive_communication, "daily_usage_challenge", ""):
            message.append(f"*Daily Challenge:* {brief.executive_communication.daily_usage_challenge}")
        message.append("")

        message.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        message.append("👔 *4. HR & BEHAVIORAL INTERVIEW (STAR)*")
        message.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        message.append(f"• *Behavioral Question:* \"{brief.hr_section.behavioral_question}\"")
        message.append(f"• *Why Interviewer Asks:* {brief.hr_section.why_interviewer_asks}")
        message.append(f"• *STAR Breakdown:* {brief.hr_section.star_framework}")
        message.append(f"• *Sample Answer:* \"{brief.hr_section.sample_answer}\"")
        message.append(f"• *Common Mistakes:* {brief.hr_section.common_mistakes}")
        message.append(f"• *Practice Task:* {brief.hr_section.practice_task}")
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