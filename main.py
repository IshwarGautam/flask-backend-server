"""Chapter 2: Create User API, table and routes."""

# pip install virtualenv
# virtualenv venv
# venv/Scripts/activate (for windows)
# source venv/bin/activate (for linux/macOS)

# pip install flask flask-restx python-decouple flask-sqlalchemy flask-cors
from flask import Flask
from flask_cors import CORS
from config import DevConfig
from database.exts import db
from api.user_routes import user_ns
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, doc="/docs", prefix="/api")

api.add_namespace(user_ns)

app.config.from_object(DevConfig)  # Load the DevConfig settings

# Allow CORS for all routes and all origins
CORS(app)

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
