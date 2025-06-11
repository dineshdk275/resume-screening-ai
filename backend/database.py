from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resume_filename = db.Column(db.String(255), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    score = db.Column(db.Float, nullable=False)
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
