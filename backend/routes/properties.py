from fastapi import APIRouter

router = APIRouter(prefix="/properties", tags=["Properties"])

@router.get("/")
def list_properties():
    return [
        {"id": 1, "title": "3BHK Apartment", "price": 4500000},
        {"id": 2, "title": "Villa with Garden", "price": 12500000},
    ]
