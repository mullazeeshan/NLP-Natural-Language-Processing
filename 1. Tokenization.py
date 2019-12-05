# Heading  - - - - - Tokenization of paragraphs/sentences
# Tokenisation is a process of breaking down given paragraph into words or sentences.

import nltk
import pandas as pd

# Run below lines to install nltk additional resources
# nltk.download()
# nltk.download('punkt')


f = open("Natural Language Processing/1. Data.txt","r", encoding="utf-8")
f.seek(0)
para = f.read()

para

# Tokenising Sentences - Para into sentence
sentences = nltk.sent_tokenize(para)

# Tokenising words - Para into word
words = nltk.word_tokenize(para)


