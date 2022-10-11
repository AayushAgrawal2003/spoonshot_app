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
from scrapper import description
import time
import nltk

#User Input
print("Welcome! \nTo use Simple Word Matching [0] \nTo use Webscraping [1] --> This may take signicantly more time, since it scarapes the internet for a description for each ingridient\nTo use Synonyms [2] \nTo use All [3]")
control = int(input())
st = time.time()


#Finding Synonyms
def synonym_extractor(phrase):
     synonyms = []
     for syn in wordnet.synsets(phrase):
          for l in syn.lemmas():
               synonyms.append(l.name())

     #print(set(synonyms))
     return list(set(synonyms))


#Calculating the most used/relevant words in the article
toks = word_tokenize(open('data.txt').read().lower().replace(',',"").replace('.',"").replace('!',"").replace('"',"").replace("'","").replace("’","").replace("and",""))
tf = Counter(toks)
freqs = Counter(w.lower() for w in brown.words())
n = len(brown.words())
for word in tf:
    tf[word] *= log(n / (freqs[word] + 1))**2    

#list of words and their use frequecy
common_words = tf.most_common()

dict_main = {k: 0 for v, k in enumerate(arr)}

#Comparing all available data.

for i in range(len(arr)):
    words = arr[i].split()
    for word in words:
        if control== 0:
            for k in range(len(common_words)):
                if common_words[k][0].lower() == word.lower():
                    dict_main[arr[i]] += common_words[k][1] 
        #synonym list comparision 
        if control == 2 or control == 3:
            synonyms = synonym_extractor(word)
            synonyms.append(word)
            for j in range(len(synonyms)):
                for k in range(len(common_words)):
                    if nltk.edit_distance(common_words[k][0].lower(), synonyms[j].lower()) < 3:
                        dict_main[arr[i]] += common_words[k][1] 
        #webscrapper list comparision 
        if control == 1 or control == 3:
            #calling imported function description
            description_points =  description(word)
            for desc in description_points:
                for k in range(len(common_words[0:10])):
                    if nltk.edit_distance(common_words[k][0].lower(), desc.lower()) < 3 and len(common_words[k][0]) > 2:
                        dict_main[arr[i]] += common_words[k][1] 

et = time.time()

#Sorting and calculating percentage values.
sorted_dict = sorted(dict_main.items(), key=lambda kv:[kv[1], kv[0]] , reverse = 1)
total = 0
percentage = {}
rating = []
for value in dict_main.values():
    total += value
for i in sorted_dict:
    percentage[i[0]] = (str(math.ceil(((i[1]/total)*100))) + "%")
    rating.append([i[0] , (str(math.ceil(((i[1]/total)*100))) + "%")])
pprint.pprint(rating)
elapsed_time = et - st
print('process completed in: ', elapsed_time, 'seconds')
