
# COVID-19 DATA ANALYSIS PROJECT

# 1. Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Importing the dataset
df = pd.read_csv("covid_19_data.csv")

print("\n========== COVID-19 DATASET ==========")
print(df.head())

# 3. Exploring the dataset
print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# 4. Data cleaning
df.columns = df.columns.str.strip()

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

numeric_columns = ["Confirmed", "Deaths", "Recovered"]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(0)

df = df.dropna(subset=["Date", "Country/Region"])

print("\nCleaned Dataset:")
print(df.head())

# 5. Total cases by country
country_data = df.groupby("Country/Region")[
    ["Confirmed", "Deaths", "Recovered"]
].max()

country_data = country_data.sort_values(
    by="Confirmed", ascending=False
)

print("\nTop 10 Countries by Confirmed Cases:")
print(country_data.head(10))

# 6. Overall COVID-19 statistics
total_confirmed = int(df["Confirmed"].max())
total_deaths = int(df["Deaths"].max())
total_recovered = int(df["Recovered"].max())

print("\n========== COVID-19 SUMMARY ==========")
print("Maximum Confirmed Count:", total_confirmed)
print("Maximum Death Count:", total_deaths)
print("Maximum Recovered Count:", total_recovered)

# 7. Grouping data by date
daily_data = df.groupby("Date")[
    ["Confirmed", "Deaths", "Recovered"]
].sum().sort_index()

print("\nDaily Data:")
print(daily_data.head())

# 8. Line graph
plt.figure(figsize=(10, 5))

daily_data.plot(
    y=["Confirmed", "Deaths", "Recovered"],
    kind="line",
    figsize=(10, 5)
)

plt.title("COVID-19 Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Reported Counts")
plt.grid(True)
plt.tight_layout()
plt.savefig("covid_line_graph.png")
plt.show()

# 9. Bar chart - Top 10 countries
top_countries = country_data.head(10)

top_countries["Confirmed"].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 10 Countries by Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("covid_bar_chart.png")
plt.show()

# 10. Pie chart - Overall reported totals
plt.figure(figsize=(7, 7))

plt.pie(
    [total_deaths, total_recovered],
    labels=["Deaths", "Recovered"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Reported Deaths vs Recoveries")
plt.tight_layout()
plt.savefig("covid_pie_chart.png")
plt.show()

# 11. Bar chart - Confirmed, deaths, recovered
plt.figure(figsize=(8, 5))

plt.bar(
    ["Confirmed", "Deaths", "Recovered"],
    [total_confirmed, total_deaths, total_recovered]
)

plt.title("COVID-19 Overall Statistics")
plt.ylabel("Reported Counts")
plt.tight_layout()
plt.savefig("covid_summary_bar.png")
plt.show()

# 12. Additional Pandas analysis
print("\nCountry-wise average confirmed cases:")
print(df.groupby("Country/Region")["Confirmed"].mean().head(10))

print("\nMaximum reported deaths by country:")
print(country_data["Deaths"].sort_values(ascending=False).head(10))

# 13. Exporting results
country_data.to_csv("covid_country_summary.csv")
daily_data.to_csv("covid_daily_summary.csv")

print("\nAnalysis Completed Successfully!")
print("Graphs and summary CSV files have been saved.")