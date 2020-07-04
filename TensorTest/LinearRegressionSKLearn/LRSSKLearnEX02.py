import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
import seaborn as sns

sns.set()


def adjusted_r_squared(n, p, r_squared_value):
    """
    calulates Ajusted Rsquare for the Input
    :param r_squared_value: int,
    :param p: int,
    :type n: int,
    """
    return 1 - (1 - r_squared_value) * (n - 1) / (n - p - 1)


data_input = pd.read_csv('real_estate_price_size_year.csv')
print(data_input.head())

x1 = data_input[['size', 'year']]
y1 = data_input['price']

# Initialize Linear Regression
regression = LinearRegression()
regression.fit(x1, y1)

# Get all Stats
print("Reg Co-Eff : ", regression.coef_)

print("Reg Intercept : ", regression.intercept_)

r_squared = regression.score(x1, y1)
print("RSquared : ", r_squared)

# Calculate Adjusted r_Squared
print("Adjusted R Square : ", adjusted_r_squared(x1.shape[0], x1.shape[1], r_squared))

# feature selection
f_values = f_regression(x1,y1)
print(f_values)


p_values = f_values[1].round(3)
print("p_values : ",p_values)

# creating summary table

reg_summary = pd.DataFrame(data=x1.columns.values,columns=['Features'])
reg_summary['Co-efficients'] = regression.coef_
reg_summary['p_value'] = p_values
print(reg_summary)

"""
        price     size  year
0  234314.144   643.09  2015
1  228581.528   656.22  2009
2  281626.336   487.29  2018
3  401255.608  1504.75  2015
4  458674.256  1275.46  2009
Reg Co-Eff :  [ 227.70085401 2916.78532684]
Reg Intercept :  -5772267.017463277
RSquared :  0.7764803683276794
Adjusted R Square :  0.7718717161282501
(array([285.92105192,   0.85525799]), array([8.12763222e-31, 3.57340758e-01]))
p_values :  [0.    0.357]
  Features  Co-efficients  p_value
0     size     227.700854    0.000
1     year    2916.785327    0.357

Process finished with exit code 0

"""

