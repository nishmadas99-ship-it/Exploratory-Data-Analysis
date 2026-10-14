# Exploratory Data Analysis (EDA) Project

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("student_performance.csv")

# Display the dataset
print("STUDENT PERFORMANCE DATASET")
print(df)

# Display dataset information
print("\nDATASET INFORMATION")
print(df.info())

# Display the number of rows and columns
print("\nDATASET SHAPE")
print(df.shape)

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

# Display statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Average scores
print("\nAVERAGE STUDY HOURS:", df["Study_Hours"].mean())
print("AVERAGE ATTENDANCE:", df["Attendance"].mean())
print("AVERAGE FINAL SCORE:", df["Final_Score"].mean())

# Correlation analysis
print("\nCORRELATION MATRIX")
print(df[[
    "Study_Hours",
    "Attendance",
    "Previous_Score",
    "Final_Score"
]].corr())

# Create a folder for saving charts
import os
os.makedirs("plots", exist_ok=True)

# 1. Study hours vs final score
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Final_Score"
)
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("plots/study_hours_vs_score.png")
plt.show()

# 2. Distribution of final scores
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="Final_Score",
    bins=8,
    kde=True
)
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("plots/final_score_distribution.png")
plt.show()

# 3. Correlation heatmap
plt.figure(figsize=(8, 5))
correlation = df[[
    "Study_Hours",
    "Attendance",
    "Previous_Score",
    "Final_Score"
]].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png")
plt.show()

# 4. Average final score by gender
plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="Gender",
    y="Final_Score",
    errorbar=None
)
plt.title("Average Final Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Final Score")
plt.tight_layout()
plt.savefig("plots/average_score_by_gender.png")
plt.show()

# Identify the highest final score
top_student = df.loc[df["Final_Score"].idxmax()]

print("\nTOP-PERFORMING STUDENT")
print(top_student)

# Final findings
print("\nEDA PROJECT FINDINGS")
print("1. The dataset contains student academic information.")
print("2. Missing values and duplicate records were checked.")
print("3. Statistical summaries were generated.")
print("4. Correlations between academic factors were analyzed.")
print("5. Four visualizations were created and saved.")

print("\nEDA PROJECT COMPLETED SUCCESSFULLY!")
