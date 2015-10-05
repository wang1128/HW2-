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
        review_label.append(-1)

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



feature_array = np.zeros((review_list.__len__(),list_word.__len__()))


#feature_array contain all x, x is features of every row
for idx in range(review_list.__len__()):
    x = [0]*list_word.__len__()
    for words in review_list[idx]:
        if words in list_word:
            index =list_word.index(words)
            x[index] = 1
            feature_array[idx] = np.array(x,dtype=int)


def perceptron(maxIter):
    w = np.zeros(list_word.__len__())
    maxIter = maxIter
    b=0
    for iteration in range(maxIter):
        w_copy =w
        random_idx = np.random.permutation(review_list.__len__())
        for row_idx in random_idx:
            y = np.dot(w,feature_array[row_idx]) + b
            if y>0:
                predict_label = 1
            else:
                predict_label = -1
            review_l = review_label[row_idx]
            if review_l != predict_label:
                w = w + review_l* feature_array[row_idx]
        if np.array_equal(w_copy,w):
            print("converge"+ iteration)
            continue
    return w

print(perceptron(10))
'''
f = open('validation.csv')
csv_f2 = csv.reader(f)
review_list =[]
review_label = []
list_word=[]
all_word=[]
al_w=set()
for row in csv_f2:
    if row[0].split(' ') not in vreview_list and row[0].split(' ') != ',':
        review_list.append(row[0].split(' '))
    if row[1] is'+':
        vreview_label.append(1)
    else :
        vreview_label.append(-1)
 '''