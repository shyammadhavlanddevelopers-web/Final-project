from fastapi import APIRouter

router = APIRouter(prefix="/services", tags=["Services"])

@router.get("/")
def list_services():
    return [
        {"id": 1, "title": "Construction Material Supply"},
        {"id": 2, "title": "House Repairing"},
        {"id": 3, "title": "Map Registration"},
    ]
