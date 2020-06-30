import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('Simple linear regression.csv')
print (data)

data.describe()

gpa =   1850 * 0.0017 + 0.2750 * 0.05
print(gpa)

x1 = data['SAT']
y = data['GPA']

plt.scatter(x1,y)
plt.xlabel('SAT',fontsize=10,fontname='Arial')
plt.ylabel('GPA',fontsize=10,fontname='Arial')
plt.show()

#Use Stats model
x = sm.add_constant(x1)
result = sm.OLS(y,x).fit()
print (result.summary())
