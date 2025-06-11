# 🧠 AI-Based Resume Screening System

This is a Flask-based web application that allows recruiters or job seekers to upload resumes and compare them with a job description. It uses Natural Language Processing (NLP) techniques to calculate a **match score**, helping streamline the resume screening process.

![resume screening demo](https://your-demo-image-or-gif-link.com) <!-- Optional: Add a screenshot or GIF here -->

---

## 🚀 Features

✅ Upload resumes (PDF/DOCX)  
✅ Paste job descriptions directly into the app  
✅ NLP-based match score calculation  
✅ Clean, responsive UI with modern design  
✅ Resume data is stored in a MySQL database for record-keeping

---

## 🧰 Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| Frontend    | HTML, CSS (custom UI styling)  |
| Backend     | Python, Flask                  |
| NLP         | Python string matching (can be upgraded to ML) |
| Database    | MySQL, SQLAlchemy ORM          |
| Deployment  | Run locally / Host via Render or Replit |

---

## 📸 UI Preview

### 🖥 Home Page

![screenshot](https://your-homepage-screenshot-url.com)

### 📊 Match Score Output

![result](https://your-result-page-screenshot-url.com)

---

## 📂 Project Structure

```bash
resume-screening-system/
│
├── app.py                  # Main Flask app
├── parser.py               # Extracts text from uploaded resumes
├── matcher.py              # Resume-job description matching logic
├── database.py             # DB model & initialization
├── requirements.txt        # Python dependencies
│
├── backend/
│   └── uploads/            # Uploaded resume files
│
├── templates/
│   ├── index.html          # Upload page
│   └── result.html         # Score result page
```

## ⚙️ Setup Instructions
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/resume-screening-system.git
cd resume-screening-system
```
### 2️⃣ Install Dependencies
#### Make sure you’re using Python 3.9+

```bash
pip install -r requirements.txt
```
### 3️⃣ Setup MySQL Database
#### Ensure MySQL is running, then:

```sql
CREATE DATABASE resume_db;
```
#### Update credentials in app.py:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/resume_db'
```
### 4️⃣ Run the Flask App
```bash
python app.py
```
#### Visit: http://localhost:5000


### ✅ How It Works
🔹 User uploads a resume and pastes a job description.

🔹 The app extracts plain text from the resume.

🔹 It compares the resume text with the job description using a similarity score (basic NLP).

🔹 Score is stored in the MySQL database and shown to the user.

### 🌐 Deployment Options
🔹 Render

🔹 Replit

🔹 Railway

Ask in the Issues tab if you'd like help deploying!


### 🧠 Future Improvements
🔹 🔍 Improve matching with cosine similarity or spaCy/transformers

🔹 📊 Add dashboard to view all uploaded results

🔹 👥 User login (HR vs Candidate roles)

🔹 📈 Resume quality insights (keywords, structure, grammar)

### 🧑‍💻 Author
### Dinnesh Kumaar
### [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dinnesh-kumaar-a3053a21b/) | [![Resume](https://img.shields.io/badge/Resume-View-blueviolet?style=flat&logo=read-the-docs&logoColor=white)](https://drive.google.com/file/d/12MDdctbXyQIA1L62xYTtLJw6uSxM6ZOC/view?usp=sharing)

### 📄 License
#### This project is licensed under the MIT License.

### ⭐ Show Your Support
#### If you like this project, please give it a ⭐ on GitHub and share it with others!
