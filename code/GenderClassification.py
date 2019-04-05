#from MovieLensData import load_user_item_matrix, load_gender_vector, load_user_item_matrix_100k, load_user_item_matrix_1m, load_gender_vector_1m
import MovieLensData as MD
import Classifiers
from Utils import one_hot
import numpy as np
from sklearn.feature_selection import f_regression, f_classif


def one_million(classifier):
    max_user = 6040
    max_item = 3952
    X = MD.load_user_item_matrix_1m()  # max_user=max_user, max_item=max_item)
    T = MD.load_gender_vector_1m()  # max_user=max_user)
    X = MD.normalize(X)
    #X = MD.feature_selection(X, T, f_regression)
    #X = MD.chi2_selection(X, T)
    print(X.shape)
    print(np.std(X,axis=0), len(np.std(X, axis=0)))
    classifier(X, T)


def one_hundert_k(classifier):
    X = MD.load_user_item_matrix_100k()  # max_user=max_user, max_item=max_item)
    T = MD.load_gender_vector()  # max_user=max_user)
    #X = MD.chi2_selection(X, T)

    classifier(X, T)


def one_hundert_k_obfuscated(classifier):
    X = MD.load_user_item_matrix_100k_masked()  # max_user=max_user, max_item=max_item)
    T = MD.load_gender_vector()  # max_user=max_user)
    #X = MD.chi2_selection(X, T)

    classifier(X, T)


if __name__ == '__main__':
    # load the data, It needs to be in the form N x M where N_i is the ith user and M_j is the jth item. Y, the target,
    # is the gender of every user
    import timeit
    start = timeit.default_timer()

    #max_user = 6040
    #max_item = 3952
    #X = MD.load_user_item_matrix_1m()#max_user=max_user, max_item=max_item)
    #T = MD.load_gender_vector_1m()#max_user=max_user)

    #print(X.shape, T.shape)
    #OH_T = [one_hot(int(x), 2) for x in T]
    #Classifiers.log_reg(X, T)
    #Classifiers.MLP_classifier(X, T, max_item)

    one_million(Classifiers.prior)

    stop = timeit.default_timer()
    print('Time: ', stop - start)


# SVM AUC: 0.79 +- 0.02 CV recall: 0.8173577335277402 CV precision: 0.8321544547101147
# svm rbf AUC: 0.86 +-0.02 CV recall: 0.96028671470078 CV precision: 0.7988469786349818
# log reg AUC: 0.81 CV recall: 0.8323666201934845 CV precision: 0.8386711692966065
# MLP AUC:  CV recall: 0.8549914326156598 CV precision: 0.7159403232729369
# naive bayes AUC: 0.56 +- 0.02 CV recall: 0.23274603292855547 CV precision: 0.8463640876689859
# MN bayes AUC: 0.81 +- 0.03 CV recall: 0.768882302231777 CV precision: 0.8897811875641992
# b bayes AUC: 0.77 +- 0.03 CV recall: 0.47657113057545153 CV precision: 0.8824519431822766



# ------------------- with chi2 feature selection
# SVM AUC: 0.78 +- 0.02 CV recall: 0.8018848245548685 CV precision: 0.8282078648271979 (same for p<0.1 and p<0.001)
# svm rbf AUC: 0.85 +- 0.02 CV recall: 0.9528985430125264 CV precision: 0.8050422639305786
# log reg AUC: 0.80 CV recall: 0.8252141846085077 CV precision: 0.8378892449626741
# MLP AUC:
# naive bayes AUC:
# MN bayes AUC:
# b bayes AUC:

# ------------------ different feature selections:
# chi2 : SVM AUC: 0.78 +- 0.02 CV recall: 0.8018848245548685 CV precision: 0.8282078648271979
# f_classif: SVM AUC: 0.78 +- 0.02 CV recall: 0.8002820319068551 CV precision: 0.8277579831118793
# f_regression SVM AUC: 0.78 +- 0.02 CV recall: 0.8002820319068551 CV precision: 0.8277579831118793

