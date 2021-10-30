from nltk import word_tokenize, WordNetLemmatizer
import nltk
nltk.download('punkt')
from flask import Flask, render_template, request
import taglish_sentiment_analysis_cnn as model


app = Flask(__name__)

@app.route('/')
def main():
    return  render_template("index.html")
    

@app.route('/predict',methods=['POST','GET'])

def predict():
    
    input = request.form.get("sentimentArea")

    if request.method == "POST" and input:
        # getting input with name = fname in HTML form
        sentiment = model.predict_sentiment(input)

    return jsonify( {'sentiment' : sentiment})
    '''
    if(sentiment==2):
        return render_template("index.html",sentiment='Predicted Sentiment:  Positive')

    if(sentiment==1):
        return render_template("index.html",sentiment='Predicted Sentiment:  Neutral')

    if(sentiment==0):
        return render_template("index.html",sentiment='Predicted Sentiment:  Negative')
    '''

if __name__ == '__main__':
    app.run(debug=True)