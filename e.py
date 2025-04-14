import matplotlib.pyplot as plt
import pandas as pd

df_trips = pd.read_csv("Trips_by_Distance.csv")

# Frequency bins
frequency_bins = [
    'Number of Trips <1',
    'Number of Trips 1-3',
    'Number of Trips 3-5',
    'Number of Trips 5-10',
    'Number of Trips 10-25',
    'Number of Trips 25-50',
    'Number of Trips 50-100',
    'Number of Trips 100-250',
    'Number of Trips 250-500',
    'Number of Trips >=500'
]

# Compute the average number of people per frequency category
avg_by_bin = df_trips[frequency_bins].mean()

# Plot a histogram-style bar chart
plt.figure(figsize=(12, 6))
avg_by_bin.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Average Number of People by Trip Frequency Category")
plt.xlabel("Trip Frequency Range (Number of Trips)")
plt.ylabel("Average Number of People")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
