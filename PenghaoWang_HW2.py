__author__ = 'penghao'
import numpy
from numpy import *
from math import *
import csv
import sys
from collections import Counter

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

reader=csv.reader(open("train.csv"),delimiter=' ')

#read csv files
f = open('train.csv')
csv_f = csv.reader(f)
review_list =[]
list_word=[]
list_word2=[]
all_word=[]
al_w=set()
for row in csv_f:
    if row[0].split(' ') not in review_list and row[0].split(' ') != ',':
        review_list.append(row[0].split(' '))

print(review_list[0])
print(review_list.__len__())
for i in range(review_list.__len__()):
    for column in review_list[i]:
        if column != ',' and column != '.' and column !=''and column !='!'and column !='...'and column !='(' and column !=')'and column !='"'and column !='--'and column !='?' \
                and column !=';'and column !=':':
            all_word.append(column)
            al_w.add(column)
            #if column not in list_word2:
            #    list_word2.append(column)
#print(all_word[0])
#print(al_w)
#print(list_word2)
list_word=list(al_w)

print(list_word.__len__())
#print(list_word2.__len__())
#temp = [item for item in list_word if item in list_word2]
#print(temp.__len__())
#ad_list=remove_values_from_list(all_word,'a')
#print(list_word.__len__())
#print(all_word.count('a'))
#print(ad_list.__len__())


c= Counter(all_word).most_common(list_word.__len__())
#common_most= Counter(all_word).most_common(50)
#c1=common_most
#print (c1[0])

for elements in c:
    removestr = elements
    if removestr[1]<5 or removestr[1]>300:
        list_word.remove(removestr[0])

print(list_word.__len__())