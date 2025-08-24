import seaborn as sns
import pandas as pd

# Load a small dataset (example: tips dataset)
df = sns.load_dataset("tips")

# Show first few rows
print("Dataset Preview:\n", df.head(), "\n")

# Descriptive statistics
print("Descriptive Statistics:\n", df.describe(), "\n")

# Mean of numeric columns
print("Mean:\n", df.mean(numeric_only=True), "\n")

# Median
print("Median:\n", df.median(numeric_only=True), "\n")

# Standard Deviation
print("Standard Deviation:\n", df.std(numeric_only=True), "\n")

# Minimum values
print("Minimum Values:\n", df.min(numeric_only=True), "\n")

# Maximum values
print("Maximum Values:\n", df.max(numeric_only=True), "\n")

# Bonus: Check for missing values
print("Missing Values:\n", df.isnull().sum(), "\n")
