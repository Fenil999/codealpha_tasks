import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load simplified CSV
df = pd.read_csv("co2_emissions.csv")

# Sort top emitters
top_emitters = df.sort_values(by="co2", ascending=False)

# Plot Top 10 CO2 Emitters
plt.figure(figsize=(10,6))
sns.barplot(x="co2", y="country", data=top_emitters, palette="Reds_r")
plt.title("Top 10 CO2 Emitting Countries (2021)")
plt.xlabel("CO2 Emissions (Million Tonnes)")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# Correlation Heatmap
numeric_cols = ['co2', 'co2_per_capita', 'gdp', 'population']
plt.figure(figsize=(8,6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between CO2, GDP, and Population")
plt.tight_layout()
plt.show()
