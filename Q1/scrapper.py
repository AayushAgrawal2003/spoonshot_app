import pandas as pd
from bs4 import BeautifulSoup as bs
import requests 


def description(word):

    URL =  "https://www.dictionary.com/browse/" + word
    r = requests.get(URL)
    soup =  bs(r.content,'html.parser')


    l = soup.find('div' , attrs = {'class':'css-10n3ydx'})
    if l != None:
        vals = l.text.replace(';',' ').replace(':',' ').replace('.',' ').split(" ")[0:20]
    else:
        return([])

    return(vals)

#print(description("cars"))