# spoonshot_app


## Q1 
### Run Instructions 

```
cd Q1/
python compare.py
```
Install all required packages using 

```
pip install requirements.txt
```

### Explanation of approaches used.

1. Used nltk library to find most common words in the article, calcuated the their frequency.
2. Matching the words in the ingridient list to the words in the most common words list.
3. Synonyms of the words in the ingridient list and looked for them in the most common words list.
4. WebScrapping, webscrapped data from [Dictionary.com](www.dictonary.com).
5. Also impleted bert on the article given to pick out relevant keywords, however that was dropped since words were very limited.
6. For comparing strings used `nltk.edit_distance()` to adjust for words like ***vegetable*** and ***vegetables***


### Output

The 3 models used require different amount of time, the graph has been plotted out below.
-->  add graph

The Output of the three codes are as follows. 
-->  add ouput ss



## Q2 
### Run Instructions 

Used 2 different algorithms for solving the problem both of them are **O(n)** 

1. It goes through array twice once forward and once backward and multiplies all prev products with the current element to get a product from both sides.

2. It goes through the array once and calculates the product and checks for number of 0's.

> Run time for 1 is slighly less than 2, but I prefer 2 over one since its cleaner and uses a better algorithm for larger datasets.

