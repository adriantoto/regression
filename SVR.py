# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:43:18 2019

@author: LENOVO
"""
# SVR 

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X =  dataset.iloc[:, 1:2].values
#X = pd.DataFrame(Xnd)
y = dataset.iloc[:, 2:3].values
#y = pd.DataFrame(ynd)

# Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
                                                    random_state = 0)"""

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Fitting the SVR Model to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

# Predicting a new result with SVR
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

# Visualising the SVR Results 
plt.scatter(X,y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SVR model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show

# Visualising the SVR Results (higher resolution)
X_grid = np.arange(min(X), max(X),0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X,y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (SVR model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show
