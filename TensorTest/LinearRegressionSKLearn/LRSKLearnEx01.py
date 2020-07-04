import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import seaborn as sns
sns.set()

data = pd.read_csv('real_estate_price_size.csv')
print (data)

x1=data['size']
y=data['price']

#Print X shape /Y Shape
print (x1.shape , " Y shape " , y.shape)

regression = lm.LinearRegression(n_jobs=2)

# we are providing vectors as parameters but fit requires 2D array
#regression.fit(x1,y)
"""
Fit method will throw error as below:
    "if it contains a single sample.".format(array))
ValueError: Expected 2D array, got 1D array instead:
array=[ 643.09  656.22  487.29 1504.75 1275.46  575.19  570.89  620.82  682.26

Fix:
----
use reshape to convert it to 2d Array
"""
xr =x1.values.reshape(-1,1)
yr =y.values.reshape(-1,1)
print (" xr shape " , xr.shape , " yr shape " , yr.shape)
regression.fit(xr,y)
print(regression)

# Get R-Squared
print (" R-Squared : ",regression.score(xr,yr))

#Get Coefficient
print (" Co-Efficient : ",regression.coef_)