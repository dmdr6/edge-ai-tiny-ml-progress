# Window 1: Import dependencies

import tensorflow as tf   # Tensorflow is an open source machine learning library
import numpy as np
import matplotlib.pyplot as plt
import math


# Window 2: Generate random numbers and calculate their sine

samples = 1000      # Sample data points
seed = 1337         # Set seed value to get the same random numbers each time the code is ran

np.random.seed(seed)
tf.random.set_seed(seed)

# Generate a uniformly distributed set of random numbers in the range from
# 0 to 2n, which covers a complete sine wave oscillation
x_values = np.random.uniform(low=0, high=2*math.pi, size=samples)

# Shuffle the values to guarantee they're not in order
np.random.shuffle(x_values)

# Calculate the corresponding sine values
y_values = np.sin(x_values)

# Plot our data
plt.plot(x_values, y_values, 'b.')
plt.show()


# Window 3: Add some random noise to our datapoints and draw another graph

# Add a small random number to each y value
y_values += 0.15 * np.random.rand(*y_values.shape)

# Plot our data
plt.plot(x_values, y_values, 'b.')
plt.show()


# Window 4: The following code splits our data and then plots each set 
# as a different color

# Use 60% of our data for training and 20% for testing. The remaining 20% will be
# used for validation. Calculate the indices of each section.
train_split = int(0.6 * samples)
test_split = int(0.2 * samples + train_split)

# Use np.split to chop our data into three parts
# The second argument to np.split is an array of indices where the data will be
# split. Provide two indices, so the data will be divided into three chunks.
x_train, x_validate, x_test = np.split(x_values, [train_split, test_split])
y_train, y_validate, y_test = np.split(y_values, [train_split, test_split])

# Double check that our splits add up correctly
assert (x_train.size + x_validate.size + x_test.size) == samples

# Plot the data in each partition in different colors:
plt.plot(x_train, y_train, 'b.', label="Train")
plt.plot(x_validate, y_validate, 'y.', label="Validate")
plt.plot(x_test, y_test, 'r.', label="Test")
plt.legend()
plt.show()
