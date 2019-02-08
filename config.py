"""
Processing Config
"""


###############################
#                             #
# Preparation Script Settings #
#                             #
###############################

# The path in the project directory to read in the CSV files
PRE_INPUT_DIRECTORY = '../prep/data/input/'

# The path in the project directory to output all data about CSV files
PRE_OUTPUT_DIRECTORY = '../prep/data/output/'

# The file names for both CSV files to be read in (include .csv extension)
INPUT_A_FILE = 'carpet.csv'
INPUT_B_FILE = 'hardwood.csv'

# The number of features (columns in the data)
FEATURE_COUNT = 64

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
GRAPHS_OUTPUT_BOOL = False

# Save graphs as PNG files
GRAPHS_SAVE_BOOL = True


#############################
#                           #
# Modelling Script Settings #
#                           #
#############################

# Nodes (neurons) that the compiler can use
NODES = 128

# The goal score for correct classifications in the testing phase (0.000 = 0%, 1.000 = 100%)
MINIMUM_TEST_SCORE = 0.999

# The path in the project directory to output the models
POST_OUTPUT_DIRECTORY = '../process/data/output/'
