import re
import nltk
import pickle
import googletrans
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')

from googletrans import Translator
translator = Translator()

tfidf  = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model-mlp.pkl', 'rb'))

#Text Preprocessing
lemma = WordNetLemmatizer()
def textpreprocess(text):
    Comment = re.sub('[^a-zA-Z]', ' ', text)
    Comment = Comment.lower()
    Comment = Comment.split()
    Comment = [lemma.lemmatize(word) for word in Comment if word not in set(stopwords.words('english'))]
    Comment = ' '.join(Comment)
    
    return Comment


st.title("Abussive Language detection")
input_comment = st.text_input("Enter the comment")


if st.button('Predict'):
    
    # translating the bangla comment into English
    translation = translator.translate(input_comment, dest = 'en')
    translated_text = translation.text
    
    # Preprocess
    transform_comment = textpreprocess( translated_text) 

    #Vectorize 
    vector_input = tfidf.transform([transform_comment])

    #predict
    result = model.predict(vector_input)[0]

    #display

    if result == 1:
        st.header("This is a abussive comment")

    else:
        st.header("This is not a abusive comment")
