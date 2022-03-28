#!/opt/anaconda3/bin/python

import pandas as pd
import joblib
from flask import Flask, jsonify, request
import objects.DatabaseUtils as db
import numpy as np
import os

app = Flask(__name__)

dir = os.getcwd()

# Import trained model
log_reg = joblib.load(dir + "/" + "app" + "/" + "log_reg.pkl")


@app.route("/live", methods=["POST"])
def predict():
    data = request.json
    x = float(data["x"])
    y = float(data["y"])
    z = float(data["z"])
    pred = log_reg.predict(np.array([[x, y, z]]))

    if pred[0] == 1:
        return jsonify("Object in movement")
    return jsonify("No movement detected")


@app.route("/live-prediction", methods=["GET"])
def load_prediction():
    data_engine = db.database()

    try:
        df_live = data_engine.load(type="live")
    except:
        print("Something went wrong")

    log_reg_preds = log_reg.predict(df_live[["x", "y", "z"]])

    response = {}
    for idx, pred in enumerate(log_reg_preds):
        response[str(idx)] = str(pred)

    return response


if __name__ == "__main__":
    app.run(debug=True)
