Usage
=====

In order to use this project, you'll need a few things:
1. Download the *carpet.csv* and *hardwood.csv* files from the [here](https://www.uncg.edu/cmp/downloads/files/CH3.rar). 
([Source](https://github.com/Matmorcat/BigDataProcessing/blob/master/data/source.txt))
2. Put the CSV files in the `BigDataProcessing/data/input` folder (create a `data` folder if it does not exist)
3. Make sure that you have **Python 3.7** and the latest version of **Pipenv** to ensure you can load the environment
with the necessary dependencies.
4. Any customizations can be done in `BigDataProcessing/config.py`, but it should not be necessary to edit this file for 
the project to run.

Output
=====

If everything is setup correctly, this project should output the following files:

### Data Sets
- *carwood.csv*: contains the combined data of the carpet and wood CSV data
- *randcarwood.csv*: contains the data from *carwood.csv*, but shuffled
- *Testrandcarwood20.csv*: a sample of 20% of the *randcarwood.csv* for testing
- *Trainrandcarwood80.csv*: a sample of 80% of the *randcarwood.csv* for training

### Graphs
- *histograms.png*: a display of frequencies of values for both carpet and hardwood data
- *line_plots.png*: a display of mean values for both carpet and hardwood data by feature

### Statistics
- *stats-carpet.csv*: aggregate information (min, max, mean, median, and standard deviation) for the carpet data set per feature
- *stats-hardwood.csv*: aggregate information (min, max, mean, median, and standard deviation) for the hardwood data set per feature