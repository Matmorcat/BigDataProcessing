# Preparation Script

This script allows for inputting two class separated CSV files with raw values as a dataset into usable data for big
data processing. This data is provided by the source [**textbook**][book] as a downloadable archive.


## Usage

In order to use this script, you'll need a few things:
1. Extract the *carpet.csv* and *hardwood.csv* files from the publicly available [**archive**][rar]

2. Put the CSV files in the [`BigDataProcessing/prep/data/input`][prep_in] folder

3. Make sure that you have [**Python 3.6**][py] (TensorFlow 1.12.0 does not support Python 3.7) and
the latest version of [**Pipenv**][pip] to ensure you can load the environment
with the necessary dependencies.

4. Any customizations can be done in [`BigDataProcessing/config.py`][cf], but it should not be necessary to edit this file for 
the project to run.


## Output

If everything is setup correctly, this script should output the following files in `BigDataProcessing/prep/data/output`:

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




# Modelling Script

This script allows for processing of a set of testing and training data to create a model for classifying between a
hardwood floor and a carpet floor image.


## Usage

Before running:
1. *Testrandcarwood20.csv* and *Trainrandcarwood80.csv* exist in `BigDataProcessing/prep/data/output`

2. Customize the modelling process in [`BigDataProcessing/config.py`][cf].


## Output

If everything is setup correctly, the following files will be created in `BigDataProcessing/process/data/output`:

 File                           | Description 
 ------------------------------ | -----------------------------------------------------------
*checkpoint*                    | A save of the last state of the process in TensorFlow
*weights.data-\[num]-of-\[num]* | Each fragment of the model weights (can be separated)
*weights.index*                 | The index for all the model weights




[book]: prep/data/input/source.txt "Textbook Source"

[rar]: https://www.uncg.edu/cmp/downloads/files/CH3.rar "Chapter 3 File Archive"
[py]: https://www.python.org/downloads/ "Python Downloads"
[pip]: https://pypi.org/project/pipenv/ "Pipenv Development Page"

[cf]: config.py "Pipenv Development Page"
[prep_in]: prep/data/input "Preparation Input Folder"

[prep_py]: prep/prepare.py "Preparation Script"
[proc_py]: process/make_model.py "Modelling Script"