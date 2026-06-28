import joblib
import numpy as np

# Load model
model = joblib.load("../models/model.pkl")

# Example input (modify as needed)
study_hours = 4
attendance = 85
previous_score = 78

features = np.array([[study_hours, attendance, previous_score]])

prediction = model.predict(features)

print(f"Predicted Marks: {prediction[0]:.2f}")
