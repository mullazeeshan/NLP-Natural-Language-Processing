# Heading Lemmatization

# As stemming's outcome are words which may have less meaning. In order to over come that we use Lemmatization technique.

import nltk
import pandas as pd

f = open("Natural Language Processing/1. Data.txt","r", encoding="utf-8")
f.seek(0)
para = f.read()
para

sent="I will be going for swimming after going to gymming."

# Tokenising Sentences - Para into sentence
sentences = nltk.sent_tokenize(para)

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemmitizer = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmitizer.lemmatize(x) for x in words if x not in set(stopwords.words('english'))]
    sentences [i]= " ".join(words)