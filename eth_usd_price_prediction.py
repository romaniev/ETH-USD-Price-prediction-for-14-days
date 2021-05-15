# -*- coding: utf-8 -*-
"""ETH-USD Price prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bc--3ZmZRJgDf_hdl3BzWrTz-UQzAeQF
"""

#Predict ETH price

#Import libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas_datareader as web
import matplotlib.pyplot as plt

#Read data 
#get quote from stocks
df= web.DataReader('ETH-USD', data_source='yahoo', start='2019-01-01', end='2021-05-02')
df.head()

#Create a variable of the horizion that want to predict
projection=14
#Create a new column called prediction
df['Prediction']=df[['Close']].shift(-projection)
df

#Create the indipendent dataset (X)
X=np.array(df['Close'])
#Remove the last 14 rows
X=X[:-projection]

#Create a dipendent dataset (y)
y=df['Prediction'].values
y=y[:-projection]

#Split the model in 85% train and 15% testing dataset
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=.15)
x_train=x_train.reshape((-1, 1))
print(x_train)

#Create and train the model
linReg=LinearRegression()
#Train the model
linReg.fit(x_train, y_train)

#Test model using score
x_test=x_test.reshape((-1, 1))

linReg_confidence=linReg.score(x_test,y_test)
print("Linear regression confidence=",linReg_confidence)

#Create a variable callde x_projection and set it equal to the last 14 rows of data from the original dataset
x_projection=np.array(df[['Close']])[-projection:]
x_projection=x_projection.reshape((-1, 1))

print(x_projection)

#Print the model regression for the next 14 days
linReg_prediction=linReg.predict(x_projection)
print(linReg_prediction)