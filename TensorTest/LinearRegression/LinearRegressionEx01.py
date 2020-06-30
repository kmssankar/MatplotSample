import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

data = pd.read_csv('real_estate_price_size.csv')
print (data)

x1=data['size']
y=data['price']

plt.scatter(x1,y)
plt.xlabel('size',fontsize=10,fontname='Arial')
plt.ylabel('price',fontsize=10,fontname='Arial')

#plt.show()

x=sm.add_constant(x1)
result = sm.OLS(y,x).fit()
print(result.summary())

yhat = x1* 223.1787 + 101900
plt.plot(x1,yhat,color='green',label='regression line')
plt.show()