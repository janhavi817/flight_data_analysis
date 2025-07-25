import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Cleaned dataset.csv")
print(df.info())


# Year-wise Total Passenger Count
plt.figure(figsize=(8, 5))
yearly_passengers = df.groupby("Year")["Passenger Number"].sum()
yearly_passengers.plot(kind="line", marker="o", title="Total Passengers Over Years")
plt.xlabel("Year")
plt.ylabel("Passenger Count")
plt.grid(True, linestyle='--', alpha=0.5)

# Annotate the drop in 2020
if 2020 in yearly_passengers.index:
    plt.annotate("COVID-19 impact",
                 xy=(2020, yearly_passengers[2020]),
                 xytext=(2017, yearly_passengers[2020]*1.2),
                 arrowprops=dict(facecolor='red', arrowstyle="->"),
                 fontsize=10,
                 color='red')

plt.tight_layout()
plt.show()

