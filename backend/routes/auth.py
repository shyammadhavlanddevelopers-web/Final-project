from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/login")
def login():
    return {"msg": "Login route"}
