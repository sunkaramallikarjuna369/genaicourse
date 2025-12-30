#!/usr/bin/env python3
"""
Day 14: PyTorch Deep Learning
Simple PyTorch Neural Network Example
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

print("=== Day 14: PyTorch Deep Learning ===")

# 1. Create sample data
print("\n1. Creating Sample Data...")
X_train = torch.randn(100, 10)  # 100 samples, 10 features
y_train = torch.randint(0, 2, (100,))  # Binary classification

print(f"   Training features shape: {X_train.shape}")
print(f"   Training labels shape: {y_train.shape}")

# 2. Create DataLoader
print("\n2. Creating DataLoader...")
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
print(f"   Batch size: 32")
print(f"   Number of batches: {len(train_loader)}")

# 3. Define Neural Network
print("\n3. Defining Neural Network...")
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 64)  # Input 10 -> Hidden 64
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)  # Hidden 64 -> Hidden 32
        self.fc3 = nn.Linear(32, 2)   # Hidden 32 -> Output 2
        self.dropout = nn.Dropout(0.2)
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x

model = SimpleNet()
print(f"   Model created: {model}")

# 4. Define loss and optimizer
print("\n4. Setting up Loss and Optimizer...")
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
print(f"   Loss function: CrossEntropyLoss")
print(f"   Optimizer: Adam (lr=0.001)")

# 5. Training loop
print("\n5. Training Model (1 epoch)...")
epochs = 1
for epoch in range(epochs):
    total_loss = 0
    for batch_X, batch_y in train_loader:
        # Forward pass
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    avg_loss = total_loss / len(train_loader)
    print(f"   Epoch {epoch+1}, Loss: {avg_loss:.4f}")

# 6. Make predictions
print("\n6. Making Predictions...")
model.eval()  # Set to evaluation mode
with torch.no_grad():
    test_input = torch.randn(5, 10)
    predictions = model(test_input)
    predicted_classes = torch.argmax(predictions, dim=1)
    print(f"   Input shape: {test_input.shape}")
    print(f"   Predictions shape: {predictions.shape}")
    print(f"   Predicted classes: {predicted_classes.numpy()}")

print("\n=== Concepts Learned ===")
print("1. PyTorch tensors and operations")
print("2. Building custom neural networks with nn.Module")
print("3. DataLoader for batch processing")
print("4. Forward and backward propagation")
print("5. Optimization with Adam")
print("6. Training and evaluation modes")
