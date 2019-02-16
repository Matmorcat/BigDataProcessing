"""
This is the general config for the program.
"""

# Make sure that all randomized values are deterministic (same across multiple runs)
DETERMINISTIC_RANDOM = True

# The path in the project directory to read in the CSV files
INPUT_DIRECTORY = 'data/input/'

# The path in the project directory to output all files created
OUTPUT_DIRECTORY = 'data/output/'

# The file names for both CSV files to be read in (include .csv extension)
INPUT_A_FILE = 'carpet.csv'
INPUT_B_FILE = 'hardwood.csv'

# The colors to make each data set in the graphs that are created
INPUT_A_COLOR = 'red'
INPUT_B_COLOR = 'blue'

# The data that will be outputted to the statistics file about each data set
AGGREGATED_DATA_FUNCS = ['min', 'max', 'mean', 'median', 'std']

# Print out statistics in the console
STATS_OUTPUT_BOOL = False

# Save statistics into a CSV file
STATS_SAVE_BOOL = True

# Display graphs as pop-ups in order
FIGURES_OUTPUT_BOOL = True

# Save graphs as PNG files
FIGURES_SAVE_BOOL = True

# Output a rotating graph instead of a static graph (output boolean must be true)
FIGURES_OUTPUT_ROTATE = False
