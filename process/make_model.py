import numpy as np
import pandas as pd
import tensorflow as tf

import config as cf

# Create an array of indexes that contain the features in the dataset CSV file
feature_indexes = []
for i in range(cf.FEATURE_COUNT):
    feature_indexes.append(i)

# Import the data files

test_datafile = pd.read_csv(cf.PRE_OUTPUT_DIRECTORY + 'Testrandcarwood20.csv', usecols=feature_indexes, header=None)
test_label_col = pd.read_csv(cf.PRE_OUTPUT_DIRECTORY + 'Testrandcarwood20.csv', usecols=[cf.FEATURE_COUNT], header=None)

train_datafile = pd.read_csv(cf.PRE_OUTPUT_DIRECTORY + 'Trainrandcarwood80.csv', usecols=feature_indexes, header=None)
train_label_col = pd.read_csv(cf.PRE_OUTPUT_DIRECTORY + 'Trainrandcarwood80.csv', usecols=[cf.FEATURE_COUNT], header=None)

# Create arrays from the data and scale data down from [0,255] to [0,1] for TensorFlow

test_data = np.float32(test_datafile.values) / 255.0
test_labels = test_label_col.values

train_data = np.float32(train_datafile.values) / 255.0
train_labels = train_label_col.values


# Create label names for reference on output
class_names = ['Carpet', 'Hardwood']

# Format data for processing

print("Feature Values " + str(train_data.shape) + ":\n" + str(train_data) + "\n\nLabels " + str(train_labels.shape) + ":\n" + str(train_labels))

# Initialize variables for TensorFlow

x = tf.placeholder(tf.float32, shape=train_data.shape)
x = train_data

# Create a model for the classification
model = tf.keras.Sequential([

    # Create a 128 node layer
    tf.keras.layers.Dense(cf.NODES, activation=tf.nn.relu),

    # Create an output layer that quantifies the probabilities for each class
    tf.keras.layers.Dense(2, activation=tf.nn.softmax)
])
# Compile the model and train it for accuracy

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train and evaluate model
test_acc = 0
gen = 1

while test_acc < 0.999:
    model.fit(train_data, train_labels, epochs=1)

    test_loss, test_acc = model.evaluate(test_data, test_labels)

    print('Test Accuracy (Gen ' + str(gen) + '):', test_acc)
    gen += 1

model.summary()
model.save_weights(cf.POST_OUTPUT_DIRECTORY + 'weights')
print('Test Accuracy (Gen ' + str(gen) + '): ' + str(test_acc*100) + '%')
