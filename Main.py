"""
A very basic program that takes in two files (see config for file names) as CSV files and calculates some statistics and
outputs new CSV and PNG files for analysis and produces randomized data sets for training machine learning algorithms.
"""
from typing import Tuple
import random

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import config as cf

# Make random function deterministic for testing
if cf.DETERMINISTIC_RANDOM:
    random.seed(510)


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
        stats_data.to_csv(cf.OUTPUT_DIRECTORY + 'stats-' + name.lower() + '.csv')


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

    # Read the carpet and hardwood data in from the data folder
    carpet_data = pd.read_csv(cf.INPUT_DIRECTORY + cf.INPUT_A_FILE, header=None)
    hardwood_data = pd.read_csv(cf.INPUT_DIRECTORY + cf.INPUT_B_FILE, header=None)

    # Print out general statistics on each data set per feature
    stats(carpet_data, 'Carpet')
    stats(hardwood_data, 'Hardwood')

    ######################
    # Create a histogram #
    ######################

    plt.figure(1)

    # How many bars to show in the histogram
    bin_count = 25

    # Build the carpet data histogram
    plt.hist = carpet_data.aggregate('mean', axis='columns')\
        .hist(bins=bin_count, alpha=0.5, label='Carpet', color=cf.INPUT_A_COLOR, edgecolor='black')

    # Build the hardwood data histogram
    plt.hist = hardwood_data.aggregate('mean', axis='columns')\
        .hist(bins=bin_count, alpha=0.5, label='Hardwood', color=cf.INPUT_B_COLOR, edgecolor='black')

    # Set axes, labels, and other common plot info
    plt.legend(loc='best')
    plt.title("Combined Data")
    plt.xlabel("Mean Feature Values")
    plt.ylabel("Frequency of Observations")
    plt.minorticks_on()
    plt.grid(which='major', axis='y', linestyle=':')
    plt.grid(which='major', axis='x')

    # Output the histogram to a file
    if cf.FIGURES_SAVE_BOOL:
        plt.savefig(cf.OUTPUT_DIRECTORY + 'histograms.png')

    # Display the histogram
    if cf.FIGURES_OUTPUT_BOOL:
        plt.show()

    # Clear the figure from memory
    plt.close(1)

    ######################
    # Create a line plot #
    ######################

    plt.figure(2)

    # Build the carpet data line plot
    plt.plot = carpet_data.aggregate('mean', axis='rows')\
        .plot(label='Carpet', color=cf.INPUT_A_COLOR)

    # Build the carpet data line plot
    plt.plot = hardwood_data.aggregate('mean', axis='rows')\
        .plot(label='Hardwood', color=cf.INPUT_B_COLOR)

    # Set axes, labels, and other common plot info
    plt.legend(loc="best")
    plt.title("Combined Data")
    plt.xlabel("Feature Number")
    plt.ylabel("Mean Values")
    plt.minorticks_on()
    plt.grid(which='major', axis='y', linestyle='-.')
    plt.grid(which='major', axis='x', linestyle=':')
    plt.grid(which='minor', axis='y', linestyle=':')

    # Output the line plot to a file
    if cf.FIGURES_SAVE_BOOL:
        plt.savefig(cf.OUTPUT_DIRECTORY + 'line_plots.png')

    # Display the line plot
    if cf.FIGURES_OUTPUT_BOOL:
        plt.show()

    # Clear the figure from memory
    plt.close(2)

    ############################
    # Create a 3D scatter plot #
    ############################

    fig = plt.figure(3)

    # Should not have to exist, but choose the lowest common feature count just in case
    common_feature_count = min(carpet_data.shape[1], hardwood_data.shape[1])

    # Select 3 random features to compare in a 3D scatter plot
    feature_set = sorted(random.sample(range(common_feature_count), 3))

    carpet_x = carpet_data[feature_set[0]]
    carpet_y = carpet_data[feature_set[1]]
    carpet_z = carpet_data[feature_set[2]]
    hardwood_x = hardwood_data[feature_set[0]]
    hardwood_y = hardwood_data[feature_set[1]]
    hardwood_z = hardwood_data[feature_set[2]]

    # This does nothing but ensure that Axes3D import isn't remove. Errors will be thrown if the import is removed.
    Axes3D

    graph = fig.add_subplot(111, projection='3d')

    graph.scatter(carpet_x, carpet_y, carpet_z, color=cf.INPUT_A_COLOR, s=4, alpha=0.50, label='Carpet')
    graph.scatter(hardwood_x, hardwood_y, hardwood_z, color=cf.INPUT_B_COLOR, s=4, alpha=0.50, label='Hardwood')

    # Set axes, labels, and other common plot info
    plt.legend(loc="best")
    plt.title("Combined Data")

    graph.set_xlabel("Feature " + str(feature_set[0]))
    graph.set_ylabel("Feature " + str(feature_set[1]))
    graph.set_zlabel("Feature " + str(feature_set[2]))

    # Output the 3D scatter plot to a file
    if cf.FIGURES_SAVE_BOOL:
        plt.savefig(cf.OUTPUT_DIRECTORY + '3d_scatter_plot.png')

    # Display the 3D scatter plot
    if cf.FIGURES_OUTPUT_BOOL:
        if cf.FIGURES_OUTPUT_ROTATE:

            # Rotate the axes and update
            for angle in range(0, 360):
                graph.view_init(30, angle)
                plt.draw()
                plt.pause(.001)

        else:
            plt.show()

    # Clear the figure from memory
    plt.close(3)

    # Create a new data set with both previous data stacked together (round to 2 decimal places to fix approx. error)
    combined_data = round(combined(carpet_data, hardwood_data), 2)

    # Create a CSV file with this data
    combined_data.to_csv(cf.OUTPUT_DIRECTORY + 'carwood.csv', header=None, index=None)

    # Create a new data set with the combined data, but shuffled
    combined_shuffled_data = shuffled(combined_data)

    # Create a CSV file with this data
    combined_shuffled_data.to_csv(cf.OUTPUT_DIRECTORY + 'randcarwood.csv', header=None, index=None)

    # Get the first 80% of the shuffled file
    top80_data = combined_shuffled_data.iloc[:int(round(combined_shuffled_data.shape[0] * 0.80))]

    # Create a CSV file with this data
    top80_data.to_csv(cf.OUTPUT_DIRECTORY + 'Trainrandcarwood80.csv', header=None, index=None)

    # Get the last 20% of the shuffled file
    bottom20_data = combined_shuffled_data.iloc[int(round(combined_shuffled_data.shape[0] * 0.80)):]

    # Create a CSV file with this data
    bottom20_data.to_csv(cf.OUTPUT_DIRECTORY + 'Testrandcarwood20.csv', header=None, index=None)



