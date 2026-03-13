from fastapi import FastAPI

app = FastAPI()

alerts = []

@app.get("/")
def home():
    return {"message": "Real-Time IDS Running"}

@app.get("/alerts")
def get_alerts():
    return alerts