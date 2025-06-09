# in app.py or main.py
from flask import Flask

app = Flask(__name__)

@app.route("/api/activities/home")
def home():
    return jsonify({"activities": ["Activity 1", "Activity 2"]})






