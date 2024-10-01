import os
from extensions import db, app
from models import Participant
from sqlalchemy import inspect

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "a_secure_secret_key")

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database tables created successfully")
    inspector = inspect(db.engine)
    existing_tables = inspector.get_table_names()
    print("Tables in the database:", existing_tables)

from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
