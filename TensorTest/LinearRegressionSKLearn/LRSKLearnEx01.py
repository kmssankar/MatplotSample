import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import seaborn as sns
sns.set()

data = pd.read_csv('real_estate_price_size.csv')
print(data)

x1 = data['size']
y = data['price']

# Print X shape /Y Shape
print (x1.shape , " Y shape " , y.shape)

regression = lm.LinearRegression(n_jobs=2)

# we are providing vectors as parameters but fit requires 2D array
# regression.fit(x1,y)
"""
Fit method will throw error as below:
    "if it contains a single sample.".format(array))
ValueError: Expected 2D array, got 1D array instead:
array=[ 643.09  656.22  487.29 1504.75 1275.46  575.19  570.89  620.82  682.26

Fix:
----
use reshape to convert it to 2d Array
"""
xr = x1.values.reshape(-1,1)
yr = y.values.reshape(-1,1)
print(" xr shape ", xr.shape, " yr shape ", yr.shape)
regression.fit(xr,y)
print(regression)

# Get R-Squared
print(" R-Squared : ",regression.score(xr,yr))

# Get Coefficient
print(" Co-Efficient : ",regression.coef_)

# run an input
predict_data = pd.DataFrame(data=[2300,1900],columns=['size'])

print( "predict_data Shape : ",predict_data.shape,"\n",predict_data)

predicted_result = regression.predict(predict_data)

print(" prediction for size ", predict_data,"\n",predicted_result)

# Join data to the existing Input
predicted_df = pd.DataFrame({"predicted_result":predicted_result})
result_out = predict_data.join(predicted_df)

print(result_out)

# plot the regression

yhat = regression.coef_ * xr + regression.intercept_
plt.scatter(xr,yr)
plt.plot(xr,yhat,color='green')
plt.xlabel('size',fontsize=10)
plt.ylabel('price',fontsize=10)
plt.show()


# output
"""
C:\Users\Sankar\PycharmProjects\MlProj01\venv\Scripts\python.exe C:/Users/Sankar/PycharmProjects/MlProj01/TensorTest/LinearRegressionSKLearn/LRSKLearnEx01.py
         price     size
0   234314.144   643.09
1   228581.528   656.22
2   281626.336   487.29
3   401255.608  1504.75
4   458674.256  1275.46
5   245050.280   575.19
6   265129.064   570.89
7   175716.480   620.82
8   331101.344   682.26
9   218630.608   694.52
10  279555.096  1060.36
11  494778.992  1842.51
12  215472.104   694.52
13  418753.008  1009.25
14  444192.008  1300.96
15  440201.616  1379.72
16  248337.600   690.54
17  234178.160   623.94
18  225451.984   681.07
19  299416.976  1027.76
20  268125.080   620.71
21  171795.240   549.69
22  412569.472  1207.45
23  183459.488   518.38
24  168047.264   525.81
25  362519.720  1103.30
26  271793.312   570.89
27  406852.304  1334.10
28  297760.440   681.07
29  368988.432  1496.36
..         ...      ...
70  276875.632  1021.95
71  181587.576   643.41
72  298926.496   656.22
73  211724.096   549.80
74  228313.024   685.48
75  286161.600   685.48
76  382120.152  1183.46
77  365863.936  1334.10
78  251560.040   682.26
79  342988.456  1188.62
80  180307.216   681.07
81  408637.816  1122.34
82  190909.056   681.07
83  282683.544   643.09
84  303597.216   685.48
85  376253.808  1009.25
86  154282.128   479.75
87  327252.112  1028.41
88  211904.536   601.66
89  354512.112  1236.93
90  251140.656   694.52
91  338078.168  1071.55
92  298170.880   694.52
93  266684.248   698.29
94  262477.856   698.29
95  252460.400   549.80
96  310522.592  1037.44
97  383635.568  1504.75
98  225145.248   648.29
99  274922.856   705.29

[100 rows x 2 columns]
(100,)  Y shape  (100,)
 xr shape  (100, 1)  yr shape  (100, 1)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=2, normalize=False)
 R-Squared :  0.7447391865847586
 Co-Efficient :  [223.17874259]
predict_data Shape :  (2, 1) 
    size
0  2300
1  1900
 prediction for size     size
0  2300
1  1900 
 [615223.70976883 525952.21273098]
   size  predicted_result
0  2300     615223.709769
1  1900     525952.212731
End

Process finished with exit code 0

"""
print('End')
