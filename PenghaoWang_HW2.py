__author__ = 'penghao'

from numpy import *
import numpy as np
from math import *
import csv
import sys
from collections import Counter



#read csv files
f = open('train.csv')
csv_f = csv.reader(f)
review_list =[]
review_label = []
list_word=[]
all_word=[]
al_w=set()

for row in csv_f:
    if row[0].split(' ') not in review_list and row[0].split(' ') != ',':
        review_list.append(row[0].split(' '))
    if row[1] is'+':
        review_label.append(1)
    else :
        review_label.append(0)

print(review_label)
#print(review_label)
#Creat the list of words that we will use
#print (review_list[0])
for i in range(review_list.__len__()):
    for column in review_list[i]:
        if column != ',' and column != '.' and column !=''and column !='!'and column !='...'and column !='(' and column !=')'and column !='"'and column !='--'and column !='?' \
                and column !=';'and column !=':':
            all_word.append(column)
            al_w.add(column)

list_word=list(al_w)
#Delete the most common words and words that appears less than five time
c= Counter(all_word).most_common(list_word.__len__())
for elements in c:
    removestr = elements
    if removestr[1]<5 or removestr[1]>300:
        list_word.remove(removestr[0])

w = [0]*list_word.__len__()

feature_array = np.zeros((review_list.__len__(),list_word.__len__()))
#print(w.__len__())
#print(list_word.__len__())
#print(list_word.index('clearly'))
#creat feature value for every row
for idx in range(review_list.__len__()):
    x = [0]*list_word.__len__()
    for words in review_list[idx]:
        if words in list_word:
            index =list_word.index(words)
            x[index] = 1
            feature_array[idx] = np.array(x)
#print(list_word[1451])
print(feature_array[0])
y = np.array(list_word)
print(y)
print type(y)

maxIter = 10
b=0
for iteration in range(maxIter):
    random_idx = np.random.permutation(2853)