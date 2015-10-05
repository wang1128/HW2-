__author__ = 'penghao'

from numpy import *
import numpy as np
from math import *
import csv
import sys
from collections import Counter

def cal_reviewlistlabel(filename):
    #read csv files
    f = open(filename)
    csv_f = csv.reader(f)
    review_list =[]
    review_label = []
    for row in csv_f:
        if row[0].split(' ') not in review_list and row[0].split(' ') != ',':
            review_list.append(row[0].split(' '))
        if row[1] is'+':
            review_label.append(1)
        else :
            review_label.append(-1)
    return review_list, review_label

def calListuniWord(review_list):
    list_word=[]
    all_word=[]
    al_w=set()
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
    return list_word

def calListbiWord(review_list):
    list_word=[]
    all_word=[]
    all_word_copy=[]
    list_biword=[]
    al_w=set()
    for i in range(review_list.__len__()):
        for column in review_list[i]:
            if column != ',' and column != '.' and column !=''and column !='!'and column !='...'and column !='(' and column !=')'and column !='"'and column !='--'and column !='?' \
                    and column !=';'and column !=':' and review_list[i].index(column) < review_list[i].__len__()-1:
                all_word.append(column+ ' ' + review_list[i][review_list[i].index(column)+1])
                al_w.add(column+ ' ' + review_list[i][review_list[i].index(column)+1])

    list_word=list(al_w)

    #Delete the most common words and words that appears less than five time
    c= Counter(all_word).most_common(list_word.__len__())
    for elements in c:
        removestr = elements

        if  removestr[1]<3 or removestr[1]>100: #removestr[0] is the word removestr[1] is the count
            list_word.remove(removestr[0])

    return list_word

def cal_feature_array(review_list,list_word):
    feature_array = np.zeros((review_list.__len__(),list_word.__len__()))
    #feature_array contain all x, x is features of every row
    for idx in range(review_list.__len__()):
        x = [0]*list_word.__len__()
        for words in review_list[idx]:
            if words in list_word:
                index =list_word.index(words)
                x[index] = 1
                feature_array[idx] = np.array(x,dtype=float)
    return feature_array

def cal_bifeature_array(review_list,list_word):
    feature_array = np.zeros((review_list.__len__(),list_word.__len__()))
    #feature_array contain all x, x is features of every row
    for idx in range(review_list.__len__()):
        x = [0]*list_word.__len__()
        for words in review_list[idx]:
            if review_list[idx].index(words) < review_list[idx].__len__()-1:
                biwords = words + ' ' + review_list[idx][review_list[idx].index(words)+1]
                if biwords in list_word:
                    index =list_word.index(biwords)
                    x[index] = 1
                    feature_array[idx] = np.array(x,dtype=float)
    return feature_array

def cal_both_feature_array(review_list,list_word):
    feature_array = np.zeros((review_list.__len__(),list_word.__len__()))
    #feature_array contain all x, x is features of every row
    for idx in range(review_list.__len__()):
        x = [0]*list_word.__len__()
        for words in review_list[idx]:
            if review_list[idx].index(words) < review_list[idx].__len__()-1:
                biwords = words + ' ' + review_list[idx][review_list[idx].index(words)+1]
                if biwords in list_word :
                    index =list_word.index(biwords)
                    x[index] = 1
            if words in list_word:
                index =list_word.index(words)
                x[index] = 1
            feature_array[idx] = np.array(x,dtype=float)
    return feature_array

def perceptron(maxIter,review_list,review_label,list_word,feature_array):
    w = np.zeros(list_word.__len__())
    maxIter = maxIter
    b = 0
    #feature_array = cal_feature_array(review_list,list_word)
    for iteration in range(maxIter):
        w_copy = w
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

            print("converge")
            print(iteration)
            break

    return w

'''
def winnow(maxIter):
    w = np.ones(list_word.__len__())
    maxIter = maxIter

    for iteration in range(maxIter):
        w_copy =w
        random_idx = np.random.permutation(review_list.__len__())
        for row_idx in random_idx:
            y = np.dot(w,feature_array[row_idx])
            if y>0:
                predict_label = 1
            else:
                predict_label = -1
            review_l = review_label[row_idx]
            if review_l != predict_label:
                w = w/2.0
        #if np.array_equal(w_copy,w):
        #    print("converge")
        #    continue
    return w
print(winnow(10))
'''
def calTrainError(filename,list_word,w,condition):
    vreviewlist,vreviewlabel = cal_reviewlistlabel(filename)
    if condition == 1: #1 means unigram
        vfeatureArray = cal_feature_array(vreviewlist,list_word)
    if condition == 2: #2 means bigram
        vfeatureArray = cal_bifeature_array(vreviewlist,list_word)
    if condition == 3: #3 means both
        vfeatureArray = cal_both_feature_array(vreviewlist,list_word)

    b =0
    count=0
    for idx in range(vreviewlist.__len__()):
        y = np.dot(w,vfeatureArray[idx]) + b
        if y>0:
            predict_label = 1
        else:
            predict_label = -1
        review_l = vreviewlabel[idx]
        if review_l != predict_label:
            count=count+1

    return(count)

review_list,review_label = cal_reviewlistlabel('train.csv')
print(review_list[0])
#print(calListbiWord(review_list).__len__())

list_uniWord = calListuniWord(review_list)
#feature_array = cal_feature_array(review_list,list_uniWord)
w10=perceptron(10,review_list,review_label,list_uniWord,cal_feature_array(review_list,list_uniWord))
print(w10)

print(calTrainError('train.csv',list_uniWord,w10,1))
print(calTrainError('validation.csv',list_uniWord,w10,1))

list_biWord = calListbiWord(review_list)
#print(list_biWord)

w_bi_10 = perceptron(10,review_list,review_label,list_biWord,cal_bifeature_array(review_list,list_biWord))
print(w_bi_10)

print(calTrainError('train.csv',list_biWord,w_bi_10,2))
print(calTrainError('validation.csv',list_biWord,w_bi_10,2))
list_bothWord = []
list_bothWord = list_uniWord + list_biWord

bothfeatureArray = cal_both_feature_array(review_list,list_bothWord)
w_both = perceptron(10,review_list,review_label,list_bothWord,bothfeatureArray)
print(w_both.__len__())
print(w_both)
print(calTrainError('train.csv',list_bothWord,w_both,3))
print(calTrainError('validation.csv',list_bothWord,w_both,3))