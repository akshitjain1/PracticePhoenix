# Changelog

All meaningful changes to this project will be documented in this file.

## [2.0.0+1] - Sprint 23 (PracticePhoenix Mobile Android Platform Regeneration)

### Changed
- Regenerated the entire Android platform subsystem (`practicephoenix_mobile/android`) from the official Flutter Stable template compatible with Flutter 3.44.4 and Android SDK 36.
- Replaced legacy Groovy scripts (`build.gradle`, `settings.gradle`) with modern Kotlin DSL build scripts (`build.gradle.kts`, `settings.gradle.kts`, `app/build.gradle.kts`).
- Upgraded Gradle Wrapper distribution to `gradle-9.1.0-all.zip` in `android/gradle/wrapper/gradle-wrapper.properties` to meet Android Gradle Plugin 8.8+ requirements.
- Configured AndroidX and Jetifier enablement flags (`android.useAndroidX=true`, `android.enableJetifier=true`) inside `android/gradle.properties`.
- Disabled cross-drive Kotlin incremental compilation (`kotlin.incremental=false`, `kotlin.incremental.useClasspathSnapshot=false`) in `android/gradle.properties` to eliminate Windows drive root mismatch exceptions during concurrent compilation.
- Preserved custom dark Phoenix crest launcher vector drawables (`ic_launcher_background.xml` & `ic_launcher_foreground.xml`) and launch background drawable (`launch_background.xml`).
- Verified 100% clean validation sequence: `flutter clean`, `flutter pub get`, `flutter analyze` (`No issues found!`), `flutter build apk --debug`, and `flutter build apk --release` (`49.6MB`). Zero Dart source files modified.

---

## [2.0.0+1] - Sprint 22 (PracticePhoenix Mobile Production Stabilization)

### Fixed
- Migrated `CardTheme` to `CardThemeData` in `lib/core/theme/app_theme.dart` to satisfy Flutter 3.44 type assignability rules.
- Renamed property lookup from `estimated_study_time` to `estimatedStudyTime` in `lib/features/home/home_screen.dart` matching `WelcomeDashboardModel` getter definitions.
- Resolved closure syntax mistakes in `_nextStep()` and `_prevStep()` of `lib/features/session/session_wizard_screen.dart` (`setState(() { ... });`).
- Eliminated constructor parameter warnings and unused import diagnostics in `lib/services/backend_service.dart`.
- Achieved certified zero-issue static analysis status (`No issues found!` via `flutter analyze`).

### Changed
- Migrated Android application infrastructure completely from deprecated Android v1 embedding to Android V2 embedding.
- Generated standard plugin loader configuration in `android/settings.gradle` and root project structure in `android/build.gradle`.
- Created `android/app/build.gradle` defining namespace `com.practicephoenix.mobile` and SDK compilation parameters.
- Created `android/app/src/main/kotlin/com/practicephoenix/mobile/MainActivity.kt` extending `io.flutter.embedding.android.FlutterActivity`.
- Updated `android/app/src/main/AndroidManifest.xml` referencing clean activity names and embedding version metadata (`flutterEmbedding=2`).

---

## [2.0.0-alpha] - Sprint 21 (PracticePhoenix Mobile Production APK & Real Device Alpha)

### Added
- Prepared mobile application codebase for release APK generation (`flutter build apk --release`) and physical Android device usage (`version: 2.0.0+1`).
- Implemented persistent SharedPreferences backend configuration (`ConfigService`), enabling immediate switching between Android Emulator (`http://10.0.2.2:8000`) and physical LAN IP testing (`http://192.168.1.100:8000`) without restarting the app.
- Added a live server connection diagnostic indicator in Settings consuming `GET /health` with auto-refresh capabilities to verify local network bridges.
- Created minimal dark Splash Screen (`SplashScreen`) displaying PracticePhoenix branding and motto ("Become 1% Better Every Day"), initializing local preferences before automatically navigating to the main interface.
- Packaged custom vector XML drawable resources (`ic_launcher_background.xml` & `ic_launcher_foreground.xml`) providing a dark Phoenix star crest launcher icon.
- Polished spacing, padding, typography, error cards, and retry triggers across all bottom navigation tabs.
- Verified via updated widget test suite (`test/widget_test.dart`) and 100% green Python FastAPI integration test suite (`pytest`).

---

## [2.0.0-alpha1] - Sprint 20 (PracticePhoenix Mobile Daily Session UI & APK Alpha)

### Added
- Replaced all raw JSON rendering views in `SessionScreen`, `RevisionScreen`, and `ProgressScreen` with polished Material 3 dark interactive cards.
- Built an 18-step sequential Morning Session wizard (`SessionWizardScreen`) occupying one screen per section with top `ProgressStepper` (`Step X of Y`), back navigation, and continue actions covering Welcome, News, Read Aloud, Executive Comm, HR STAR, 9 Technical FAANG subjects, Spaced Repetition, and Today's Mission deliverables.
- Created 10 requested reusable widgets under `lib/widgets/custom_cards.dart`: `SectionHeader`, `SectionCard`, `QuestionCard`, `DefinitionCard`, `ExampleCard`, `InterviewCard`, `CodeBlockCard`, `MissionChecklist`, `ProgressStepper`, and `ContinueButton`.
- Implemented local persistence and offline fallback using `SharedPreferences` (`CacheService`), ensuring study sessions load instantly and function gracefully during offline network conditions.
- Updated Flutter widget test suite (`test/widget_test.dart`) to verify custom card rendering and zero JSON debugging leakage.
- Verified Python FastAPI backend integration test suite (`pytest`) confirming 100% contract stability across all consumed REST endpoints.

---

## [2.0.0-beta2] - Sprint 19 (PracticePhoenix Mobile Flutter Foundation)

### Added
- Created complete production-grade Flutter application project foundation (`practicephoenix_mobile/`) adhering to Feature-First Clean Architecture, Riverpod State Management, GoRouter Navigation, Dio Networking, and Material 3 Dark Theme.
- Added core networking infrastructure under `lib/core/network/` (`ApiClient`, `BaseRepository`, `ErrorHandler`, `ResponseParser`) with multi-environment support (`AppConfig.devBaseUrl = 'http://10.0.2.2:8000'`).
- Created real Dart data models matching backend FastAPI JSON contracts: `DailyBriefModel`, `RevisionResponseModel`, and `ProgressResponseModel` without dummy or mocked models.
- Implemented Bottom Navigation shell (`BottomNavScaffold`) with exactly 4 tabs: Home, Revision, Progress, and Settings.
- Designed exact Home Screen UI layout (`HomeScreen`) with greeting, current streak, today's focus, estimated study time, large `START TODAY'S SESSION` button, revision due, and continue yesterday elements.
- Implemented shell feature screens (`SessionScreen`, `RevisionScreen`, `ProgressScreen`) executing real HTTP requests (`GET /session/today`, `GET /revision`, `GET /progress`) via Dio and displaying clean Loading, Success, and Error states.
- Created widget test suite (`test/widget_test.dart`) verifying layout hierarchy and navigation targets.

---

## [2.0.0-beta1] - Sprint 18 (PracticePhoenix Mobile Backend API Layer)

### Added
- Added `fastapi==0.115.11` and `uvicorn==0.34.0` to `requirements.txt`.
- Created FastAPI REST application root (`app/api/main.py`) configured with `CORSMiddleware` (`allow_origins=["*"]`) for mobile dev and interactive OpenAPI documentation at `/docs`.
- Created modular REST endpoint routers under `app/api/routes/` wrapping existing production services without business logic duplication:
  - `health.py`: `GET /health` -> Returns `HealthStatus` from `HealthService`.
  - `session.py`: `GET /session/today` -> Returns `DailyBrief` from `DailyService`.
  - `revision.py`: `GET /revision` -> Returns pending counts and due topics from `RevisionService`.
  - `progress.py`: `GET /progress` -> Returns completion metrics from `ProgressService`.
  - `history.py`: `GET /history` -> Returns archived briefs from `HistoryService`.
  - `analytics.py`: `GET /analytics` -> Returns weakness rankings and interaction totals from `AnalyticsService`.
  - `roadmap.py`: `GET /roadmap` -> Returns remaining lessons and estimated study days from `ProgressService`.
  - `interview.py`: `GET /interview/question` & `POST /interview/answer` -> Orchestrates adaptive interview session loops via `InterviewService`.
- Created API integration test suite (`tests/test_api_layer.py`) utilizing FastAPI `TestClient` to verify HTTP contracts across all 9 endpoints.
- Certified 100% green pass rate across 41 total unit and integration tests (`pytest`).

---

## [2.0.0-alpha1] - Sprint 17 (Morning Experience Opening Subsystem)

### Added
- Extended `app/ai/schemas/daily_schema.py` adding `WelcomeDashboard`, `NewsSection`, `PronunciationWord`, `ReadAloudSection`, and `HRSection` Pydantic models while guaranteeing backward compatibility.
- Created modular section generators (`NewsGenerator`, `ReadAloudGenerator`, `HRGenerator`) and visual card formatting.

---

## [2.0.0-design] - Sprint 16 (PracticePhoenix v2.0 Product Design Sprint)

### Added
- Created `PRODUCT_VISION.md`, `MORNING_SESSION.md`, `ARCHITECTURE_v2.md`, `CONTENT_GUIDELINES.md`, and `ROADMAP_v2.md`.

---

## [1.2.0] - Sprint 15 (Final Production Stabilization Subsystem)

### Added
- Created `app/utils/message_chunker.py` (`MessageChunker`) and enabled native API structured JSON output mode (`response_format={"type": "json_object"}`).
