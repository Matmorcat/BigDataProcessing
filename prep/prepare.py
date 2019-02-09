"""
A very basic program that takes in two files (see config for file names) as CSV files and calculates some statistics and
outputs new CSV and PNG files for analysis and produces randomized data sets for training machine learning algorithms.
"""
from pathlib import Path
from typing import Tuple

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import config as cf


def stats(data: pd.DataFrame, name='Unknown', printout=cf.STATS_OUTPUT_BOOL, save=cf.STATS_SAVE_BOOL):

    dimensions: Tuple[int, int] = data.shape
    row_count: int = dimensions[0]
    col_count: int = dimensions[1]

    stats_data = round(data.aggregate(cf.AGGREGATED_DATA_FUNCS), 2)
    stats_data = stats_data.add_prefix("Feature ")

    if printout:
        print(name + " Statistics:\n")
        print(stats_data)
        print("Observations (rows): " + str(row_count))
        print("Dimensions / Features (columns): " + str(col_count))
        print("\n\n")
    if save:
        stats_data.to_csv(cf.PRE_OUTPUT_DIRECTORY + 'stats-' + name.lower() + '.csv')


def ravelled(tabular_data: pd.DataFrame) -> np.ndarray:

    return tabular_data.values.ravel()


def combined(carpet_data: pd.DataFrame, hardwood_data: pd.DataFrame) -> pd.DataFrame:

    # Create a new data set with the data from both
    union_data = carpet_data.assign(type=0)                  # Assign a new column "type" with value 0 (carpet ID)
    union_data = union_data.append(hardwood_data.assign(type=1))  # Assign a new column with value 1 (hardwood ID)

    # Return the combined data set (not shuffled, carpet data followed by hardwood data)
    return union_data


def shuffled(data: pd.DataFrame) -> pd.DataFrame:

    # Randomize the entries (rows) of the data set (returns a random sample with all rows shuffled)
    return data.sample(frac=1).reset_index(drop=True)


class Main:

    file_a_path = cf.PRE_INPUT_DIRECTORY + cf.INPUT_A_FILE
    file_b_path = cf.PRE_INPUT_DIRECTORY + cf.INPUT_B_FILE

    # Make sure that the needed files exist
    if not Path(file_a_path).is_file():
        print("File not found in path: " + file_a_path)
        exit()
    if not Path(file_b_path).is_file():
        print("File not found in path: " + file_b_path)
        exit()

    print("Reading in the data...")
    # Read the carpet and hardwood data in from the data folder
    carpet_data = pd.read_csv(file_a_path, header=None)
    hardwood_data = pd.read_csv(file_b_path, header=None)

    # Make the directory if it does not exist
    os.makedirs(cf.PRE_OUTPUT_DIRECTORY, exist_ok=True)

    print("Calculating statistical information...")
    # Print out general statistics on each data set per feature
    stats(carpet_data, 'Carpet')
    stats(hardwood_data, 'Hardwood')

    print("Creating graphs...")

    # Build the carpet data histogram
    plt.hist = carpet_data.aggregate('mean', axis='columns')\
        .hist(bins=cf.BIN_COUNT, alpha=0.5, label='Carpet', color=cf.INPUT_A_COLOR, edgecolor='black')

    # Build the hardwood data histogram
    plt.hist = hardwood_data.aggregate('mean', axis='columns')\
        .hist(bins=cf.BIN_COUNT, alpha=0.5, label='Hardwood', color=cf.INPUT_B_COLOR, edgecolor='black')

    # Set axes, labels, and other common plot info
    plt.legend(loc='best')
    plt.title("Combined Data")
    plt.xlabel("Feature Values")
    plt.ylabel("Frequency")
    plt.minorticks_on()
    plt.grid(which='major', axis='y', linestyle=':')
    plt.grid(which='major', axis='x')

    # Output the histogram to a file
    if cf.GRAPHS_SAVE_BOOL:
        print("Saving histogram...")
        plt.savefig(cf.PRE_OUTPUT_DIRECTORY + 'histograms.png')

    # Display the histogram
    if cf.GRAPHS_OUTPUT_BOOL:
        print("Displaying histogram...")
        plt.show()

    # Clear the figure to make a new figure
    plt.clf()

    # Build the carpet data line plot
    plt.plot = carpet_data.aggregate('mean', axis='rows')\
        .plot(label='Carpet', color=cf.INPUT_A_COLOR)

    # Build the hardwood data line plot
    plt.plot = hardwood_data.aggregate('mean', axis='rows')\
        .plot(label='Hardwood', color=cf.INPUT_B_COLOR)

    # Set axes, labels, and other common plot info
    plt.legend(loc="best")
    plt.title("Combined Data")
    plt.xlabel("Feature Number")
    plt.ylabel("Mean")
    plt.minorticks_on()
    plt.grid(which='major', axis='y', linestyle='-.')
    plt.grid(which='major', axis='x', linestyle=':')
    plt.grid(which='minor', axis='y', linestyle=':')

    # Output the line plot to a file
    if cf.GRAPHS_SAVE_BOOL:
        print("Saving line plot...")
        plt.savefig(cf.PRE_OUTPUT_DIRECTORY + 'line_plots.png')

    # Display the line plot
    if cf.GRAPHS_OUTPUT_BOOL:
        print("Displaying line plot...")
        plt.show()

    print("Generating labelled datasets...")

    # Create a new data set with both previous data stacked together (round to 2 decimal places to fix approx. error)
    combined_data = round(combined(carpet_data, hardwood_data), 2)

    # Create a new data set with the combined data, but shuffled
    combined_shuffled_data = shuffled(combined_data)

    # Get the first 80% of the shuffled file
    top80_data = combined_shuffled_data.iloc[:int(round(combined_shuffled_data.shape[0] * 0.80))]

    # Get the last 20% of the shuffled file
    bottom20_data = combined_shuffled_data.iloc[int(round(combined_shuffled_data.shape[0] * 0.80)):]

    print("Saving all generated datasets...")

    # Create a CSV file with this data
    combined_data.to_csv(cf.PRE_OUTPUT_DIRECTORY + 'carwood.csv', header=None, index=None)

    # Create a CSV file with this data
    combined_shuffled_data.to_csv(cf.PRE_OUTPUT_DIRECTORY + 'randcarwood.csv', header=None, index=None)

    # Create a CSV file with this data
    top80_data.to_csv(cf.PRE_OUTPUT_DIRECTORY + 'Trainrandcarwood80.csv', header=None, index=None)

    # Create a CSV file with this data
    bottom20_data.to_csv(cf.PRE_OUTPUT_DIRECTORY + 'Testrandcarwood20.csv', header=None, index=None)

    print("\nDatasets successfully created!")

