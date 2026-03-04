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

    return jsonify({
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)