from fastapi import FastAPI
from app.agent import run_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Festiva Planner AI running"}

@app.get("/plan")
def plan_event(query: str):
    result = run_agent(query)
    return result