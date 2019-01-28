"""
This is the general config for the program.
"""

# Path Variables
INPUT_DIRECTORY = 'data/input/'
OUTPUT_DIRECTORY = 'data/output/'

# Input File Names
INPUT_A_FILE = 'carpet.csv'
INPUT_B_FILE = 'hardwood.csv'

# Input File Colors
INPUT_A_COLOR = 'red'
INPUT_B_COLOR = 'blue'

# The data that will be outputted to the statistics file about each data set
AGGREGATED_DATA_FUNCS = ['min', 'max', 'mean', 'median', 'std']

# Print out statistics in the console
STATS_OUTPUT_BOOL = True

# Save statistics into a CSV file
STATS_SAVE_BOOL = True

# Display graphs as pop-ups in order
GRAPHS_OUTPUT_BOOL = True

# Save graphs as PNG files
GRAPHS_SAVE_BOOL = True
