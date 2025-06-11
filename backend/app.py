from flask import Flask, render_template, request
import os
from parser import extract_text
from matcher import match_resume
from database import db, Match, init_db

app = Flask(__name__)  # <-- Must be defined before using @app.route

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/resume_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'backend', 'uploads')

init_db(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']
    job_desc = request.form['job_desc']

    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    resume_text = extract_text(file_path)
    score = match_resume(resume_text, job_desc)

    match = Match(resume_filename=file.filename, job_description=job_desc, score=score)
    db.session.add(match)
    db.session.commit()

    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
