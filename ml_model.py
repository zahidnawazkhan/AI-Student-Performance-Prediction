import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Sample student dataset
data = {
    "study_hours": [1, 2, 2.5, 3, 3.5, 4, 4.5, 5,
                    5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9],

    "attendance": [60, 65, 68, 70, 72, 75, 78, 80,
                   82, 84, 86, 88, 90, 92, 94, 96],

    "previous_marks": [45, 50, 52, 55, 58, 60, 63, 66,
                       68, 70, 73, 76, 80, 83, 86, 90],

    "final_marks": [48, 53, 55, 58, 61, 64, 67, 70,
                    72, 75, 78, 81, 84, 87, 90, 93]
}

df = pd.DataFrame(data)

# Features
X = df[["study_hours", "attendance", "previous_marks"]]

# Target
y = df["final_marks"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create machine learning model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("AI Student Performance Prediction System")
print("----------------------------------------")
print(f"Model Mean Absolute Error: {mae:.2f} marks")

# User input
print("\nEnter student information:")

study_hours = float(input("Study hours per day: "))
attendance = float(input("Attendance percentage: "))
previous_marks = float(input("Previous exam marks: "))

new_student = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_marks": [previous_marks]
})

# Prediction
prediction = model.predict(new_student)[0]

prediction = max(0, min(100, prediction))

print(f"\nPredicted Final Marks: {prediction:.2f}%")

if prediction >= 80:
    print("Performance Level: Excellent")
elif prediction >= 70:
    print("Performance Level: Very Good")
elif prediction >= 60:
    print("Performance Level: Good")
elif prediction >= 50:
    print("Performance Level: Average")
else:
    print("Performance Level: Needs Improvement")

# Create graph
plt.scatter(df["study_hours"], df["final_marks"])

plt.xlabel("Study Hours per Day")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")

plt.grid(True)

plt.savefig("study_hours_vs_marks.png", dpi=150)

plt.show()