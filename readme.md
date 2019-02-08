# Preparation Script

This script allows for processing two class separated CSV files with raw values as a dataset into usable data for big
data processing.

## Usage

In order to use this project, you'll need a few things:
1. Download the *carpet.csv* and *hardwood.csv* files from the [here](https://www.uncg.edu/cmp/downloads/files/CH3.rar). 
([Source](https://github.com/Matmorcat/BigDataProcessing/blob/master/prep/data/input/source.txt))
2. Put the CSV files in the `BigDataProcessing/prep/data/input` folder (create an `input` folder if it does not exist)
3. Make sure that you have **Python 3.6** (3.7 will not work with TensorFlow) and the latest version of **Pipenv** to ensure you can load the environment
with the necessary dependencies.
4. Any customizations can be done in `BigDataProcessing/config.py`, but it should not be necessary to edit this file for 
the project to run.

## Output

If everything is setup correctly, this project should output the following files in `BigDataProcessing/prep/data/output`:

### Data Sets
 File                    | Description 
 ----------------------- | -----------------------------------------------------------
*carwood.csv*            | Contains the combined data of the carpet and wood CSV data
*randcarwood.csv*        | Contains the data from *carwood.csv*, but shuffled
*Testrandcarwood20.csv*  | A sample of 20% of the *randcarwood.csv* for testing
*Trainrandcarwood80.csv* | A sample of 80% of the *randcarwood.csv* for training

### Graphs
 File                    | Description 
 ----------------------- | -----------------------------------------------------------
*histograms.png*         | A display of frequencies of values for both carpet and hardwood data
*line_plots.png*         | A display of mean values for both carpet and hardwood data by feature

### Statistics
 File                    | Description 
 ----------------------- | -----------------------------------------------------------
*stats-carpet.csv*       | Aggregate info (min, max, mean, median, and standard deviation) for carpet data
*stats-hardwood.csv*     | Aggregate info (min, max, mean, median, and standard deviation) for hardwood data
