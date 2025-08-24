import pandas as pd
import matplotlib.pyplot as plt

# Load sales data (make sure sales.csv is in the same folder)
df = pd.read_csv("sales.csv")

# Plot sales trend
plt.plot(df["Month"], df["Sales"], marker="o")

# Add labels and title
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")

# Show the chart
plt.show()
