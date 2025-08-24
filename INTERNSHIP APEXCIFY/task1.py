
import pandas as pd

# Load CSV file (students.csv should be in the same folder as this script)
df = pd.read_csv("students.csv")

# Calculate each student's average score
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)

# Find the student with the highest average
top_student = df.loc[df["Average"].idxmax()]

# Show results
print("All Students with Averages:\n", df)
print("\nStudent with Highest Average:\n", top_student)
