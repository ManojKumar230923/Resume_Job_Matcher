#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import fitz  # PyMuPDF
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import ipywidgets as widgets
from IPython.display import display, clear_output


# In[2]:


# Download stopwords once
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


# In[3]:


# --- Resume Text Extraction ---
def extract_resume_text(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# In[4]:


# --- Text Cleaning ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)


# In[5]:


# --- Sample Job Descriptions ---
job_descriptions = {
    "Data Scientist": "Looking for a Data Scientist with experience in Python, machine learning, NLP, pandas, scikit-learn, etc.",
    "Web Developer": "Looking for a Web Developer with HTML, CSS, JavaScript, React or Django experience.",
    "DevOps Engineer": "DevOps Engineer role involving Docker, Kubernetes, CI/CD, and AWS or Azure experience."
}


# In[6]:


# --- Resume Matching ---
def match_resume_to_jobs(resume_text, job_descriptions):
    documents = [resume_text] + list(job_descriptions.values())
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    matches = sorted(zip(job_descriptions.keys(), similarity_scores), key=lambda x: x[1], reverse=True)
    return matches


# In[10]:


# --- File Upload Function ---
def on_file_upload(change):
    global file_path, file_content
    if change.new:
        file_content = change.new[0]['content']  # Get file content as bytes
        file_path = change.new[0]['name']  # Get file name
        file_path_label.value = f"✅ File selected: {file_path}"
        #run_button.tooltip = file_content  # Store content in the button tooltip


# In[12]:


# --- UI Widgets ---
file_upload = widgets.FileUpload(accept='.pdf', multiple=False)
run_button = widgets.Button(description="🔍 Match Jobs")
output = widgets.Output()

file_path_label = widgets.Label(value="No file selected")

def on_run_button_clicked(b):
    with output:
        clear_output()
        if not file_content:
            print("❌ No file selected. Please upload a file first.")
            return
        print("🔄 Processing...")
        resume_raw_text = extract_resume_text(file_content)
        resume_clean = clean_text(resume_raw_text)
        matches = match_resume_to_jobs(resume_clean, job_descriptions)
        print("\n✅ Top job matches:\n")
        for role, score in matches:
            print(f"{role}: {score * 100:.2f}%")

# Observe the file upload
file_upload.observe(on_file_upload, names='value')

# Button click handler for matching jobs
run_button.on_click(on_run_button_clicked)

# Display widgets in the notebook
display(file_upload, file_path_label, run_button, output)







