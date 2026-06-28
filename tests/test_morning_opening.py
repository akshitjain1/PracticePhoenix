import pytest
from app.ai.schemas.daily_schema import (
    DailyBrief, WelcomeDashboard, NewsSection, ReadAloudSection, HRSection,
    ExecutiveCommunication, VocabularyWord, CSSection, BackendSection, AISection, DSASection, EngineeringInsight
)
from app.services.generators.news_generator import NewsGenerator
from app.services.generators.read_aloud_generator import ReadAloudGenerator
from app.services.generators.hr_generator import HRGenerator
from app.services.generators.exec_comm_generator import ExecutiveCommunicationGenerator
from app.ai.formatter import TelegramFormatter


def test_opening_schemas_defaults():
    welcome = WelcomeDashboard()
    assert welcome.day_number == 1
    assert welcome.estimated_study_time == 25
    assert "System Architecture" in welcome.todays_focus

    news = NewsSection()
    assert "EEVDF" in news.summary

    read_aloud = ReadAloudSection()
    assert "Stampede" in [pw.word for pw in read_aloud.pronunciation_words]

    hr = HRSection()
    assert "Situation" in hr.star_framework or "STAR" in hr.star_framework


def test_opening_generators_fallback():
    news_gen = NewsGenerator()
    news = news_gen.run("Microservices")
    assert "microservice" in news.summary.lower() or "linux" in news.summary.lower() or "istio" in news.summary.lower()

    read_aloud_gen = ReadAloudGenerator()
    read_aloud = read_aloud_gen.run("Caching")
    assert "cache" in read_aloud.paragraph.lower() or "caching" in read_aloud.paragraph.lower() or "system" in read_aloud.paragraph.lower()

    hr_gen = HRGenerator()
    hr = hr_gen.run("Ownership")
    assert "ownership" in hr.behavioral_question.lower() or "decision" in hr.behavioral_question.lower() or "time" in hr.behavioral_question.lower()

    exec_gen = ExecutiveCommunicationGenerator()
    exec_comm = exec_gen.run("Resilience")
    assert hasattr(exec_comm, "interview_sentence")
    assert hasattr(exec_comm, "daily_usage_challenge")


def test_telegram_formatter_opening_experience():
    brief = DailyBrief(
        welcome_dashboard=WelcomeDashboard(day_number=15, current_streak=15, curriculum_progress=72.5),
        news_section=NewsSection(summary="Important tech release", why_it_matters="Boosts velocity", interview_relevance="System design concept"),
        read_aloud_section=ReadAloudSection(),
        hr_section=HRSection(),
        executive_communication=ExecutiveCommunication(
            vocabulary=[VocabularyWord(word="Resilient", pronunciation="ri-zil-yuhnt", meaning="Robust", synonyms=[], antonyms=[], examples=[])],
            professional_phrase="Align on resilience",
            communication_principle="Be clear",
            interview_sentence="Built a resilient pipeline",
            daily_usage_challenge="Use resilient today"
        ),
        operating_systems=CSSection(topic="OS", interview_question="Q", why_interviewer_asks="Why", ideal_answer="A", engineering_explanation="Deep", real_world_example="Ex", follow_up_questions=[]),
        dbms=CSSection(topic="DB", interview_question="Q", why_interviewer_asks="Why", ideal_answer="A", engineering_explanation="Deep", real_world_example="Ex", follow_up_questions=[]),
        computer_networks=CSSection(topic="Net", interview_question="Q", why_interviewer_asks="Why", ideal_answer="A", engineering_explanation="Deep", real_world_example="Ex", follow_up_questions=[]),
        backend=BackendSection(topic="Back", question="Q", answer="A"),
        ai_engineering=AISection(topic="AI", question="Q", answer="A"),
        dsa=DSASection(problem="Prob", pattern="Pat", complexity="Comp"),
        engineering_insight=EngineeringInsight(title="Insight", description="Desc")
    )

    formatter = TelegramFormatter()
    output = formatter.format(brief)

    assert "🚀 *Daily Preparation Brief* | PracticePhoenix v2.0" in output
    assert "🌅 *WELCOME DASHBOARD*" in output
    assert "*Day Number:* 15 | *Current Streak:* 15 Days" in output
    assert "📰 *1. ENGINEERING NEWS*" in output
    assert "Important tech release" in output
    assert "📖 *2. READ ALOUD ARTICULATION*" in output
    assert "👔 *4. HR & BEHAVIORAL INTERVIEW (STAR)*" in output
    assert "## 💻 Operating Systems" in output
