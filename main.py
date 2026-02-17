from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


from database.db import init_db, store_flagged_message, get_all_flagged
from security.metrics import update_metrics, get_metrics
from agent.reasoning_engine import analyze_message
from agent.intent_generator import generate_intents
from security.armor_plugin import enforce_intent
from agent.action_executor import execute_action

app = FastAPI()
templates = Jinja2Templates(directory="templates")
init_db()


class MessageRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Secure Scam Agent API is running"}


@app.post("/analyze")
def analyze(request: MessageRequest):

    user_input = request.message

    analysis = analyze_message(user_input)
    intents = generate_intents(user_input, analysis)

    results = []

    for intent in intents:
        approval = enforce_intent(intent)

        if approval["status"] == "approved":
            action_result = execute_action(intent)
        else:
            action_result = approval

        results.append({
            "intent": intent.model_dump(),
            "execution_result": action_result
        })

    # ✅ Update runtime metrics
    update_metrics(analysis, results)

    if analysis["risk_score"] >= 60:
        store_flagged_message(
            user_input,
            analysis["risk_score"],
            "Auto-flagged by secure agent"
        )


    return {
        "analysis": analysis,
        "actions": results
    }


@app.get("/metrics")
def metrics_dashboard():
    return get_metrics()

@app.get("/flagged")
def view_flagged():
    return get_all_flagged()

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "metrics": get_metrics(),
            "flagged": get_all_flagged()
        }
    )
