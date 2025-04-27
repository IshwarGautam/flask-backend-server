<<<<<<< HEAD
"""Chapter 5: Implement login and sign up."""
=======
"""Chapter 4: Data validation with parser."""
>>>>>>> 5a6a1423a01c033dc1efb35c36bfb2ea438a690e

# pip install virtualenv
# virtualenv venv
# venv/Scripts/activate (for windows)
# source venv/bin/activate (for linux/macOS)

# pip install flask flask-restx python-decouple flask-sqlalchemy flask-cors flask-jwt-extended
from flask import Flask
from flask_cors import CORS
from config import DevConfig
from database.exts import db
from api.auth_routes import auth_ns
from api.user_routes import user_ns
from flask_restx import Api, Resource
from flask_jwt_extended import JWTManager
from api.employee_leave_routes import employee_leave_ns

app = Flask(__name__)
api = Api(app, doc="/docs", prefix="/api")

api.add_namespace(user_ns)
api.add_namespace(auth_ns)
api.add_namespace(employee_leave_ns)

app.config.from_object(DevConfig)  # Load the DevConfig settings

# Allow CORS for all routes and all origins
CORS(app)

# Initialize the database
db.init_app(app)

JWTManager(app)


@app.route("/")
def home():
    return "Hello world from IG Tech Team"


@api.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello world from hello resource."}


if __name__ == "__main__":
    app.run(debug=True)
