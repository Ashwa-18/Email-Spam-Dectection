iimport streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()

# Load the vectorizer and model
def tranform_text(text):
    texts = text.lower()
    texts = nltk.word_tokenize(texts)
    y = []
    for i in texts:
        if i.isalnum():  # alphanumeric
            y.append(i)
    textt = y[:]
    y.clear()
    for i in textt:
        if i not in stopwords.words('english') and string.punctuation:
            y.append(i)
    textt = y[:]
    y.clear()
    for i in textt:
        y.append(ps.stem(i))
    return " ".join(y)
   
   
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title("Email/SMS Spam Classifier")
input_email = st.text_area("Enter a Message")
# 1: preprocess
tranform_email = tranform_text(input_email)
# 2: vectorizer
vec_email = tfidf.transform([tranform_email])
# 3: predict
result = model.predict(vec_email )[0] # 0 or 1 it returns array so we take first element..Actualy array returned 1 element but in so we want to take integer
# 4  Display
if st.button("Check"):
    if result == 0:
        st.header("Not Spam")
    else:
        st.header("Spam")


     
