#A stock prediction python program using machine learning models

import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split


#Get the data using quandl
df = quandl.get('WIKI/GME')
#Look at the data collected
print(df.head())

#Get the adjusted close price for the stock
df = df[['Adj. Close']]
#Look at the new data collected
print(df.head())

#A variable for predicting 'n' days into the future
forecast_out = 30
#Create another column shifted n units up
df['Prediction'] = df['Adj. Close'].shift(-forecast_out)
#Print the new set
print(df.tail())

#Create the independent data set (x)
#Convert the data into a numpy array
X = np.array(df.drop(['Prediction'],1))
#Remove the last n rows
X = X[:-forecast_out]
print(X)

#Create the dependent data set (y)
#Convert the data into a numpy array
y = np.array(df['Prediction'])
#Get all of the y values except the last n rows
y = y[:-forecast_out]
print(y)

#Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#Create and train the Support Vector Machine
svr_rbf = SVR(kernel = 'rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

#Testing Model: Score returns the coefficient of determination R^2 of the prediction
#The best possible score is 1.0
svm_confidence = svr_rbf.score(x_test, y_test)
print("svm_confidence: ", svm_confidence)

#Create and train the Linear Regression Model
lr = LinearRegression()
#Train the model
lr.fit(x_train, y_train)

#Testing Model: Score returns the coefficient of determination R^2 of the prediction
#The best possible score is 1.0
lr_confidence = lr.score(x_test, y_test)
print("lr_confidence: ", lr_confidence)

#Set x_forecast to the last 30 rows of the data from Adj. Close column
x_forecast = np.array(df.drop(['Prediction'],1))[-forecast_out:]
print(x_forecast)

#Print linear regression model for the next n days
lr_prediction = lr.predict(x_forecast)
print(lr_prediction)

#Print support vector regression model for the next n days
svm_prediction = svr_rbf.predict(x_forecast)
print(svm_prediction)

