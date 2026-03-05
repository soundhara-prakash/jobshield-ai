from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

# Load model
model = pickle.load(open("../model/model.pkl", "rb"))
vectorizer = pickle.load(open("../model/vectorizer.pkl", "rb"))

app = Flask(__name__)

# Enable CORS
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["text"]
    vectorized_text = vectorizer.transform([data])
    prediction = model.predict(vectorized_text)[0]
    proba = model.predict_proba(vectorized_text)[0]
    risk_score = max(proba)
    text_lower = data.lower()
    flagged_patterns = []
    if "registration fee" in text_lower:
        flagged_patterns.append("Registration Fee")
    if "whatsapp" in text_lower or "telegram" in text_lower:
        flagged_patterns.append("External Contact")
    if "earn" in text_lower or "daily income" in text_lower:
        flagged_patterns.append("Unrealistic Earnings")
    return jsonify({
        "prediction": prediction,
        "risk_score": float(risk_score),
        "flags": flagged_patterns
    })

if __name__ == "__main__":
    app.run(debug=True)