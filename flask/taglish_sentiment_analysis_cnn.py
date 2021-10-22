import pre_process as scan
from nltk import word_tokenize
from tensorflow import keras 
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import numpy as np
import pickle

MAX_SEQUENCE_LENGTH = 50
EMBEDDING_DIM = 300
TRAINING_VOCAB = 2455

#LOAD MODEL
taglish_model = keras.models.load_model('C:/Users/johnr/Documents/Sentiment Analysis/sentiment-analysis-thesis/Interface/static/model/tag-lish_cnn.h5')

#LOAD TOKENIZER
with open('C:/Users/johnr/Documents/Sentiment Analysis/sentiment-analysis-thesis/Interface/static/model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# CONVERT LIST TO STRING
def listToString(s): 
    
  # initialize an empty string
  str1 = " " 
    
  # return string  
  return (str1.join(s))


def predict_sentiment(input):
  
  #PREPROCESSING
  clean = scan.remove_punct(input)
  clean = word_tokenize(clean)
  clean = scan.lowerStemmer(clean)
  clean = scan.removeStopWords(clean)

  input = listToString(clean)


  test = [[]]
  test[0] = clean

  #CONVERT INPUT INTO PADDING
  clean_sequences  = tokenizer.texts_to_sequences(test)
  clean_input = pad_sequences(clean_sequences, maxlen=MAX_SEQUENCE_LENGTH)

  #model prediction

  input_predictions = taglish_model.predict(clean_input, batch_size=1024, verbose=1)

  labels = [2,0,1]

  input_prediction_labels = labels[np.argmax(input_predictions)]


  return input_prediction_labels