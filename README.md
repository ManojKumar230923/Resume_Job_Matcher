# Resume_Job_Matcher
# Resume Matcher

This is a Python-based tool for matching resumes (in PDF format) to job descriptions using text extraction, cleaning, and natural language processing (NLP) techniques. It allows users to upload a resume in PDF format, clean the text, and match the resume to predefined job descriptions.

## Features

- **PDF Resume Upload**: Allows users to upload a resume in PDF format.
- **Text Extraction**: Extracts text content from the uploaded resume.
- **Text Cleaning**: Cleans the extracted text by removing stop words and non-alphabetic characters.
- **Job Matching**: Matches the cleaned resume text to predefined job descriptions using TF-IDF vectorization and cosine similarity.
- **Job Suggestions**: Returns the top job matches based on similarity scores.

## Requirements

Make sure you have Python 3.6 or higher installed, along with the following libraries:

- `fitz` (PyMuPDF): For reading and extracting text from PDF files.
- `nltk`: For natural language processing (e.g., stopword removal).
- `sklearn`: For vectorization and cosine similarity calculation.
- `ipywidgets`: For creating interactive widgets in Jupyter Notebooks.

You can install the required libraries using the following command:

```bash
pip install fitz nltk scikit-learn ipywidgets
