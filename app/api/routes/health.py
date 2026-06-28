from fastapi import APIRouter
from app.services.health_service import HealthService, HealthStatus


router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthStatus)
def get_health():
    """Orchestrates HealthService to return complete system diagnostics."""
    service = HealthService()
    return service.check_health()
