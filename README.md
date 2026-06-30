# 🎓 Student Marks Prediction System

## 📌 Project Overview

The **Student Marks Prediction System** is a simple Python-based application that predicts a student's expected marks based on two factors:

* Daily study hours
* Attendance percentage

The project uses a basic mathematical formula to estimate marks and classifies the student's performance into different categories. It is designed for beginners to understand Python functions, conditional statements, user input, and simple prediction logic.

---

# 🎯 Features

* Predicts student marks based on study hours and attendance
* Accepts user input from the keyboard
* Calculates predicted marks using a simple formula
* Displays performance category
* Easy to understand and modify
* Beginner-friendly Python project

---

# 🛠 Technologies Used

* Python 3.x
* CSV Module (imported for future data storage)
* Functions
* Conditional Statements
* User Input

---

# 📂 Project Structure

```text
Student-Marks-Prediction/
│
├── marks_prediction.py      # Main Python program
├── README.md                # Project documentation
└── requirements.txt         # Required libraries (optional)
```

---

# 📦 Requirements

This project uses only Python's built-in libraries.

No external packages are required.

Python Version:

```text
Python 3.x
```

---

# ▶️ How to Run

1. Install Python 3.
2. Save the program as:

```text
marks_prediction.py
```

3. Open Terminal or Command Prompt.
4. Navigate to the project folder.
5. Run the program:

```bash
python marks_prediction.py
```

6. Enter:

   * Study hours per day
   * Attendance percentage

The program will display the predicted marks and performance level.

---

# 🧠 Working Principle

## Step 1: Input

The user enters:

* Study hours per day
* Attendance percentage

Example:

```text
Study Hours = 6
Attendance = 90
```

---

## Step 2: Prediction Formula

The program calculates predicted marks using:

```text
Marks = (Study Hours × 7) + (Attendance × 0.4)
```

If the calculated marks exceed 100, the value is limited to 100.

---

## Step 3: Performance Classification

The predicted marks are categorized as follows:

| Marks    | Performance |
| -------- | ----------- |
| 75 – 100 | Excellent   |
| 60 – 74  | Good        |
| 40 – 59  | Average     |
| Below 40 | Poor        |

---

# 📈 Example Output

### Example 1

```text
=== Student Marks Prediction System ===

Enter study hours per day: 6
Enter attendance percentage: 90

Predicted Marks: 78.0
Performance: Excellent
```

### Example 2

```text
Enter study hours per day: 4
Enter attendance percentage: 80

Predicted Marks: 60.0
Performance: Good
```

---

# ⚙ Prediction Formula

```text
Predicted Marks = (Study Hours × 7) + (Attendance × 0.4)
```

Example:

```text
Study Hours = 5

Attendance = 85%

Marks = (5 × 7) + (85 × 0.4)

Marks = 35 + 34

Marks = 69
```

---

# 📚 Concepts Used

This project demonstrates:

* Python Functions
* User Input
* Arithmetic Operations
* Conditional Statements (`if`, `elif`, `else`)
* Variables
* Output Formatting
* Basic Prediction Logic

---

# 🚀 Future Improvements

* Store student records using CSV files
* Read student data from a CSV file
* Train a Machine Learning model using historical student data
* Add graphical charts for performance analysis
* Develop a GUI using Tkinter
* Create a web application using Flask or FastAPI
* Predict grades using multiple features such as assignments, internal tests, and attendance

---

# 💡 Limitations

* Uses a simple mathematical formula instead of a trained AI model.
* Predictions are estimates and may not reflect actual academic performance.
* Does not currently save or analyze historical student data.

---

# 👩‍💻 Author

**Pratiksha Pasarge**

Diploma in Computer Engineering

---

# 📄 License

This project is created for educational and learning purposes. You are free to use, modify, and improve it for academic or personal use.
