import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# Load dataset
df = pd.read_csv("../data/sample_data.csv")

X = df[["study_hours", "attendance", "previous_score"]]
y = df["marks"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model trained successfully!")
print(f"MAE: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# Save model
os.makedirs("../models", exist_ok=True)
joblib.dump(model, "../models/model.pkl")

print("Model saved to models/model.pkl")
