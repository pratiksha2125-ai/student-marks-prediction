import csv

def predict_marks(study_hours, attendance):
    # Simple AI logic
    marks = (study_hours * 7) + (attendance * 0.4)
    return min(100, round(marks, 2))

print("=== Student Marks Prediction System ===")

study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))

predicted_marks = predict_marks(study_hours, attendance)

print(f"Predicted Marks: {predicted_marks}")

if predicted_marks >= 75:
    print("Performance: Excellent")
elif predicted_marks >= 60:
    print("Performance: Good")
elif predicted_marks >= 40:
    print("Performance: Average")
else:
    print("Performance: Poor")
