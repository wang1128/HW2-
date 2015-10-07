# HW2-
All right reserved
- The numpy and csv function are imported. Numpy is used to calculate the perceptron and winnow algorithm.

- cal_reviewlistlabel() function is used to read the csv file. The parameter is filename. It return review_list, review_label. For the label part, if the label is '+', the review label is 1. Otherwise, the review label will be -1.

- calListuniWord(review_list) function is used to generate the list of uni-gram words and save them to the list_ word. When read the unigram word to the list, the frequency of the words are calculated. I delete the words that appears less then five time or more than 300 times. I do this because the most frequent words are the words like : the, a , film, an... These words are meaningless. Also, the words that appear in low frequency are deleted because they won't affect the weight too much.

- calListbiWord(review_list): function is used to generate the list of bi-gram words. It is pretty like calListuniWord(review_list). It is also remove the most common words and the words that appear only few times.

- cal_feature_array(review_list,list_word) cal_bifeature_array and cal_both_feature_array : is calculate the unigram,bigram and both feature set.

- perceptron() function is calculate w by using perceptron algorithm and feature sets.

- winnow() function is calculate w by using winnow algorithm and feature sets.

- calPrecsion_p() is to calculate precision.

- calRecall_p() is to calculate recall.
- calFscore() is to calculate F-score
- calTrainError_p() is to calculate accuracy
- calaprf() is to print out the precision, recall , Fscore and accuracy
