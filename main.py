from fastapi import FastAPI

# Application initialize kar rahe hain
app = FastAPI(title="B2B Compliance API")

# Pehla route (Homepage)
@app.get("/")
def read_root():
    return {
        "status": "Online",
        "message": "B2B Contract & Compliance Audit Engine is Running!"
    }

# Health Check Route
@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "database": "Ready",
        "ai_engine": "Standby"
    }