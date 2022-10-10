from collections import Counter
from math import log
from nltk import word_tokenize
from nltk.corpus import brown
import nltk
nltk.download('punkt')
nltk.download('brown')

toks = word_tokenize(open('data.txt').read().lower())
tf = Counter(toks)
freqs = Counter(w.lower() for w in brown.words())
n = len(brown.words())
for word in tf:
    tf[word] *= log(n / (freqs[word] + 1))**2    
for word, score in tf.most_common(10):
    print('%8.2f %s' % (score, word))