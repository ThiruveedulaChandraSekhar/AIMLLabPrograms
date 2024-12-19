import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv('movies.csv')

# Display the first few rows of the dataset
print(df.head())

# Step 1: Check for missing values in the dataset
print("Missing values before imputation:")
print(df.isnull().sum())

# Step 2: Check the data type of each attribute
print("\nData types of each attribute:")
print(df.dtypes)

# Step 3: Impute missing values
# Impute numerical columns with mean
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

# Verify if missing values are imputed in numerical columns
print("Missing values in numerical columns after imputation:")
print(df[numerical_cols].isnull().sum())

# Impute categorical columns with most frequent value (mode)
categorical_cols = df.select_dtypes(include=['object']).columns
mode_imputer = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = mode_imputer.fit_transform(df[categorical_cols])

# Verify if missing values are imputed in categorical columns
print("Missing values in categorical columns after imputation:")
print(df[categorical_cols].isnull().sum())

# Save the cleaned dataset as a CSV file
output_file_csv = 'Cleaned_Dataset.csv'
df.to_csv(output_file_csv, index=False)

print(f"Cleaned dataset saved as {output_file_csv}")