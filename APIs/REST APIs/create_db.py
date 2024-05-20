#This is created because I attempted to use functionality that needed the current applications outside of the app
from app import app, db

with app.app_context():
    db.create_all()
    print("Database tables created!")