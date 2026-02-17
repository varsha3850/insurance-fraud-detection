from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    premium = float(request.form['premium'])
    claim = float(request.form['claim'])

    if claim > premium:
        result = "Fraud Claim"
    else:
        result = "Legitimate Claim"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
