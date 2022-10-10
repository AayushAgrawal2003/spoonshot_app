
#nltk.download('punkt')
#nltk.download('brown')

from collections import Counter
from math import log
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.corpus import wordnet
from search import arr
import pprint
from collections import OrderedDict
import numpy as np
import math

toks = word_tokenize(open('../Q1/data.txt').read().lower().replace(',',"").replace('.',"").replace('!',"").replace('"',"").replace("'","").replace("’","").replace("and","").replace('–'," "))
tf = Counter(toks)

freqs = Counter(w.lower() for w in brown.words())
n = len(brown.words())
for word in tf:
    tf[word] *= log(n / (freqs[word] + 1))**2    


common_words = tf.most_common()

