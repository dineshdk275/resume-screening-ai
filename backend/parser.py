import spacy
import re

nlp = spacy.load('en_core_web_sm')

# Define a simple skill list or load from a file
SKILLS_DB = ['java', 'python', 'javascript', 'html', 'css', 'react', 'node.js', 'express', 'mysql', 'flask']

def extract_skills(text):
    doc = nlp(text.lower())
    skills_found = set()

    # Look for exact skill matches in tokens
    for token in doc:
        if token.text in SKILLS_DB:
            skills_found.add(token.text)

    # Also check for multi-word skills using regex or phrase matching (optional)
    # Example for 'node.js'
    if re.search(r'node\.js', text.lower()):
        skills_found.add('node.js')

    return list(skills_found)

def extract_experience(text):
    # Simple regex to extract years of experience mentioned e.g. "2 years", "3+ years"
    experience = 0
    matches = re.findall(r'(\d+)\s*\+?\s*(year|yr)s?', text.lower())
    if matches:
        experience = max(int(match[0]) for match in matches)
    return experience

def extract_education(text):
    # Look for keywords like B.Tech, Bachelor, Master, etc.
    edu_keywords = ['bachelor', 'master', 'b.tech', 'bsc', 'msc', 'phd']
    text_lower = text.lower()
    for kw in edu_keywords:
        if kw in text_lower:
            return kw
    return None

def extract_text(file_path):
    # This depends on your file type; if PDF, use PyPDF2 or similar
    import PyPDF2
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text
