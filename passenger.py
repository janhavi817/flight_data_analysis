import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Cleaned dataset.csv")
print(df.info())
 #Total Passenger Traffic by Airline 
df.groupby("Airline")["Passenger Number"].sum().sort_values(ascending=False).plot(title="Passengers by Airline")
plt.ylabel("Passengers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()