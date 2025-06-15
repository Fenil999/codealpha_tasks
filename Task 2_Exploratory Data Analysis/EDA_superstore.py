import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Superstore_Sales.csv", encoding='ISO-8859-1')

print(df.head())

print(df.info())

print(df.isnull().sum())

print(df.describe())

print(df['Category'].value_counts())

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Sales', y='Profit', hue='Category')
plt.title("Sales vs Profit by Category")
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Sub-Category', y='Profit')
plt.xticks(rotation=45)
plt.title("Profit by Sub-Category")
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

