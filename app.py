import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
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

# Features and target
X = df[["study_hours", "attendance", "previous_marks"]]
y = df["final_marks"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Website title
st.title("🎓 AI Student Performance Prediction")

st.write(
    "Enter student information to predict the expected final exam marks."
)

# User inputs
study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=85.0
)

previous_marks = st.number_input(
    "Previous Exam Marks",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

# Prediction button
if st.button("Predict Final Marks"):

    new_student = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_marks": [previous_marks]
    })

    prediction = model.predict(new_student)[0]

    prediction = max(0, min(100, prediction))

    st.success(f"Predicted Final Marks: {prediction:.2f}%")

    if prediction >= 80:
        level = "Excellent"
    elif prediction >= 70:
        level = "Very Good"
    elif prediction >= 60:
        level = "Good"
    elif prediction >= 50:
        level = "Average"
    else:
        level = "Needs Improvement"

    st.info(f"Performance Level: {level}")

# Graph
st.subheader("Study Hours vs Final Marks")

chart_data = df[["study_hours", "final_marks"]].set_index("study_hours")
st.line_chart(chart_data)