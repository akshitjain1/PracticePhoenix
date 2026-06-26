# Changelog

All meaningful changes to this project will be documented in this file.

## [1.0.0] - Sprint 13 (Release Candidate Validation & General Availability)

### Added
- Created `RELEASE_NOTES_v1.0.0.md` General Availability release announcement documenting full engineering scope and operational hardening.
- Created `PERFORMANCE.md` baselining application startup latency (`420ms`), LLM generation wall clock (`18.4s`), scheduler overhead (`85ms`), and container steady-state RAM (`~70MB`).
- Created `TROUBLESHOOTING.md` diagnostic runbook solving polling conflicts, rate limits, SQLite locks, and cron misfires.
- Created `.dockerignore` excluding virtual environments and test caches from Docker build contexts.
- Created `tests/test_rc_validation.py` simulating database backup restoration lifecycles, corrupt curriculum JSON parsing traps, and database connection heartbeats.
- Executed dependency audit and certified 100% green pass rate across 23 unit tests (`pytest`).
- Updated `README.md`, `PROJECT_STATE.md`, and `CHANGELOG.md` for official v1.0.0 GA certification.

---

## [0.9.0] - Sprint 12 (Production Deployment Engineering Subsystem)

### Added
- Containerized Docker setup, CI automation, and host runbooks.

---

## [0.8.0] - Sprint 11 (Production Hardening Subsystem)

### Added
- Diagnostics, `/health` endpoint, hot backups, and job idempotency.
