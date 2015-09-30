__author__ = 'penghao'
import numpy
from numpy import *
from math import *
import csv
import sys
from collections import Counter

reader=csv.reader(open("train.csv"),delimiter=' ')
review_list =[]
#print(reader)
x=list(reader)
result=numpy.array(x)
for row in reader:
    print(row[0])
    #review_list.append(row[0])


#print(review_list)

#traindata = loadtxt('train.csv',usecols=range(1),dtype=str)

f = open('train.csv')
csv_f = csv.reader(f)
review_list =[]
list_word=[]
all_word=[]

for row in csv_f:
#    review_list.append([x.strip() for x in row.split(',')])
    if row[0].split(' ') not in review_list and row[0].split(' ') != ',':
        review_list.append(row[0].split(' '))
print(review_list[0][1])
print(review_list.__len__())
#for row in review_list:
for i in range(review_list.__len__()):
    for column in review_list[i]:
        if column != ',' and column != '.' and column !=''and column !='!'and column !='...' :
            all_word.append(column)
            if column not in list_word:
                list_word.append(column)

print(list_word.__len__())
print(all_word.__len__())
for word in all_word:
    if all_word.count(word)>1000:
        all_word.remove(word)
        list_word.remove(word)


print(list_word.__len__())
print(all_word.__len__())

if review_list[0][1] == 'messages':
    print('cool')
print(list_word.count("a"))





#my_string = "blah, lots  ,  of ,  spaces, here "
#mylist = [x.strip() for x in my_string.split(',')]
#print(mylist[1])
#print(review_list)
#print(csv_headings[0])
#for word in f.read().split():
#    print(word)

#traindata = loadtxt('train.csv',usecols=range(0),dtype=str)

#print(traindata)