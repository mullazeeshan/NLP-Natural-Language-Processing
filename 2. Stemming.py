# Stemming is a process of deriving to the base word of the given word

import nltk
import pandas as pd

f = open("Natural Language Processing/1. Data.txt","r", encoding="utf-8")
f.seek(0)
para = f.read()
para

# Tokenising Sentences - Para into sentence
sentences = nltk.sent_tokenize(para)

# Tokenising words - Para into word
words = nltk.word_tokenize(para)

# - - - - - - - - - 2. Stemming and Lemmitization
from nltk.stem import PorterStemmer

# Our text data may contain words like of, the , out, them as such which may be repeated very frequently but still is not helpful in nlp. So we avoid such words with the help of stopwords
from nltk.corpus import stopwords



# creating an instance / object of PorterStemmer
stemmer = PorterStemmer()

# stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(x) for x in words if x not in set(stopwords.words('english'))]
    sentences[i] = " ".join(words)