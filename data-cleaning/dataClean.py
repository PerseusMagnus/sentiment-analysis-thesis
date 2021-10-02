import pandas as pd

import nltk
#nltk.download('punkt')  #for tokenizer
from nltk import word_tokenize, WordNetLemmatizer

import re
import string

#next na isama yung dataset para di mabigat kada pull 

#data = pd.read_csv('/content/imdb_labelled.tsv', header = None, delimiter='\t')
#data.columns = ['Text', 'Label']
#data.head()

def remove_punct(text):
    text_nopunct = ''
    text_nopunct = re.sub('['+string.punctuation+']', '', text)
    return text_nopunct

#convert all tokens to lowercase
def lower_token(tokens): 
    return [w.lower() for w in tokens] 

#remove punctuation
#data['Text_Clean'] = data['Text'].apply(lambda x: remove_punct(x))

#convert sentence into tokens
#tokens = [word_tokenize(sen) for sen in data.Text_Clean]

   
#lower_tokens = [lower_token(token) for token in tokens]