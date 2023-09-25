from flask import Flask, request, render_template, jsonify
import pickle

# load model
with open('model_xgbr.pkl', "rb") as file:
    model = pickle.load(file)

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=["GET"])
def index():
    return render_template("googleplaystore.html")


@app.route("/predict", methods=["GET"])
def predict_success():

    reviews = int(request.args.get("reviews"))
    type = int(request.args.get("type"))
    price = float(request.args.get("price"))
    rating = float(request.args.get("rating"))

    installs = int(abs(model.predict([[reviews, type, price, rating]])))
    return f"Installs = {str(installs)}"

app.run( host="0.0.0.0", port=8080)

