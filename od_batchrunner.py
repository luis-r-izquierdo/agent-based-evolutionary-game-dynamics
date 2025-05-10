
from mesa.batchrunner import batch_run
import time
from od_tutorial import ODModel
import numpy as np
import pandas as pd


# Start the timer
start_time = time.time()
params = {"mu": 0.5, "N": 1000,
           "tolerance": [0.05]}#, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]}

if __name__ == '__main__':
    results = batch_run(
        ODModel,
        parameters=params,
        iterations=1,
        max_steps=1,
        number_processes=1,
        display_progress=False,
    )

    # End the timer
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    print(f"Time taken to run the batch: {elapsed_time:.2f} seconds")

    results_df = pd.DataFrame(results)
    print(f"The results have {len(results)} rows.")
    print(f"The columns of the data frame are {list(results_df.keys())}.")
    # %%
    distinct_values_per_simulation = results_df.groupby(["RunId", "tolerance"])["opinion"].nunique()

    # Merge the distinct values back with the original DataFrame to associate 'tolerance' with each 'RunId'
    distinct_values_with_tolerance = results_df[["RunId", "tolerance"]].drop_duplicates()
    distinct_values_with_tolerance["distinct_opinions"] = distinct_values_per_simulation.values

    # Group by 'tolerance' and calculate the mean number of distinct opinions
    mean_distinct_per_tolerance = distinct_values_with_tolerance.groupby("tolerance")["distinct_opinions"].mean()

    # Print the result
    print(mean_distinct_per_tolerance)

    # Plot the mean number of distinct opinions against tolerance
    # %%

    # Assuming `results_df` is your DataFrame
    distinct_values_per_simulation = results_df.groupby(["RunId", "tolerance"])["opinion"].nunique()

    # Print the result
    print(distinct_values_per_simulation)


    # %%
    # Remove "wings" (extreme opinion values)
    filtered_results = results_df[
        ~(
            ((results_df["opinion"] >= 1 - results_df["tolerance"]) & (results_df["opinion"] <= 1)) |
            ((results_df["opinion"] >= 0) & (results_df["opinion"] <= results_df["tolerance"]))
        )
    ]

    # Recalculate the number of distinct opinions after removing wings
    distinct_values_per_simulation_filtered = filtered_results.groupby(["RunId", "tolerance"])["opinion"].nunique()

    # Reset the index to make it easier to work with
    distinct_values_per_simulation_filtered = distinct_values_per_simulation_filtered.reset_index()

    # Initialize a dictionary to store the counts for each number of distinct values
    distinct_value_counts = {}

    # Iterate over the range of distinct values (1 to 7)
    for num_distinct in range(1, 8):
        # Filter simulations with the current number of distinct opinions
        simulations_with_num_distinct = distinct_values_per_simulation_filtered[
            distinct_values_per_simulation_filtered["opinion"] == num_distinct
        ]
        
        # Count the number of such simulations for each tolerance value
        counts_by_tolerance = simulations_with_num_distinct.groupby("tolerance").size()
        
        # Store the result in the dictionary
        distinct_value_counts[num_distinct] = counts_by_tolerance

    # Print the results
    for num_distinct, counts in distinct_value_counts.items():
        print(f"Number of simulations with exactly {num_distinct} distinct opinions (by tolerance):")
        print(counts)
        print()
    # %%
