import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


def clean_up(s):
    rules_list= ['@\w+','[^a-z,A-Z]', 'http', 'com','[^a-z,A-Z]']
    """
    Cleans up numbers, URLs, and special characters from a string.

    Args:
        s: The string to be cleaned up.

    Returns:
        A string that has been cleaned up.
    """
    for rule in rules_list:
        s = re.sub(rule,' ',s)
    return s

def tokenize(s):
    """
    Tokenize a string.

    Args:
        s: String to be tokenized.

    Returns:
        A list of words as the result of tokenization.
    """
    return nltk.word_tokenize(s)

def stem_and_lemmatize(l):

    lemmatizer = WordNetLemmatizer()
    stemporter = PorterStemmer()

    """=
    Perform stemming and lemmatization on a list of words.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after being stemmed and lemmatized.
    """
    stemandlemmalist=[]
    
    for word in l:
        stemmed = stemporter.stem(word)
        stemandlemma = lemmatizer.lemmatize(stemmed)
        stemandlemmalist.append(stemandlemma)
    return stemandlemmalist

def remove_stopwords(l):
    """
    Remove English stopwords from a list of strings.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after stop words are removed.
    """
    stop_words = set(stopwords.words('english'))
    
    for words in l:
        if words in stop_words:
            l.remove(words)
    return l