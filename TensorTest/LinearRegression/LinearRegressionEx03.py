import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

#Read Data
raw_data = pd.read_csv('real_estate_price_size_year_view.csv')

print(raw_data.describe())

print (raw_data.head())

raw_data["view"] = raw_data["view"].map({"Sea view":1,"No sea view":0})

print (raw_data.head())

x1 = raw_data[["size","year","view"]]

print(x1)

y=raw_data["price"]

print(y)
x = sm.add_constant(x1)

print(x)

result=sm.OLS(y,x).fit()

print(result.summary())

#predict from model
new_data = pd.DataFrame({"const":1.0,"size":[700,600],"year":[2011,2013],"view":[0,1]})

new_data.rename(index={0:"house1",1:"house2"})
prediction = result.predict(new_data)

predictiondf = pd.DataFrame({"prediction" :prediction})
print(prediction)

new_data = new_data.join(predictiondf)

print(new_data)

