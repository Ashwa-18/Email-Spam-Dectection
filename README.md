# Email Spam Classifier 📩🚫

A machine learning project that classifies emails/messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques and multiple classification models.

## Project Overview
This project performs end-to-end spam detection by cleaning and preprocessing text data, extracting useful features, training multiple machine learning models, and comparing their performance.

## Dataset
- Dataset used: **spam.csv**
- Total records: **5572**
- After cleaning duplicates: **5169**

## Workflow
1. Data Cleaning  
   - Removed unnecessary columns  
   - Renamed columns  
   - Removed duplicates  

2. Exploratory Data Analysis (EDA)  
   - Spam vs Ham distribution  
   - Text length analysis  
   - Word and sentence analysis  

3. Text Preprocessing  
   - Lowercasing  
   - Tokenization  
   - Removing punctuation  
   - Stopwords removal  
   - Stemming  

4. Feature Engineering  
   - TF-IDF Vectorization  

5. Model Building & Evaluation  

## Models Applied
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Bernoulli Naive Bayes
- Logistic Regression
- SVC
- Decision Tree
- KNN
- Random Forest
- AdaBoost
- Extra Trees
- Gradient Boosting
- XGBoost

## Best Model Performance 🏆
### Bernoulli Naive Bayes
- Accuracy: **98.07%**
- Precision Score: **1.00**

### Multinomial Naive Bayes
- Accuracy: **96.71%**
- Precision Score: **1.00**

## Technologies Used
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- NLTK

## Project Files
- `app.ipynb` → Main notebook
- `spam.csv` → Dataset
- `requirements.txt` → Required libraries



---
Developed for learning NLP and Machine Learning 🚀
