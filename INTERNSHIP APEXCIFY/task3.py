import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load survey data
df = pd.read_csv("survey.csv")

# Count satisfaction levels
counts = df["Satisfaction"].value_counts()

# Print counts
print("Survey Results:\n", counts)

# Plot bar chart
sns.barplot(x=counts.index, y=counts.values, palette="viridis")

# Add title and labels
plt.title("User Satisfaction Survey Results")
plt.xlabel("Satisfaction Level")
plt.ylabel("Number of People")

# Show the chart
plt.show()
