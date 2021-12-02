from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class preprocessing():
    def __init__(self, sentence):
        self.sentence = sentence

    # removing stopwords
    def remove_stopwords(self):
        stp = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.sentence)

        filtered_sentence = [w for w in word_tokens if not w.lower() in stp]
        filtered_sentence = []
        
        for w in word_tokens:
            if w not in stp:
                filtered_sentence.append(w)

        s = " ".join(filtered_sentence)

        self.sentence = s

    # converts all words in sentence to lowercase
    def lower_case(self):
        self.sentence = self.sentence.lower()

    # converts contractions to their full form in a given sentence
    def remove_contractions(self):
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

        words = self.sentence.split()
        reformed = [appos[word] if word in appos else word for word in words]
        retval = " ".join(reformed)
        self.sentence = retval

    # removes punctuation from a given sentence
    def remove_punctuation(self):
        word_tokens = word_tokenize(self.sentence)
        words = []
        for word in word_tokens:
            if word.isalpha():
                words.append(word)
        print(words)
        self.sentence = " ".join(words)

    def preprocess(self):
        self.lower_case()
        self.remove_stopwords()
        self.remove_contractions()
        self.remove_punctuation()

    def get_sent(self):
        return self.sentence

