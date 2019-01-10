# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 08:47:14 2018

@author: @adriantoto
"""

# Data Reprocessing 

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing Dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
#X = pd.DataFrame(Xnd)
y = dataset.iloc[:, 3].values
#y = pd.DataFrame(ynd)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
                                                    random_state = 0)

"""# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#----------------------------------------------------ANOTHER STEPS, IF ONLY NEEDED-------------------------------------------------------

"""# Taking care of missing  data ----> after Importing Dataset
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])"""

"""# Encoding categorical data -----> before Splitting The Dataset into the Training Set and Test Set
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
# Encoding dependent variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)"""
