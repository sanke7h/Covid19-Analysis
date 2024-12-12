# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting style for plots
sns.set()

df = pd.read_csv('covid_19_clean_complete.csv')

# Data Overview
print("First 5 rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())

df = df.drop(columns=['Lat', 'Long','Province/State'])  # Drop latitude and longitude

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Global Analysis
print("\nGlobal Summary:")
total_confirmed = df['Confirmed'].sum()
total_deaths = df['Deaths'].sum()
total_recovered = df['Recovered'].sum()

print(f"Total Confirmed: {total_confirmed}")
print(f"Total Deaths: {total_deaths}")
print(f"Total Recovered: {total_recovered}")

# Global Death and Recovery Rates
death_rate = (total_deaths / total_confirmed) * 100
recovery_rate = (total_recovered / total_confirmed) * 100
print(f"Death Rate: {death_rate:.2f}%")
print(f"Recovery Rate: {recovery_rate:.2f}%")

# Top 10 Countries by Confirmed Cases
grouped_countries = df.groupby('Country/Region').max()
top_countries = grouped_countries['Confirmed'].sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_countries.index, top_countries.values, color='orange')
plt.xlabel('Countries')
plt.ylabel('Confirmed Cases')
plt.title('Top 10 Countries by Confirmed COVID-19 Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./images/top_countries.png')
plt.show()

# India-Specific Analysis
india_data = df[df['Country/Region'] == 'India']
plt.figure(figsize=(12, 6))
plt.plot(india_data['Date'], india_data['Confirmed'], label='Confirmed Cases', color='blue')
plt.plot(india_data['Date'], india_data['Deaths'], label='Deaths', color='red')
plt.plot(india_data['Date'], india_data['Recovered'], label='Recovered', color='green')
plt.plot(india_data['Date'], india_data['Active'], label='Active Cases', color='black')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('COVID-19 Trends in India')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./images/india_trends.png')
plt.show()

# WHO Region Analysis
who_region_data = df.groupby('WHO Region').max()['Confirmed']
plt.figure(figsize=(10, 6))
plt.bar(who_region_data.index, who_region_data.values, color='purple')
plt.xlabel('WHO Region')
plt.ylabel('Confirmed Cases')
plt.title('Confirmed Cases by WHO Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./images/who_regions.png')
plt.show()

# Heatmap for WHO Regions
pivot_data = df.pivot_table(values='Confirmed', index='WHO Region', columns='Date', aggfunc='max')
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_data.fillna(0), cmap='YlOrRd', cbar_kws={'label': 'Confirmed Cases'})
plt.title('Heatmap of Confirmed Cases Over Time (WHO Regions)')
plt.tight_layout()
plt.savefig('./images/heatmap_cases.png')
plt.show()

### CORRELATION BETWEEN CONFIRMED AND DEATHS ###
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Confirmed'], y=df['Deaths'], alpha=0.7)
plt.title('Correlation Between Confirmed Cases and Deaths')
plt.xlabel('Confirmed Cases')
plt.ylabel('Deaths')
plt.tight_layout()
plt.savefig('./images/confirmed_deaths_correlation.png')
plt.show()

"""
    Compare COVID-19 trends between two countries.
"""
country1_data = df[df['Country/Region'] == 'India']
country2_data = df[df['Country/Region'] == 'US']

plt.figure(figsize=(12, 6))
plt.plot(country1_data['Date'], country1_data['Confirmed'], label=f'India Confirmed', color='blue')
plt.plot(country2_data['Date'], country2_data['Confirmed'], label=f'US Confirmed', color='orange')

plt.plot(country1_data['Date'], country1_data['Deaths'], label=f'India Deaths', linestyle='--', color='red')
plt.plot(country2_data['Date'], country2_data['Deaths'], label=f'US Deaths', linestyle='--', color='purple')

plt.xlabel('Date')
plt.ylabel('Count')
plt.title(f'COVID-19 Comparison: India vs US')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'./images/India vs US comparison.png')
plt.show()

print("Analysis Completed! Check the 'images' folder for visualizations.")