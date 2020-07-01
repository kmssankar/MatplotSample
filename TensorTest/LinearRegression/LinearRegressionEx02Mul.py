import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()
#Read data
data_input = pd.read_csv('real_estate_price_size_year.csv')
print(data_input.describe())
#price         size         year

y=data_input['price']
print(y)

x4=data_input[["size", "price"]]

x1=data_input[["size", "year"]]
print (x1)

x2=data_input['size']

x3=data_input['year']

x=sm.add_constant(x1)
result = sm.OLS(y,x).fit()
print (result.summary())

yhat = -5.772e+06 + 227.7009 *x2 + 2916.7853 * x3


