# TF-IDF  (term frequency–inverse document frequency)
# To overcome problems of Bag of words (same importance to all words) we use TF-IDF where each word has its own importance


import nltk
import pandas as pd

f = open("Natural Language Processing/1. Data.txt","r", encoding="utf-8")
f.seek(0)
para = f.read()
para

# Cleaning texts
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
sentences = nltk.sent_tokenize(para)

corpus = []

for i in range(len(sentences)):
      review = re.sub('[^a-zA-Z]'," ",sentences[i]) # replace other than a-z,A-Z to spaces in sentence[i]
      review = review.lower()
      review = review.split() # Split into words
      review = [ps.stem(x) for x in review if x not in set(stopwords.words("english"))]
      review = " ".join(review)
      corpus.append(review)

# Creating TF-IDF models
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
x = tf.fit_transform(corpus).toarray()