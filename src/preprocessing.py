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

    s = " ".join(filtered_sentence)

    return s

# converts all words in sentence to lowercase
def lower_case(sentence):
    return sentence.lower()

# 
def apostrophe(sentence):
    appos = {
        "aren't": "are not",
        "can't": "cannot",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "i'll": "I will",
        "i've": "I have",
        "couldn't": "could not"
    }

    words = sentence.split()
    reformed = [appos[word] if word in appos else word for word in words]
    retval = " ".join(reformed)
    return retval


print(apostrophe(lower_case("Dam this is the cutest and saddest movie I've ever seen I played with my dog for an hour after watching this, couldn't cry")))