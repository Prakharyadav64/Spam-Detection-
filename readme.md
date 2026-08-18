# Spam Message Detection

An ML-based web application that classifies text messages as Spam or Ham using TF-IDF and Multinomial Naive Bayes.

## Features

- Text message classification
- TF-IDF feature extraction
- Multinomial Naive Bayes model
- Saved ML pipeline using Joblib
- Streamlit web interface
- Local prediction through a simple UI

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Joblib
- Streamlit

## Machine Learning Workflow

1. Load the SMS dataset
2. Clean the dataset
3. Remove duplicate messages
4. Encode Ham and Spam labels
5. Split data into training and testing sets
6. Convert text into TF-IDF features
7. Train Multinomial Naive Bayes
8. Evaluate the model
9. Save the trained pipeline using Joblib
10. Build the Streamlit application
11. Deploy the application

## Project Structure

```text
Spam_detection/
│
├── app.py
├── spam.csv
├── spam_detection.ipynb
├── spam_model.joblib
├── requirements.txt
├── README.md
└── .gitignore






1. Create virtual environment
python -m venv venv

2. Activate it
.\venv\Scripts\Activate.ps1

3. Install dependencies
pip install -r requirements.txt

Run the application
streamlit run app.py





Model

The final model uses a Scikit-learn Pipeline containing:

TfidfVectorizer
MultinomialNB
The complete pipeline is saved as:
spam_model.joblib


Future Improvements
Improve spam recall
Add probability/confidence score
Add message history
Improve UI
Experiment with other classification algorithms

