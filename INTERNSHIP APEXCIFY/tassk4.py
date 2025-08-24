import seaborn as sns
import pandas as pd

# 1. Load a small dataset (Titanic dataset)
df = sns.load_dataset("titanic")

# 2. Descriptive Statistics (quick overview)
print("----- Descriptive Statistics -----")
print(df.describe())

# 3. Mean
print("\n----- Mean -----")
print(df.mean(numeric_only=True))

# 4. Median
print("\n----- Median -----")
print(df.median(numeric_only=True))

# 5. Minimum values
print("\n----- Minimum -----")
print(df.min(numeric_only=True))

# 6. Maximum values
print("\n----- Maximum -----")
print(df.max(numeric_only=True))

# 7. Standard Deviation
print("\n----- Standard Deviation -----")
print(df.std(numeric_only=True))

# 🔹 Bonus: Missing Values
print("\n----- Missing Values -----")
print(df.isnull().sum())
