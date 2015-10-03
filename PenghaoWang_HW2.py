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
all_word=[]

for row in csv_f:
    if row[0].split(' ') not in review_list and row[0].split(' ') != ',':
        review_list.append(row[0].split(' '))

print(review_list[0])
print(review_list.__len__())
for i in range(review_list.__len__()):
    for column in review_list[i]:
        if column != ',' and column != '.' and column !=''and column !='!'and column !='...' :
            all_word.append(column)
            if column not in list_word:
                list_word.append(column)


print(all_word.__len__())
ad_list=remove_values_from_list(all_word,'a')
print(list_word.__len__())
print(all_word.count('a'))
print(ad_list.__len__())

"""
for word in all_word:
    if all_word.count(word)>500:
        print(word,all_word.count(word))
        all_word=remove_values_from_list(all_word,word)

"""

#if review_list[0][1] == 'messages':
#    print('cool')
#print(list_word.count("a"))

c= Counter(all_word).most_common(100)
print (c)



#my_string = "blah, lots  ,  of ,  spaces, here "
#mylist = [x.strip() for x in my_string.split(',')]
#print(mylist[1])
#print(review_list)
#print(csv_headings[0])
#for word in f.read().split():
#    print(word)

#traindata = loadtxt('train.csv',usecols=range(0),dtype=str)

#print(traindata)