# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# df=pd.read_csv("Cleaned dataset.csv")
# print(df.info())

# (df.groupby("Airline")["Aircraft Kilometres"].sum().sort_values(ascending=False).plot(title="Total Kilometers travelled"))
# plt.ylabel("Kilometers")
# plt.xlabel("Airlines")
# plt.xticks(rotation=45)
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("Cleaned dataset.csv")

# Group by Airline and sum the Aircraft Kilometres
km_per_airline = df.groupby("Airline")["Aircraft Kilometres"].sum().sort_values(ascending=False)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(km_per_airline.index, km_per_airline.values / 1e6, color='skyblue')  # Convert to millions for readability

# Highlight airline with max kilometers
bars[0].set_color('red')  # First bar is the highest after sort_values()
bars[1].set_color('orange')  
bars[2].set_color('yellow')  

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.1f}M',  # M = million
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)

# Labels and Title
plt.title("Total Kilometers Travelled by Each Airline\n(Higher kilometers may indicate more maintenance needs)")
plt.xlabel("Airline")
plt.ylabel("Kilometers (in Millions)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
