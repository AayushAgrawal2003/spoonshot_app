from collections import Counter
from math import log
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.corpus import wordnet
from search import arr
import pprint

def synonym_extractor(phrase):
     synonyms = []
     for syn in wordnet.synsets(phrase):
          for l in syn.lemmas():
               synonyms.append(l.name())

     #print(set(synonyms))
     return list(set(synonyms))

toks = word_tokenize(open('data.txt').read().lower())
tf = Counter(toks)
freqs = Counter(w.lower() for w in brown.words())
n = len(brown.words())
for word in tf:
    tf[word] *= log(n / (freqs[word] + 1))**2    


common_words = tf.most_common()

dict_main = {k: 1 for v, k in enumerate(arr)}

#Compare

for i in range(len(arr)):
    words = arr[i].split()
    for word in words:
        synonyms = synonym_extractor(word)
        for j in range(len(synonyms)):
            for k in range(len(common_words)):
                if common_words[k][0] == synonyms[j]:
                    #print(common_words[k][1])
                    #print(arr[i])
                    dict_main[arr[i]] *= common_words[k][1]            

pprint.pprint(dict_main)