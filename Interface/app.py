from nltk import word_tokenize, WordNetLemmatizer
import nltk
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import taglish_sentiment_analysis_cnn as model
from werkzeug.utils import secure_filename
import os
import pandas as pd
import csv
from io import StringIO

app = Flask(__name__)

import os
from os.path import join, dirname, realpath

#global variable 
input_with_polarity = []


# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'C:/Users/ditab/Documents/thesis development/sentiment-analysis-thesis/Interface/static/files/'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER



#homepage
@app.route('/')
def main():
    return render_template("index.html")

#sentiment area
@app.route('/sentiment',methods=['POST','GET'])
def sentiment():
    return render_template("analyze.html")
    
#predict single input
@app.route('/predict',methods=['POST','GET'])

def predict():
    
    input = request.form.get("sentimentArea")

    if request.method == "POST":
        # getting input with name = fname in HTML form
        sentiment = model.predict_sentiment(input)
    else:
        return render_template("analyze.html",sentiment='Input is Empty')
    
    if(sentiment==2):
        return render_template("analyze.html",sentiment='Predicted Sentiment:  Positive')

    if(sentiment==1):
        return render_template("analyze.html",sentiment='Predicted Sentiment:  Neutral')

    if(sentiment==0):
        return render_template("analyze.html",sentiment='Predicted Sentiment:  Negative')


#predict multiple input   
@app.route('/predict_multiple',methods=['POST','GET'])

def uploadFiles():
    global input_with_polarity
    # get the uploaded file
    uploaded_file = request.files['file']

    print(uploaded_file.filename)
    
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        # save the file

        #read the uploaded file
        data = pd.read_csv(file_path,header = None)

        data.columns = ['text']

        sentiment_prediction = []
        emoji = 0
        no_emoji = 0

        for text in data['text']:
            polarity = model.predict_sentiment(text)
            sentiment_prediction.append(polarity[0])

            #count inputs with emoji and w/o emoji
            if(polarity[1]):
                emoji += 1
            else:
                no_emoji += 1

        #write to csv
        import csv  


        #save the text and its respective polarity into list of list
        for n in range(len(data['text'])):
            input_with_polarity.append([data['text'][n],sentiment_prediction[n]])

        
        pos = 0
        neg = 0
        neu = 0

        for sentiment in sentiment_prediction:
            if(sentiment==0):
                neg+=1
            if(sentiment==2):
                pos+=1
            if(sentiment==1):
                neu+=1
        
        print('positive: ',pos,'  negative: ',neg,'  neutral: ',neu)
        print('with emoji: ',emoji,'   without emoji: ',no_emoji)

    #start ako dito 
        header = ['Text', 'Polarity']

    si = StringIO()
        
    #with open('summarize.csv', 'w',newline='', encoding='UTF8') as f:
    writer = csv.writer(si)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(input_with_polarity)):
        print(i,' ',input_with_polarity[i])
        writer.writerow(input_with_polarity[i])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
        
    return output
    
    return render_template("analyze.html",positive = pos,negative=neg,neutral=neu,with_emoji=emoji,wo_emoji=no_emoji)
    

#download csv copy   
@app.route('/download',methods=['POST','GET'])

def download():

    header = ['Text', 'Polarity']

    si = StringIO()
        
    #with open('summarize.csv', 'w',newline='', encoding='UTF8') as f:
    writer = csv.writer(si)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(input_with_polarity)):
        print(i,' ',input_with_polarity[i])
        writer.writerow(input_with_polarity[i])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
        
    return output

if __name__ == '__main__':
    app.run(debug=True)