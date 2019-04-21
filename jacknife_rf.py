import pandas as pd
import numpy as np
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier , GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

import pandas as pd
import os
from sklearn.metrics import accuracy_score , average_precision_score
from sklearn.metrics import confusion_matrix
import numpy as np


root_path = 'your path for descriptor'

train_data = []
for file in os.listdir(root_path):
    
    file_path = root_path + '\\' + file

    
    indata = np.load(file_path)[()]

    
#     train_data.extend(indata.toarray())
    train_data.extend(indata)

train_data = np.array(train_data)
train_data = pd.DataFrame(train_data)



train_data = train_data.sample(frac=1)  

X_train = train_data.iloc[:,:-1]
Y_train = train_data.iloc[:,-1]
X_train = np.array(X_train)
Y_train = np.array(Y_train)

root_pathone = ' your path for descriptor '

test_data = []
for file in os.listdir(root_pathone):
    
    file_path = root_pathone + '\\' + file

    
    indata = np.load(file_path)[()]

    
#     train_data.extend(indata.toarray())
    test_data.extend(indata)

test_data = np.array(test_data)
test_data = pd.DataFrame(test_data)
X_test = test_data.iloc[:,:-1]
Y_test = test_data.iloc[:,-1]
X_test = np.array(X_test)
Y_test = np.array(Y_test)

# #knn
# KNN = KNeighborsClassifier(n_neighbors=2)
# KNN.fit(X_train , Y_train)
# KNN_PRE = KNN.predict(X_test)
# #
# get_suucess_rate(Y_test , KNN_PRE)
# ACCURACY_KNN = accuracy_score(Y_test , KNN_PRE)
# print('accuracy knn:' , )

#rf
RFC = RandomForestClassifier(n_estimators=50)
RFC.fit(X_train , Y_train)
RFC_PRE = RFC.predict(X_test)

get_suucess_rate(Y_test , RFC_PRE)

ACCURACY_RFC = accuracy_score(Y_test , RFC_PRE)
print('all success rate:' , ACCURACY_RFC)



# #SVM
# SVMC = SVC()
# SVMC.fit(X_train , Y_train)
# SVM_PRE = SVMC.predict(X_test)
# get_suucess_rate(Y_test , SVM_PRE)
# ACCURACY_SVM = accuracy_score(Y_test , SVM_PRE)
# print('accuracy svm:' , ACCURACY_SVM)



# feat.shape=[n. d], label.shape=[n,]
res = np.zeros((X_test.shape[0], ))
for i in range(X_test.shape[0]):
    print(i)
    feat_tmp = np.delete(X_train, i, axis=0)
    label_tmp = np.delete(Y_train, i, axis=0)
    test_feat = X_test[i, :].reshape(1, X_test.shape[1])
    
    RF = RandomForestClassifier(n_estimators=50)
    RF.fit(feat_tmp, label_tmp)
    res[i] = RF.predict(test_feat)
    
con_mat = confusion_matrix(res, Y_train)
print(con_mat)