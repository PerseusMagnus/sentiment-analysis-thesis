from nltk import word_tokenize
import nltk
#nltk.download('punkt')
import os
import collections
import re
import string

# REMOVE PUNCTUATION
def remove_punct(text):
    text_nopunct = ''
    text_nopunct = re.sub('['+string.punctuation+']', '', text)
    return text_nopunct


# CONVERT TO LOWeER CASE
def lowerStemmer(tokens): 
    return [w.lower() for w in tokens] 

# GET AND SAVE THE STOPWORDS INTO LIST
stoplist = ""

with open('C:/Users/johnr/Documents/Sentiment Analysis/sentiment-analysis-thesis/Interface/static/stopwords/stopwords.txt',encoding="utf-8") as f:
  contents = f.read()
  stoplist = stoplist + contents
   
stoplist = word_tokenize(stoplist)

# FUNCTION TO REMOVE STOPWORDS
def removeStopWords(tokens): 
    return [word for word in tokens if word not in stoplist]

