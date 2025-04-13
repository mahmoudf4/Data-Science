# Define midpoints
distance_midpoints = {
    'Number of Trips <1': 0.5,
    'Number of Trips 1-3': 2,
    'Number of Trips 3-5': 4,
    'Number of Trips 5-10': 7.5,
    'Number of Trips 10-25': 17.5,
    'Number of Trips 25-50': 37.5,
    'Number of Trips 50-100': 75,
    'Number of Trips 100-250': 175,
    'Number of Trips 250-500': 375,
    'Number of Trips >=500': 600
}

# Calculate total trips and weighted distance
total_trips = df_trips['Population Not Staying at Home'].sum()
weighted_distance = sum(df_trips[col].sum() * midpoint for col, midpoint in distance_midpoints.items())

# Average distance per trip
average_distance = weighted_distance / total_trips
print(f"Average travel distance when not staying home: {average_distance:.2f} miles")
