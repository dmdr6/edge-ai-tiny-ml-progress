# Window 1: Import dependencies
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math


# Window 2: Generate random numbers and calculate their sine

# Sample data points
samples = 1000

# Set seed value to get the same random numbers each time the code is ran
seed = 1337

np.random.seed(seed)
tf.random.set_seed(seed)

# Generate a uniformly distributed set of random numbers in the range from
# 0 to 2n, which covers a complete sine wave oscillation
x_values = np.random.uniform(low=0, high=2*math.pi, size=samples)

# Shuffle the values to guarantee they're not in order
np.random.shuffle(x_values)

# Calculate the corresponding sine values
y_values = np.sin(x_values)

# Plot the data
plt.plot(x_values, y_values, 'b.')
plt.show()


# Window 3: Add some random noise to the datapoints and draw another graph

# Add a small random number to each y value
y_values += 0.15 * np.random.rand(*y_values.shape)

# Plot the data
plt.plot(x_values, y_values, 'b.')
plt.show()


# Window 4: Split data and plot each set as a different color

# Use 60% of data for training and 20% for testing. The remaining 20% will be
# used for validation. Calculate the indices of each section
train_split = int(0.6 * samples)
test_split = int(0.2 * samples + train_split)

# Use np.split to chop our data into three parts
# The second argument to np.split is an array of indices where the data will be
# split. We provide two indices, so the data will be divided into three chunks.
x_train, x_validate, x_test = np.split(x_values, [train_split, test_split])
y_train, y_validate, y_test = np.split(y_values, [train_split, test_split])

# Double check that our splits add up correctly
assert (x_train.size + x_validate.size + x_test.size) == samples

# Plot the data in each partition in different colors
plt.plot(x_train, y_train, 'b.', label="Train")
plt.plot(x_validate, y_validate, 'y.', label="Validate")
plt.plot(x_test, y_test, 'r.', label="Test")
plt.legend()
plt.show()


# Window 5: Design a simple neural network

# Use Keras to create a simple model architecture
from keras import layers
model_1 = tf.keras.Sequential()

# First layer takes a scalar input and feeds it through 16 "neurons." The
# neurons decide whether to activate based on the 'relu' activation function.
model_1.add(layers.Dense(16, activation='relu', input_shape=(1,)))

# Final layer is a single neuron since the output has to be a single value
model_1.add(layers.Dense(1))

# Compile the model using a standard optimizer and loss function for regression
model_1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

# Print a summary of the model's architecture
model_1.summary()
