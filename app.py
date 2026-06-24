from flask import Flask, render_template, request
from model import predict_message, accuracy

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    confidence = 0
    category = ""
    reasons = []
    risk = ""
    urls = []

    if request.method == "POST":

        message = request.form["message"]

        result, confidence, category, reasons, risk, urls = predict_message(message)

        if result == "spam":
            prediction = "🚨 Spam Message"
        else:
            prediction = "✅ Safe Message"

    return render_template(
        "index.html",
        prediction=prediction,
        accuracy=accuracy,
        confidence=confidence,
        category=category,
        reasons=reasons,
        risk=risk,
        urls=urls
    )

if __name__ == "__main__":
    app.run(debug=True)