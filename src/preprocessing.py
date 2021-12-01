import pandas as pd
import numpy as np 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt


# removing stopwords
def remove_stopwords(sentence):
    stp = set(stopwords.words('english'))
    word_tokens = word_tokenize(sentence)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stp]
    filtered_sentence = []
    
    for w in word_tokens:
        if w not in stp:
            filtered_sentence.append(w)

    return filtered_sentence




