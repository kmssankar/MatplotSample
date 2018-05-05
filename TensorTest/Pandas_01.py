# Import numpy and Pandas
import numpy as np
import pandas as pd
#read from CSV
Review =pd.read_csv("D:\PythonDev\inp.csv")
print("******** Shape of a dataframe ******** ")
#shape -> shows the shape of the dataframe
print(Review.shape)
print("********************")
#head ->  first N rows (parameter provided)
print("******** Using head ******** ")
print(Review.head(2))
print("********************")
#tail ->  last N rows (parameter provided)
print("******** Using tail ******** ")
print(Review.tail(2))
print("********************")
#iloc ->Gets rows and columns based on range provided
print("*******  Using iloc ********* ")
DFiloc =Review.iloc[0:5,0:3]
print(DFiloc)