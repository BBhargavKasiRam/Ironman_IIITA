from transformers import pipeline
print("Loading ML model... Please wait.")
# Load model once at startup
classifier = pipeline("sentiment-analysis")

print("Model loaded successfully.")

def analyze_message(text: str):

    # Run model inference
    result = classifier(text)[0]

    label = result["label"]
    confidence = result["score"]

    risk_score = 0

    # Basic logic combining ML + heuristic
    if "otp" in text.lower():
        risk_score += 40

    if "urgent" in text.lower():
        risk_score += 20

    if label == "NEGATIVE":
        risk_score += int(confidence * 30)

    risk_score = min(risk_score, 100)

    if risk_score >= 70:
        classification = "Likely Scam"
    elif risk_score >= 40:
        classification = "Suspicious"
    else:
        classification = "Likely Safe"

    return {
        "classification": classification,
        "risk_score": risk_score,
        "ml_label": label,
        "ml_confidence": round(confidence, 2)
    }
