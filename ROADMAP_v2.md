# PracticePhoenix v2.0: Phased Implementation Roadmap

## Overview
This roadmap translates the product vision and architectural blueprints of PracticePhoenix v2.0 into a structured 5-phase engineering release schedule. Each phase delivers verifiable, production-grade milestones while maintaining zero regressions in existing stable serverless delivery workflows.

---

## Phase 1: Morning Session Redesign & Core Expansion
**Objective**: Expand the underlying data contract and generator ecosystem from 8 sections to the full 14-section v2.0 morning ritual.

### Engineering Deliverables
- **Schema Expansion**: Create `app/ai/schemas/daily_schema_v2.py` defining `BriefV2` and its 15 constituent domain models (`NewsSection`, `ReadAloudSection`, `HRSection`, `SystemDesignSection`, etc.).
- **Modular Generator Implementation**: Build out the 15 independent generator classes in `app/services/generators/` inheriting from `BaseGenerator[T]`.
- **Orchestration Upgrade**: Update `DailyService.generate_daily_brief()` to execute 15 wave-parallel thread workers with isolated fallback wrappers (`_safe_resolve_v2`).
- **Formatter Modernization**: Upgrade `TelegramFormatter` to assemble the new visual card headers and sequential markdown breaks.

### Acceptance Criteria
- Full 14-section brief successfully generates within `< 20 seconds` wall clock time.
- Automated chunker splits output cleanly across sequential messages without markdown corruption.

---

## Phase 2: Content Quality & Strict Prompt Calibration
**Objective**: Enforce the strict quantitative and depth constraints defined in `CONTENT_GUIDELINES.md` across all LLM inference providers.

### Engineering Deliverables
- **Prompt Engineering**: Rewrite all 15 template files in `app/ai/prompts/` incorporating explicit word limits, anti-fluff rules, and mandatory "Three-Layer Rigor" instructions.
- **JSON Enforcement**: Ensure 100% adherence to native API `response_format={"type": "json_object"}` across Groq and Gemini gateways.
- **Fallback Library Tuning**: Expand offline fallback dictionaries to provide rich, production-grade answers during network disconnects.

### Acceptance Criteria
- Zero validation errors across 1,000 automated CI test runs.
- All generated sections conform exactly to target word budgets (`150-200` words per deep dive).

---

## Phase 3: Adaptive Personalization Engine
**Objective**: Dynamically tailor brief contents based on individual user interaction telemetry and historical revision performance.

### Engineering Deliverables
- **Telemetry Coupling**: Connect `ActivityRepository` and `RevisionRepository` directly into `DailyService` planning logic.
- **Dynamic Weighting**: Automatically assign extra deep-dive slots or harder algorithmic variations to domain tracks where the user's recall success rate drops below `75%`.
- **Adaptive Coaching**: Feed real-time streak trends and topic weakness analytics into `CoachGenerator` for hyper-personalized executive mentoring notes.

### Acceptance Criteria
- Users struggling with specific domains (e.g., Operating Systems) automatically receive targeted reinforcement in subsequent morning briefs.

---

## Phase 4: Voice Articulation & Audio Evaluation Mode
**Objective**: Introduce interactive voice processing to verify verbal articulation during Read Aloud and HR STAR practice tasks.

### Engineering Deliverables
- **Telegram Audio Handlers**: Implement webhook/polling listeners for `.ogg` voice notes sent to the bot.
- **Speech-to-Text Pipeline**: Integrate Whisper API transcription to convert user spoken recordings into raw text transcripts.
- **Articulation Evaluator**: Build an LLM evaluation service comparing student spoken transcripts against target pronunciation words and STAR structuring rules, returning instant vocal feedback scores.

### Acceptance Criteria
- Users can reply to the morning brief with a voice note and receive a structured critique within `5 seconds`.

---

## Phase 5: Omnichannel Web Dashboard Companion
**Objective**: Provide a rich visual companion interface for complex architectural graph navigation and desktop progress tracking.

### Engineering Deliverables
- **REST / GraphQL API**: Expose backend study history, analytics, and revision queues via secured FastAPI endpoints.
- **React / Next.js Frontend**: Build a responsive web dashboard visualizing compounding streak matrices, skill radar charts, and interactive Mermaid architecture diagrams.
- **Real-Time Sync**: Ensure study actions performed on Telegram reflect instantaneously on the web dashboard via WebSocket or polling updates.

### Acceptance Criteria
- Seamless cross-platform authentication and real-time state synchronization between mobile Telegram and web companion.
