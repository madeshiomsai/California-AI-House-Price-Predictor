from flask import Flask, render_template, request
import joblib
import numpy as np

info = joblib.load("california_info.joblib")
model = info["model"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    v1 = float(request.form["a"])
    v2 = float(request.form["b"])
    v3 = float(request.form["c"])
    v4 = float(request.form["d"])
    v5 = float(request.form["e"])
    v6 = float(request.form["f"])

    arr = np.array([[v1, v2, v3, v4, v5, v6]])

    prediction = model.predict(arr)

    return render_template(
        "result.html",
        prediction=round(prediction[0], 2)
    )


if __name__ == "__main__":
    app.run(debug=True)