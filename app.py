from flask import Flask, request, render_template
import numpy as np
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


with open("LR.pkl",'rb') as f:
    model = pickle.load(f)

@app.route("/")
def default_site():
    return render_template("index.html",predicted_weight=None)

@app.route("/predict", methods=["GET","POST"])
def predict():
    height = float(request.form["height"])
    data = np.array([[height]])

    pred = model.predict(data)[0]
    return render_template("index.html",predicted_weight=pred)

if __name__ == "__main__":
    app.run(debug=True)

