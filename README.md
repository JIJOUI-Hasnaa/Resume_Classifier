# Resume Classifier 📄

## Overview

Resume Classifier is an NLP-based application designed to automatically analyze and classify resumes into predefined professional categories.

The project uses Natural Language Processing (NLP) and Machine Learning techniques to transform resume text into numerical representations and predict the corresponding job category.

## Features

- Resume text extraction and preprocessing.
- Text vectorization using a trained vectorizer.
- Resume classification using a Machine Learning model.
- Interactive application interface.
- Automated prediction of professional categories.

## Project Structure

```text
Resume_Classifier/
│
├── images/
├── pages/
├── __pycache__/
├── Home_Page.py
├── main.py
├── model.py
├── extraction.py
├── model.pkl
├── vectorizer.pkl
├── pyproject.toml
└── README.md
```

## Technologies Used

- Python
- Natural Language Processing (NLP)
- Machine Learning
- Scikit-learn
- Pandas
- Streamlit
- Joblib

## How It Works

1. A resume is provided to the application.
2. Text is extracted from the resume.
3. The extracted text is preprocessed.
4. The trained vectorizer converts the text into numerical features.
5. The Machine Learning model predicts the resume category.
6. The predicted category is displayed to the user.

## Installation

Clone the repository:

```bash
git clone https://github.com/JIJOUI-Hasnaa/Resume_Classifier.git
cd Resume_Classifier
```

Install dependencies:

```bash
pip install -e .
```

Run the application (if Streamlit is configured):

```bash
streamlit run Home_Page.py
```

## Project Purpose

This project explores the application of NLP and Machine Learning to resume classification and automated recruitment support.

## Author

**Hasnaa JIJOUI**

