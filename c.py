import dask
dask.config.set({"dataframe.convert-string": False})

import pandas as pd
import dask.dataframe as dd
import matplotlib.pyplot as plt
import time

# Simulated processor counts
core_counts = [10, 20]
timing_results = {}

# Load data with pandas
data = pd.read_csv("Trips_by_Distance.csv")

# Convert trip columns to numeric
data["Number of Trips 10-25"] = pd.to_numeric(data["Number of Trips 10-25"], errors="coerce")
data["Number of Trips 50-100"] = pd.to_numeric(data["Number of Trips 50-100"], errors="coerce")

# Convert to Dask DataFrame
dask_data = dd.from_pandas(data, npartitions=4)

# Simulate execution with different core counts
for cores in core_counts:
    print(f"\nSimulating with {cores} cores...")
    start = time.time()

    # Filter rows where trip counts exceed 10 million
    result_10_25 = dask_data[dask_data["Number of Trips 10-25"] > 1e7][["Date", "Number of Trips 10-25"]].compute()
    result_50_100 = dask_data[dask_data["Number of Trips 50-100"] > 1e7][["Date", "Number of Trips 50-100"]].compute()

    # Record processing time
    duration = time.time() - start
    timing_results[cores] = duration

    # Show result summary
    print(f"{len(result_10_25)} rows >10M (10–25)")
    print(f"{len(result_50_100)} rows >10M (50–100)")
    print(f"Time taken: {duration:.2f} seconds")

# Display time summary
print("\nExecution Time Summary:")
for c, t in timing_results.items():
    print(f"{c} cores: {t:.2f} seconds")
