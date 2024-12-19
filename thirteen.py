import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# Load the original dataset
file_path = 'customer_churn.csv'  # Replace with your file path
churn_data = pd.read_csv("customer_churn.csv")

# Select relevant features and target
features = churn_data[['Age', 'Total_Purchase', 'Account_Manager', 'Years', 'Num_Sites']]
target = churn_data['Churn']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Scale the feature data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the ANN model
model = Sequential([
    Dense(16, input_shape=(X_train_scaled.shape[1],), activation='sigmoid'),
    Dense(8, activation='sigmoid'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=10, validation_data=(X_test_scaled, y_test),
                    verbose=1)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

# Prepare unseen data for prediction
# Example unseen data for prediction, ensure the columns match those in the training set
unseen_data = pd.DataFrame({
    'Age': [45],
    'Total_Purchase': [12000],
    'Account_Manager': [0],
    'Years': [6.7],
    'Num_Sites': [12]
})

# Scale the unseen data
unseen_data_scaled = scaler.transform(unseen_data)

# Predict churn on the unseen data
churn_predictions = model.predict(unseen_data_scaled)

# Convert probabilities to binary predictions (0 or 1)
churn_predictions_binary = (churn_predictions > 0.5).astype(int)

# Display predictions
print("Predicted Churn Probabilities:", churn_predictions.flatten())
print("Predicted Churn (0 = No, 1 = Yes):", churn_predictions_binary.flatten())
