import pandas as pd
import numpy as np
#READING AND BASIC INFORMATION
df=pd.read_csv("carrier.csv")
print(df.head())
print(df.tail())
print(df.columns)


# DROOPING LESS IMPORTANT COLUMNS
dropped_columns=['Freight', 'Mail',
       'Total Cargo',  'Mail Tonne Kilometer',
       'Freight Tonne Kilometer']
df.drop(columns=dropped_columns,axis=1,inplace=True)
print(df.info())

#CHECKING MISSING VALUES
print(f"Missing values in the dataset: {df.isnull().sum()}")

#FILLING VALUES OF IMPORTANT COLUMNS WITH MEAN

df["Passenger Load Factor"] = df["Passenger Load Factor"].fillna(df["Passenger Load Factor"].mean())
df["Weight Load Factor"] = df["Weight Load Factor"].fillna(df["Weight Load Factor"].mean())


#DROPPING LESS IMPORTANT ROWS

df.dropna(subset=["Passenger Number", "Aircraft Hours", "Aircraft Kilometres","Passenger Kilometers","Seat Kilometers","Total Tonne Kilometer" ,   
"Available Tonne Kilometer" ],inplace=True)

print(df.describe)

df.to_csv("Cleaned dataset.csv",index=False)