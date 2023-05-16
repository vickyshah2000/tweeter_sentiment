import pandas as pd
import numpy as np
import nltk
import re
import pickle
import itertools
from nltk.stem.wordnet import WordNetLemmatizer 
from django.conf import settings
import os
from sklearn import svm
from sklearn.svm import SVC
import seaborn as sns
import neattext.functions as nfx
# Load ML Pkgs
# Estimators
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

# Transformers
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
# tweet = 'Layin n bed with a headache  ughhhh...waitin on your call...'
import joblib
import pickle
class emotion_analysis_code():

    lem = WordNetLemmatizer()

    def cleaning(self, text):
        txt = str(text)
        txt = re.sub(r"http\S+", "", txt)
        if len(txt) == 0:
            return 'no text'
        else:
            txt = txt.split()
            index = 0
            for j in range(len(txt)):
                if txt[j][0] == '@':
                    index = j
            txt = np.delete(txt, index)
            if len(txt) == 0:
                return 'no text'
            else:
                words = txt[0]
                for k in range(len(txt)-1):
                    words+= " " + txt[k+1]
                txt = words
                txt = re.sub(r'[^\w]', ' ', txt)
                if len(txt) == 0:
                    return 'no text'
                else:
                    txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
                    txt = txt.replace("'", "")
                    txt = nltk.tokenize.word_tokenize(txt)
                    #data.content[i] = [w for w in data.content[i] if not w in stopset]
                    for j in range(len(txt)):
                        txt[j] = self.lem.lemmatize(txt[j], "v")
                    if len(txt) == 0:
                        return 'no text'
                    else:
                        return txt

    def predict_emotion(self, tweet):

        tweet_in_pandas = pd.Series(' '.join(self.cleaning(tweet)))

        # #path_vec = os.path.join(settings.MODELS, 'vectorizer.pickle')
        # path_model = os.path.join(settings.MODELS, 'emotion.pkl')
        # path_vec = os.path.join(settings.MODELS, 'emotions.csv')
        path_model = os.path.join(settings.MODELS, 'emotion.pkl')
        path_vec = os.path.join(settings.MODELS, 'emotions.csv')

        # # load vectorizer
        # # vec_file = 'vectorizer.pickle'
        # vectorizer = pickle.load(open(path_vec, 'rb'))

        # # load trained model
        # # filename = 'finalized_model.sav'
        # model = pickle.load(open(path_model, 'rb'))
        pipe_lr=joblib.load(open(path_model, "rb"))
        #df_predict=np.loadtxt(path_vec, skiprows=0)
        df_predict=pd.read_csv(path_vec)
        #x_train=df_predict.transform(tweet_in_pandas)
        text=df_predict['text']

       # test = vectorizer.transform(tweet_in_pandas)
        predicted_sentiment = pipe_lr.predict(text)
        final_sentiment = (predicted_sentiment[0])
        if final_sentiment == 'worry':
            return 'Worry'
        elif final_sentiment == 'sadness':
            return 'Sadness'
        elif final_sentiment == 'joy':
            return 'Joy'
        elif final_sentiment == 'love':
            return 'Love'
        else:
            return 'Hate'