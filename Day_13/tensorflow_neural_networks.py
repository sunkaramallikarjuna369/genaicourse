#!/usr/bin/env python3
"""
Day 13: TensorFlow and Neural Networks
Simple Neural Network for Image Classification
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print("=== Day 13: TensorFlow Neural Networks ===")

# Load MNIST dataset (handwritten digits)
print("\n1. Loading MNIST Dataset...")
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize data (0-1 range)
print("2. Normalizing data...")
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

print(f"   Training data shape: {x_train.shape}")
print(f"   Test data shape: {x_test.shape}")

# Build Simple Neural Network
print("\n3. Building Neural Network Model...")
model = keras.Sequential([
    # Flatten 28x28 image to 784 values
    layers.Flatten(input_shape=(28, 28)),
    # First dense layer with 128 neurons
    layers.Dense(128, activation="relu"),
    # Dropout to prevent overfitting
    layers.Dropout(0.2),
    # Second dense layer with 64 neurons
    layers.Dense(64, activation="relu"),
    # Output layer with 10 neurons (digits 0-9)
    layers.Dense(10, activation="softmax")
])

# Compile model
print("4. Compiling Model...")
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\n5. Model Summary:")
model.summary()

# Train model (commented to save time)
print("\n6. Training Model (1 epoch for demo)...")
history = model.fit(
    x_train, y_train,
    epochs=1,
    batch_size=32,
    validation_split=0.1,
    verbose=0
)

print(f"   Training Loss: {history.history['loss'][0]:.4f}")
print(f"   Training Accuracy: {history.history['accuracy'][0]:.4f}")

# Evaluate on test data
print("\n7. Evaluating on Test Data...")
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"   Test Loss: {test_loss:.4f}")
print(f"   Test Accuracy: {test_accuracy:.4f}")

# Make predictions
print("\n8. Making Predictions...")
predictions = model.predict(x_test[:5], verbose=0)
for i in range(5):
    predicted_digit = tf.argmax(predictions[i]).numpy()
    true_digit = y_test[i]
    print(f"   Sample {i+1}: Predicted={predicted_digit}, True={true_digit}")

print("\n=== Concepts Learned ===")
print("1. Loading and preprocessing data")
print("2. Building sequential neural networks")
print("3. Using activation functions (ReLU, Softmax)")
print("4. Dropout for regularization")
print("5. Compiling and training models")
print("6. Evaluating model performance")
print("7. Making predictions")
