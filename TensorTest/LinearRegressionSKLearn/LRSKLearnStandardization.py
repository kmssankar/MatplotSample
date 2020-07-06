# Standardization or feature scaling
# (x - mean )/standard Deviation makes mean 0 and SD as 1.
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
sns.set()

data = pd.read_csv('real_estate_price_size.csv')
print(data)

x1 = data['size']
y = data['price']

# Print X shape /Y Shape
print(x1.shape, " Y shape ", y.shape)

x1_reshaped = x1.values.reshape(-1,1)
scalar = StandardScaler()
scalar.fit(x1_reshaped)
print(scalar)

x_scaled = scalar.transform(x1_reshaped)

print(x_scaled)
