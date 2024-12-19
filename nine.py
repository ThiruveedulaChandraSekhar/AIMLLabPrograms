from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report


# Load the Iris dataset
iris = datasets.load_iris()

# Features and target
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Labels (Species: 0: Setosa, 1: Versicolor, 2: Virginica)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Gaussian Naive Bayes classifier
nb_classifier = GaussianNB()

# Train the model using the training data
nb_classifier.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = nb_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print classification report
report = classification_report(y_test, y_pred, target_names=iris.target_names)

# Display results
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", report)

unseen_data = [[6.1, 3.0, 4.6, 1.4]]

prediction = nb_classifier.predict(unknown_data)

print(f"\nThe predicted species for the unknown data {unseen_data} is: {prediction} <0: Setosa, 1: Versicolor, 2: Virginica>")