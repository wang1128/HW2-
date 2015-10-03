__author__ = 'penghao'
import numpy
from numpy import *
from math import *
import csv
import sys
from collections import Counter

#read csv files
f = open('train.csv')
csv_f = csv.reader(f)
review_list =[]
list_word=[]
all_word=[]
al_w=set()

for row in csv_f:
    if row[0].split(' ') not in review_list and row[0].split(' ') != ',':
        review_list.append(row[0].split(' '))

#Creat the list of words that we will use
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
