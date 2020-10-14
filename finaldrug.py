from __future__ import division
import math
from Bio.SeqUtils.ProtParam import ProteinAnalysis
f=open("DrugBank_Approved.txt","r")
t=f.read()
f.close()
vals=t.split("\n")
print(len(vals))

class FrequencyPositionMatrix():
    
    def scoring(self, pscores,p):
        for i in range(len(p)):
            pass
            #print(p[i])
        #print("\n")
        for i in range(79):
            pass
            #print(i+1,":")
            for j in range(len(p)):
                pass
                #print('%2.3f'%pscores[i][j])
            #print("\n")


class PositionWeightMatrix():
    

    def calcu(self,content):
        scorevals=[]
        vals=content.split("\n")
        p="ARNDCEQZGMILFPSTWYV"
        #print(len(vals))
        for i in range(1,5,2):
            try:
                print("-->",vals[i])
                n=1
                s=[]
                s.append(vals[i])
                
                s1=s[0]
                l=len(s1)
                sc=[[0.0 for i in range(l*4)] for j in range(len(p)*4)]
                for i in range(79):
                    for j in range(len(p)):
                        m=1
                        for k in range(n):
                            if p[j]==s[k][i]:
                                m=m+1
                        v=m/(20+n)
                        a=v/0.05
                        sc[i][j]=math.log(a/math.log(10))
                #print("The scoring matrix is:")
                for i in range(len(p)):
                    pass
                    #print(p[i])
                #print("\n")
                for i in range(79):
                    pass
                    #print(i+1,":")
                    for j in range(len(p)):
                        #print('%2.3f'%sc[i][j])
                        scorevals.append('%2.3f'%sc[i][j])
            except:
                pass
                #print("\n")

##        pssm = FrequencyPositionMatrix()
##        pssm.scoring(score,en)
        return scorevals

data=[]
f=open("DrugBank_Approved.txt","r")
content=f.read()
f.close()
value=content.split("\n")
print(len(vals))
a=PositionWeightMatrix()
scorevalue=a.calcu(content)
print(scorevalue)
from sklearn.externals import joblib
import datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score as vals
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import os,glob
import pickle
from os import path
import math 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np# difference of lasso and ridge regression is that some of the coefficients can be zero i.e. some of the features are 
# completely neglected
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import numpy as np
import nltk
tokens=[]
#print(vals)
X=[]
trgt=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
Y=[]
l1=0
for i in glob.glob(os.getcwd()+"\\datas\\*.txt"):
    f=open(i,"r")
    con=f.read()
    f.close()
    content=con.split("\n")
    
    for j in range(1,len(content),2):
        try:
            print(content[j-1])
            a=PositionWeightMatrix()
            scorevalue=a.calcu(content[j])
            X = ProteinAnalysis(content[j])
            p1=[]
            p2=[]
            l=[]
            for q in trgt:
                t1=X.get_amino_acids_percent()[q]
                t2=X.count_amino_acids()[q]
                p1.append(t1)
                p2.append(t2)

            d=X.molecular_weight()

            e=X.aromaticity()

            f=X.instability_index()

            g=X.isoelectric_point()
            for q in p1:
                l.append(q)
            for q in p2:
                l.append(q)
            l.append(d)
            l.append(e)
            l.append(f)
            l.append(g)
            data.append(l)
            Y.append(l1)
        except Exception as ex:
            pass
    l1+=1



X=np.array(data)
Y=np.array(Y)
from nltk.tokenize import sent_tokenize, word_tokenize
##for i in X:
##    print(sent_tokenize(i)) 
X_train,X_test,y_train,y_test=train_test_split(X,Y, test_size=0.3, random_state=31)
print(X_train)
lasso = Lasso()
lasso.fit(X_train,y_train)
filename = 'finalized_model.sav'
pickle.dump(lasso, open(filename, 'wb'))
print(lasso)
train_score=lasso.score(X_train,y_train)
test_score=lasso.score(X_test,y_test)
coeff_used = np.sum(lasso.coef_!=0)
print(test_score)


from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE # doctest: +NORMALIZE_WHITESPACE
X, y = make_classification(n_classes=2, class_sep=2,
 weights=[0.1, 0.9], n_informative=3, n_redundant=1, flip_y=0,
 n_features=20, n_clusters_per_class=1, n_samples=1000, random_state=10)
print('Original dataset shape %s' % Counter(y))
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_train, y_train)
print('Resampled dataset shape %s' % Counter(y_res))
filename = 'finalized_smote.sav'
pickle.dump(lasso, open(filename, 'wb'))

from sklearn.ensemble import RandomForestClassifier
data1=[]
a12=0
lbl=[]
for i in glob.glob(os.getcwd()+"\\pos\\*.fa"):
    f=open(i,"r")
    con=f.read()
##    print("con  ",con)
    f.close()
    
    
    content=con.split("\n")
    print(content[0])
    for j in range(1,len(content),2):
        
        X = ProteinAnalysis(content[j])
        p1=[]
        p2=[]
        l=[]
        for q in trgt:
            t1=X.get_amino_acids_percent()[q]
            t2=X.count_amino_acids()[q]
            p1.append(t1)
            p2.append(t2)

        d=X.molecular_weight()

        e=X.aromaticity()

        f=X.instability_index()

        g=X.isoelectric_point()
        for q in p1:
            l.append(q)
        for q in p2:
            l.append(q)
        l.append(d)
        l.append(e)
        l.append(f)
        l.append(g)
        data1.append(l)
        lbl.append(a12)
    a12+=1

import random
z = list(zip(data1, lbl))
random.shuffle(z)
a, b = zip(*z)
X_train,X_test,y_train,y_test=train_test_split(a,b, test_size=0.3, random_state=31)

clf = RandomForestClassifier(max_depth=2, random_state=0)
print(clf)
clf.fit(X_train, y_train)
RandomForestClassifier(max_depth=2, random_state=0)
print(clf.feature_importances_)

filename = 'finalized_rf.sav'
pickle.dump(clf, open(filename, 'wb'))


loaded_model = pickle.load(open(filename, 'rb'))
scr = loaded_model.score(X_test,y_test)
print("score: ",scr)
result = loaded_model.predict([data1[0]])
print("result",result)
print("ytest",y_test[0])

import numpy as np
from sklearn.model_selection import KFold
X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([1, 2, 3, 4])
kf = KFold(n_splits=2)
kf.get_n_splits(X)

print(kf)
KFold(n_splits=2, random_state=None, shuffle=False)
for train_index, test_index in kf.split(X):
     print("TRAIN:", train_index, "TEST:", test_index)
     X_train, X_test = X[train_index], X[test_index]
     y_train, y_test = y[train_index], y[test_index]
##from collections import Counter
##from sklearn.datasets import make_classification
##from imblearn.over_sampling import SVMSMOTE
##from matplotlib import pyplot
##from numpy import where
### define dataset
##X, y = make_classification(n_samples=10000, n_features=2, n_redundant=0,
##	n_clusters_per_class=1, weights=[0.99], flip_y=0, random_state=1)
### summarize class distribution
##counter = Counter(y)
##print(counter)
### transform the dataset
##oversample = SVMSMOTE()
##X, y = oversample.fit_resample(X, y)
### summarize the new class distribution
##counter = Counter(y)
##print(counter)
### scatter plot of examples by class label
##for label, _ in counter.items():
##	row_ix = where(y == label)[0]
##	pyplot.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))
##pyplot.legend()
##pyplot.show()

