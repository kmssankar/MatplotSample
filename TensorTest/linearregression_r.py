# Linear
#Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive and informative statistical graphics.
import numpy as np
import sklearn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
import seaborn as sb
from sklearn.model_selection import train_test_split

sb.set_style("whitegrid")
sb.set_context("poster")

# special matplotlib argument for improved plots
from matplotlib import rcParams

from sklearn.datasets import load_boston
boston = load_boston()

print(boston.keys())

print(boston.data.shape)

#Feature Names
print(boston.feature_names)
#Target Names
print(boston.target)
#DESCR
print(boston.DESCR)
#print(boston.items())


#Use DataFrame to load Data
bostonDf = pd.DataFrame(boston.data)
print(bostonDf.head(4))

# Add Column Headings to the DataFrame
bostonDf.columns = boston.feature_names
print("Boston Data Head : \n " , bostonDf.head(5))


#View the Shape of the Target
print("Boston Target Shape : " , boston.target.shape)

bostonDf['Price'] = boston.target

#After Adding target to main DataFrame

print("Boston Data with Target Head : \n " , bostonDf.head(5))

print("Boston DataFrame Description : " ,bostonDf.describe())

# Data preparation for Train and test

X = bostonDf.drop('Price',axis=1)
Y = bostonDf['Price']

X_train, X_test, Y_train, Y_test = train_test_split (X, Y, test_size = 0.22, random_state = 5)
print(" x_train Shape : ",X_train.shape , " Y_train Shape : " ,Y_train.shape ," X_test Shape : ",X_test.shape ," Y_test Shape : " ,Y_test.shape )

# Linear Regression

lm = LinearRegression()
lm.fit(X_train, Y_train)
Y_pred = lm.predict(X_test)
print("Mean squared error : " , sklearn.metrics.mean_squared_error(Y_test, Y_pred))
plt.scatter(Y_test, Y_pred)
plt.title("Predicted VS Actual Price")
plt.xlabel("Actual price")
plt.ylabel("Predicted price")
plt.show()

#Export Model
# save the model to disk
filename = 'Linear_Regression_model.sav'
joblib.dump(lm, filename)

loaded_model = joblib.load(filename)
result = loaded_model.score(X_test, Y_test)
print(result)











