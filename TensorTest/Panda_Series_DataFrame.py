# Import Pandas
from typing import List

import pandas as pd

#Converting tuple to Series
Tup = ('Sankar', 'Ashok',123,35.17,'2018-07-05')
TupSer = pd.Series(Tup)
print (TupSer)
print ("TupSer Type :",type(TupSer))

#Dictonary to Series

Dict ={'Name':'sankar','Designation':'Associte','City':'Erode'}
DictSer = pd.Series(Dict)
print(DictSer)
print("DictSer :" ,type(DictSer))

#DataFrame ->Pandas

DFSrc = {'Name':['Sankar','Johnson','Ashok'],'Experience':[6,10,2],'Technology':['Python','Java','Java']}
PdDataFrame = pd.DataFrame(DFSrc);
print (PdDataFrame)
print("PdDataFrame Type ",type(PdDataFrame))

#Set index as a column
PdChgIdx = PdDataFrame.set_index("Name")
print (PdChgIdx)
print("PdChgIdx Type ",type(PdChgIdx))

#Add Addtional Columns
PdAddColum =PdDataFrame
PdAddColum['Nationality'] ="Indian"
print (PdAddColum)
print("\nPdAddColum Type ",type(PdAddColum))

#Add Custom Index
IdxDF = {'Idx':['Idx1', 'Idx2', 'Idx3']}
PdIdx = pd.DataFrame(IdxDF)
print("\nPD DF Index : " ,PdIdx)
PdAddColum.index=PdIdx["Idx"]
print ("\nAfter Adding Index \n ",PdAddColum)
print("\nPdAddColum Type ",type(PdAddColum))

# Select column based on the Rows or Index
print("\nSelect Rows based on index \n ",PdAddColum.ix['Idx1'])
print("\nSelect column based on Column Name \n ",PdAddColum['Technology'])
print("\nSelect Rows based on index Range and Column \n ",PdAddColum.ix[:'Idx2','Name'])
print("\nSelect Rows based on index and Multi Column \n ",PdAddColum.ix[:'Idx2',['Name','Nationality']])

#Delete a column
PdDelColumn = PdAddColum.drop('Nationality', axis=1)
print("\nPdAddColum After dropping column \n ",PdDelColumn,"\nType",type(PdDelColumn))

del PdDelColumn['Technology']
print("\nPdAddColum After dropping column using del\n ",PdDelColumn,"\nType",type(PdDelColumn))



