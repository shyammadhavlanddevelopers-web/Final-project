from fastapi import FastAPI
from routes import properties, services, auth

app = FastAPI(title="Real Estate Website API")

app.include_router(properties.router)
app.include_router(services.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"msg": "Real Estate API running!"}
