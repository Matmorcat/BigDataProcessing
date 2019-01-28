from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def stats(data: pd.DataFrame, name='Unknown', printout=False, save=True):

    dimensions: Tuple[int, int] = data.shape
    row_count: int = dimensions[0]
    col_count: int = dimensions[1]

    stats = round(data.aggregate(['min', 'max', 'mean', 'median', 'std']), 2)
    stats = stats.add_prefix("Feature ")

    if printout:
        print(name + " Statistics:\n")
        print(stats)
        print("Observations (rows): " + str(row_count))
        print("Dimensions / Features (columns): " + str(col_count))
        print("\n\n")
    if save:
        stats.to_csv('data/stats-' + name.lower() + '.csv')


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
    carpet_data = pd.read_csv('data/carpet.csv', header=None)
    hardwood_data = pd.read_csv('data/hardwood.csv', header=None)

    # Print out general statistics on each data set per feature
    stats(carpet_data, 'Carpet', printout=True, save=True)
    stats(hardwood_data, 'Hardwood', printout=True, save=True)
    # How many bars to show in the histogram
    bin_count = 25

    # Build the carpet data histogram
    plt.hist = carpet_data.aggregate('mean', axis='columns')\
        .hist(bins=bin_count, alpha=0.5, label='Carpet', color='red', edgecolor='black')

    # Build the hardwood data histogram
    plt.hist = hardwood_data.aggregate('mean', axis='columns')\
        .hist(bins=bin_count, alpha=0.5, label='Hardwood', color='blue', edgecolor='black')

    # Set axes, labels, and other common plot info
    plt.legend(loc='best')
    plt.title("Combined Data")
    plt.xlabel("Feature Values")
    plt.ylabel("Frequency")
    plt.minorticks_on()
    plt.grid(which='major', axis='y', linestyle=':')
    plt.grid(which='major', axis='x')

    # Output the histogram to a file
    plt.savefig('data/histograms.png')

    # Display the histogram
    plt.show()

    # Build the carpet data line plot
    plt.plot = carpet_data.aggregate('mean', axis='rows')\
        .plot(label='Carpet', color='red')

    # Build the carpet data line plot
    plt.plot = hardwood_data.aggregate('mean', axis='rows')\
        .plot(label='Hardwood', color='blue')

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
    plt.savefig('data/line_plots.png')

    # Display the line plot
    plt.show()

    # Create a new data set with both previous data stacked together (round to 2 decimal places to fix approx. error)
    combined_data = round(combined(carpet_data, hardwood_data), 2)

    # Create a CSV file with this data
    combined_data.to_csv('data/carwood.csv', header=None, index=None)

    # Create a new data set with the combined data, but shuffled
    combined_shuffled_data = shuffled(combined_data)

    # Create a CSV file with this data
    combined_shuffled_data.to_csv('data/randcarwood.csv', header=None, index=None)

    # Get the first 80% of the shuffled file
    top80_data = combined_shuffled_data.iloc[:int(round(combined_shuffled_data.shape[0] * 0.80))]

    # Create a CSV file with this data
    top80_data.to_csv('data/Trainrandcarwood80.csv', header=None, index=None)

    # Get the last 20% of the shuffled file
    bottom20_data = combined_shuffled_data.iloc[int(round(combined_shuffled_data.shape[0] * 0.80)):]

    # Create a CSV file with this data
    bottom20_data.to_csv('data/Testrandcarwood20.csv', header=None, index=None)

