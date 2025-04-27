"""Chapter 6: SQLAlchemy migration with Flask Migrate"""

# pip install virtualenv
# virtualenv venv
# venv/Scripts/activate (for windows)
# source venv/bin/activate (for linux/macOS)

# pip install flask flask-restx python-decouple flask-sqlalchemy flask-cors flask-jwt-extended flask-migrate
from flask import Flask
from flask_cors import CORS
from config import DevConfig
from database.exts import db
from flask_migrate import Migrate
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
Migrate(app, db, directory="database/migrations")
# ====================== FLASK MIGRATE COMMANDS =========================
# Set Flask app first
# $env:FLASK_APP = "main.py" (in powershell)
# set FLASK_APP=main.py (in command prompt)
# export FLASK_APP=main.py (in Linux/macOS)
# flask db init                   -> Create migrations folder (only once)
# flask db migrate -m "<message>" -> Create migration scripts
# flask db upgrade                -> Apply changes to the database
# flask db downgrade              -> Rollback to previous version
# =======================================================================


@app.route("/")
def home():
    return "Hello world from IG Tech Team"


@api.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello world from hello resource."}


if __name__ == "__main__":
    app.run(debug=True)
