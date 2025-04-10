
from flask import Flask, render_template, request, jsonify
import os
from resume_parser import parse_resume
from job_matcher import match_resume_to_job

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']
    job_description = request.form['job_description']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    parsed_resume = parse_resume(filepath)
    score = match_resume_to_job(parsed_resume, job_description)

    return jsonify({
        'score': round(score * 100, 2),
        'parsed_resume': parsed_resume
    })

if __name__ == '__main__':
    app.run(debug=True)
