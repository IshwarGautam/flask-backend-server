from main import app
from database.exts import db

with app.app_context():
    db.create_all()
    print("Database created!")

# create database by running `python -m database.db_init` (it will treat database directory as a module)
