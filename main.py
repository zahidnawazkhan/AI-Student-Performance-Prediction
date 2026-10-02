import tkinter as tk
from tkinter import messagebox


def predict_performance():
    try:
        math = float(math_entry.get())
        computer = float(computer_entry.get())
        physics = float(physics_entry.get())
        english = float(english_entry.get())
        study_hours = float(hours_entry.get())

        marks = [math, computer, physics, english]

        if any(mark < 0 or mark > 100 for mark in marks):
            messagebox.showerror("Error", "Marks must be between 0 and 100.")
            return

        if study_hours < 0:
            messagebox.showerror("Error", "Study hours cannot be negative.")
            return

        percentage = sum(marks) / len(marks)

        if percentage >= 80:
            performance = "Excellent"
        elif percentage >= 70:
            performance = "Very Good"
        elif percentage >= 60:
            performance = "Good"
        elif percentage >= 50:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        if study_hours >= 4:
            prediction = "High potential for improvement"
        elif study_hours >= 2:
            prediction = "Moderate potential for improvement"
        else:
            prediction = "More study time is recommended"

        result = (
            f"Average Marks: {percentage:.2f}%\n"
            f"Current Performance: {performance}\n"
            f"Study Hours: {study_hours:.1f} hours/day\n\n"
            f"Prediction: {prediction}"
        )

        result_label.config(text=result)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter numbers in all fields."
        )


window = tk.Tk()
window.title("AI Student Performance Prediction System")
window.geometry("500x550")

title = tk.Label(
    window,
    text="AI Student Performance Prediction System",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)


def create_input(label_text):
    frame = tk.Frame(window)
    frame.pack(pady=5)

    label = tk.Label(frame, text=label_text, width=18, anchor="w")
    label.pack(side="left")

    entry = tk.Entry(frame, width=20)
    entry.pack(side="left")

    return entry


math_entry = create_input("Math Marks:")
computer_entry = create_input("Computer Marks:")
physics_entry = create_input("Physics Marks:")
english_entry = create_input("English Marks:")
hours_entry = create_input("Study Hours/Day:")


predict_button = tk.Button(
    window,
    text="Predict Performance",
    command=predict_performance,
    font=("Arial", 12, "bold")
)
predict_button.pack(pady=20)


result_label = tk.Label(
    window,
    text="Enter student information above.",
    font=("Arial", 11),
    justify="left"
)
result_label.pack(pady=10)


footer = tk.Label(
    window,
    text="Student Project - Computer & Data Science",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=15)


window.mainloop()