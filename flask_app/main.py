from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route("/health", methods=["GET"])
def root():
    return "ok"