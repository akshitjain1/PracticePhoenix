from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health, session, revision, progress, history, analytics, roadmap, interview


app = FastAPI(
    title="PracticePhoenix Mobile API",
    description="FastAPI REST orchestration layer exposing production services for PracticePhoenix mobile and web applications.",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for Flutter localhost development and mobile emulators
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register endpoints
app.include_router(health.router)
app.include_router(session.router)
app.include_router(revision.router)
app.include_router(progress.router)
app.include_router(history.router)
app.include_router(analytics.router)
app.include_router(roadmap.router)
app.include_router(interview.router)
