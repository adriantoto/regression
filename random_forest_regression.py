# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:30:43 2019

@author: @adriantoto
"""

# Random Forest Regression

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
#X = pd.DataFrame(Xnd)
y = dataset.iloc[:, 2].values
#y = pd.DataFrame(ynd)

# Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
                                                    random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Fitting the Random Forest Regression Model to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=400, random_state=0)
regressor.fit(X, y ) 

# Predicting a new result with Random Forest Regression
y_pred = regressor.predict([[6.5]])

# Visualising the Random Forest Regression Results (higher resolution)
X_grid = np.arange(min(X), max(X),0.01)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X,y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Random Forest Regression model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show
