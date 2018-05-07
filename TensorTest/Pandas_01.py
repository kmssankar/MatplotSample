# Import Pandas library
import pandas as pd
#read from CSV
Review =pd.read_csv("inp.csv")
#Read table -> Function using Delimiter
ReadCat =pd.read_table("inp.csv",sep=",")
print(ReadCat)
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
#iloc ->Get single row
print("*****  Iloc single row")
SinRow = Review.iloc[2]
print(SinRow)
#iloc ->Remove Header
print("*****  Iloc Remove header ")
RemHeader = Review.iloc[:,1:]
print(RemHeader)
print("*****  Reindexing the DataFrame ")
RevIdx = RemHeader.reindex
print(RevIdx)
print("*****  Display the index of the DataFrame ")
print(RemHeader.index)

#select specific columns using column name
print("*****  select specific columns using column name")
Speccols = Review["title"]
print("Speccols Type : ",type(Speccols))
print(Speccols.head())
#select specific columns using multiple columns
print("*****  select specific columns using multiple columns")
MultiCols =Review[["title", "release_year","score"]]
print(MultiCols)
print("MultiCols Type : ",type(MultiCols))

# Using Mean Function
print("*****  select specific columns and rows")
Speccols = Review.loc[0:2,"release_year"]
print(Speccols.head())

# Using Mean , count , min , max ,Median , Std deviation , Co-relation Function
print("*****  mean Function")
print("Mean of Score ",Review["score"].mean())
print("Count of Score ",Review["score"].count())
print("Min of Score ",Review["score"].min())
print("Max of Score ",Review["score"].max())
print("Median of Score ",Review["score"].median())
print("Std Deviation of Score ",Review["score"].std())
print("Std Co-relation of Score & release_year ")
print(Review[["score","release_year"]].corr())

#Using Mean to get mean of all numeric fields
print("******* Mean of all numeric fields in Dataframe")
print("Mean of All numeric fields : ",Review.mean())


