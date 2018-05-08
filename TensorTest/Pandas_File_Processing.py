#Import Pandas
import pandas as pd

#Read from CSV file
ReadFile = pd.read_csv("cast.csv",index_col=None)
print("\n File content head\n",ReadFile.head())

print("\n File content head->3 \n",ReadFile.head(2))
print("\n File content tail\n",ReadFile.tail())
print("\n File content tail->4 \n",ReadFile.tail(4))

#Length of Input File
print("\nLength of the Readfile:",len(ReadFile))

#Create a dataframe with column
ReadFileCol = ReadFile['title']
print("\n DataFrame with Single column \n ",ReadFileCol)
print("\n Type of DataFrame with Single column \n ",type(ReadFileCol))
print("\n ReadFile of index : 74000 \n",ReadFile.ix[74000])

#Column > 1990
ReadFileColGt90 = ReadFile[(ReadFile['year'] > 2015) & (ReadFile['year'] <= 2017)]
ReadFileColGt90Srted = ReadFileColGt90.sort_values(by=['name'])
print("\n ReadFile with year > 2015 and < 2017 \n",ReadFileColGt90.head())
print("\n ReadFile with year > 2015 and < 2017 sorted \n",ReadFileColGt90Srted.head())







