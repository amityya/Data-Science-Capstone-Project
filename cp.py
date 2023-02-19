
#importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import *
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor

#importing data
df = pd.read_csv('CAR DETAILS.csv')

lst=[i.split(' ')[0] for i in df['name']]
df['manufacturer']=lst


#deleting uncessary rows and columns
d1=df['manufacturer'].value_counts()
w=d1[d1.values<10].index
q=list(w)

for i in q:
    w=df[df['manufacturer']==i].index
    for j in list(w):
      df.drop(j,inplace=True)


df.drop(columns=['name'],axis=1,inplace=True)
df.drop_duplicates(inplace=True)



# get dummies
df=pd.get_dummies(data=df,columns=['fuel','seller_type','owner','transmission','manufacturer'])

#separating dependent and independent variable
x=df.drop(columns=['selling_price'],axis=1)
y=df['selling_price']



# building models


bg=BaggingRegressor(base_estimator=rf,n_estimators=5,random_state=25)
bg.fit(x,y)

# saving models
import pickle
pickle.dump(bg,open('bagging.pkl','wb'))

