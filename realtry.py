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
        p="ARNDCEQZGMILMFPSTWYV"
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
        except Exception,ex:
            pass
    l1+=1

print(data)
##for i in range(1,len(value),2):
##    #print(value[i])
##    lr_rate=0.33
##    c=list(value[i])
##    nltk_tokens = nltk.word_tokenize("".join(c))
##    tokens.append(c)
##    tfidf = TfidfVectorizer()
##    val=lr_rate
##    X.append(c)
##    Y.append(random.randrange(2))

##from rdkit import DataStructs
##from rdkit import Chem
##from rdkit.Chem import AllChem
##ms = [Chem.MolFromSmiles('COC'), Chem.MolFromSmiles('CCO'),
## Chem.MolFromSmiles('COC')]
##fps = [Chem.RDKFingerprint(x) for x in ms]
##sim=DataStructs.FingerprintSimilarity(fps[0],fps[1])
##sim1=DataStructs.FingerprintSimilarity(fps[0],fps[2])
##
##sim2=DataStructs.FingerprintSimilarity(fps[1],fps[2])
##
##m2 = Chem.MolFromSmiles('COC')
##print(Chem.MolToMolBlock(m2))  
##
##res = AllChem.MMFFOptimizeMoleculeConfs(m2)
##print(res)


##for i in glob.glob(os.getcwd()+"\\DrugBank_Approved-PSSM\\*.pssm"):
##    #print(i)
##    f=open(i,"r")
##    con=f.read()
##    f.close()
##    v=con.split("\n")
##    q=[]
##    for t in v:
##        t=t.replace("\t", " ")
##        q.append(str(t))
##    tfidf = TfidfVectorizer()
##    vectors = tfidf.fit_transform(q)
##    #print(vectors)
##    X.append(str(vectors))
##    Y.append(random.randrange(2))
##
X=np.array(data)
Y=np.array(Y)
from nltk.tokenize import sent_tokenize, word_tokenize
##for i in X:
##    print(sent_tokenize(i)) 
X_train,X_test,y_train,y_test=train_test_split(X,Y, test_size=0.3, random_state=31)

lasso = Lasso()
lasso.fit(X_train,y_train)
filename = 'finalized_model.sav'
pickle.dump(lasso, open(filename, 'wb'))
train_score=lasso.score(X_train,y_train)
test_score=lasso.score(X_test,y_test)
coeff_used = np.sum(lasso.coef_!=0)
print(test_score)


