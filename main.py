"""Chapter 1: Initialize Flask, create API documentation and dev database."""

# pip install virtualenv
# virtualenv venv
# venv/Scripts/activate (for windows)
# source venv/bin/activate (for linux/macOS)

# pip install flask flask-restx python-decouple flask-sqlalchemy
from flask import Flask
from config import DevConfig
from database.exts import db
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, doc="/docs", prefix="/api")

app.config.from_object(DevConfig)  # Load the DevConfig settings

# Initialize the database
db.init_app(app)


@app.route("/")
def home():
    return "Hello world from IG Tech Team"


@api.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello world from hello resource."}


if __name__ == "__main__":
    app.run(debug=True)
