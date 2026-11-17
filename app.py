from flask import Flask, request, send_from_directory, jsonify
import numpy as np
import pickle
from pathlib import Path
import sklearn
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
templates = BASE_DIR / "templates"
with open(BASE_DIR/"LR.pkl",'rb') as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return send_from_directory(templates,"index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    height = float(data['height'])
    pred = model.predict(np.array([[height]]))
    return jsonify({"predicted_weight":round(float(pred[0]),2)})

if __name__ == "__main__":
    app.run(debug=True)

