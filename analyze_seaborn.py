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

import pandas as pd
# ['Type', 'Airline', 'Year', 'Month', 'Aircraft Number', 'Aircraft Hours',
#        'Aircraft Kilometres', 'Passenger Number', 'Passenger Kilometers',
#        'Seat Kilometers', 'Passenger Load Factor', 'Passenger Tonne Kilometer',
#        'Total Tonne Kilometer', 'Available Tonne Kilometer',
#        'Weight Load Factor']

# Example dataset
# df = pd.DataFrame({
#     "Category": ["A", "A", "B", "B", "C", "C"],
#     "Month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Feb"],
#     "Sales": [100, 120, 90, 110, 80, 95]
# })

# # Create pivot table
# pivot_table = df.pivot_table(index="Category", columns="Month", values="Sales", aggfunc="sum")
# print(pivot_table)
