import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("Cleaned dataset.csv")
print(df.columns)

pivot_table=df.pivot_table(index="Year",columns="Month",values="Passenger Number")
print(pivot_table)
sns.heatmap(pivot_table)
plt.title("Passengers by Year and Month")
plt.show()


