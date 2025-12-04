import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score  # Import accuracy_score

# Load the dataset
df = pd.read_csv('flood_risk_dataset_india.csv')
df.head()

# Split features and target
X = df.drop(columns=['Flood Occurred'])  # Features
y = df['Flood Occurred']  # Target variable

# Define numeric and categorical features
numeric_features = ['Latitude', 'Longitude', 'Rainfall (mm)', 'Temperature (°C)', 'Humidity (%)',
                    'River Discharge (m³/s)', 'Water Level (m)', 'Elevation (m)', 'Population Density']

categorical_features = ['Land Cover', 'Soil Type', 'Infrastructure', 'Historical Floods']

# Define transformers for preprocessing
numeric_transformer = StandardScaler()  # Scale numerical features
categorical_transformer = OneHotEncoder()  # Encode categorical features

# Create column transformer for preprocessing both types of features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Build pipeline with preprocessing and RandomForestClassifier (for classification task)
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', RandomForestClassifier(random_state=42))])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model using the training set
pipeline.fit(X_train, y_train)

# Save the trained model to a pickle file
with open('flood_batata.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

# # Check the accuracy of the model on the test set (optional)
# y_pred = pipeline.predict(X_test)
# print(f"Accuracy on Test Set: {accuracy_score(y_test, y_pred)}")
