__author__ = 'penghao'
from numpy import *
import numpy as np

list = ['i', 'am', 'a', 'boy']
list_copy=[]
for item in list:
    if list.index(item) < list.__len__()-1:
        list_copy.append(list[list.index(item)] + ' ' + list[list.index(item)+1])
        print(list_copy)