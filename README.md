# HW2-
Two online learning algorithms are implemented, the Perceptron algorithm and the Winnow algorithm. The observation of their performances in practice by running the algorithms over the movie review datasets. In the dataset, each line corresponds to a single snippet
which comes from a movie review and is labeled with either a positive or negative sign. The program learns the weights using a language model and then predict whether a given snippet is positive or negative. The dataset is split into training, validation, and test sets. The program uses the training set for learning weigh

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
