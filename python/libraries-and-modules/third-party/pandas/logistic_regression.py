import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import random as ra


#### Read in and Inspect Data ####
data_path = "data analysis (pandas)\iris.csv"
df = pd.read_csv(data_path)

# Check the dataset
df.info()
print()

#Show first 10 rows
print(df.head(10))
print()

# Check the output flower types
print(df['variety'].value_counts())
print()


#### Split into Features and Labels ####
# Features(X) - The independent variables, or predictors
# Label(y) - The dependent variables, or values to be predicted
X = df.iloc[:, :-1].values

# Grab all rows, and only the last column
y = df.iloc[:, -1].values

# What does X look like
print('\nThe shape of X is: ', X.shape)
print(X[:5])
print()

# What does Y look like
print('\nThe shape of y is: ', y.shape)
print(y[:5])
print()
