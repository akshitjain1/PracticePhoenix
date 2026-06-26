from concurrent.futures import ThreadPoolExecutor
from app.ai.schemas.daily_schema import DailyBrief
from app.services.learning_engine import LearningEngine
from app.services.coaching_service import CoachingService
from app.services.generators.ai_generator import AIEngineeringGenerator
from app.services.generators.backend_generator import BackendGenerator
from app.services.generators.cs_generator import CSSectionGenerator
from app.services.generators.dsa_generator import DSAGenerator
from app.services.generators.exec_comm_generator import ExecutiveCommunicationGenerator
from app.services.generators.insight_generator import EngineeringInsightGenerator
from app.utils.logger import app_logger


class DailyService:

    def __init__(self):
        self.learning_engine = LearningEngine()
        self.curriculum = self.learning_engine.curriculum

    def generate_daily_brief(self) -> DailyBrief:
        app_logger.info("Orchestrating modular section generators and Personal Coaching for Daily Brief...")
        plan = self.learning_engine.get_today_plan()

        exec_comm_gen = ExecutiveCommunicationGenerator()
        os_gen = CSSectionGenerator("operating_systems.md")
        dbms_gen = CSSectionGenerator("dbms.md")
        cn_gen = CSSectionGenerator("computer_networks.md")
        backend_gen = BackendGenerator()
        ai_gen = AIEngineeringGenerator()
        dsa_gen = DSAGenerator()
        insight_gen = EngineeringInsightGenerator()
        coaching_service = CoachingService()

        with ThreadPoolExecutor(max_workers=10) as executor:
            f_exec = executor.submit(exec_comm_gen.run, plan.topics["communication"].topic)
            f_os = executor.submit(os_gen.run, plan.topics["operating_systems"].topic)
            f_dbms = executor.submit(dbms_gen.run, plan.topics["dbms"].topic)
            f_cn = executor.submit(cn_gen.run, plan.topics["computer_networks"].topic)
            f_backend = executor.submit(backend_gen.run, plan.topics["backend"].topic)
            f_ai = executor.submit(ai_gen.run, plan.topics["ai_engineering"].topic)
            f_dsa = executor.submit(dsa_gen.run, plan.topics["dsa"].topic)
            f_insight = executor.submit(insight_gen.run, plan.topics["engineering_insight"].topic)
            f_coaching = executor.submit(coaching_service.generate_coaching_advice)

            brief = DailyBrief(
                executive_communication=f_exec.result(),
                operating_systems=f_os.result(),
                dbms=f_dbms.result(),
                computer_networks=f_cn.result(),
                backend=f_backend.result(),
                ai_engineering=f_ai.result(),
                dsa=f_dsa.result(),
                engineering_insight=f_insight.result(),
                personal_coaching=f_coaching.result(),
            )

        self.learning_engine.complete_today()
        app_logger.info("Daily Brief assembled successfully with coaching and spaced repetitions.")
        return brief