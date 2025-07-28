# Student Performance Dashboard

This is a Streamlit-based web application that analyzes student performance data. The app allows users to upload a CSV file of student marks, computes useful metrics such as total and average scores, assigns grades, and presents insightful visualizations.

---

## Features

- Upload and analyze student data from CSV files.
- Automatically calculate:
  - Total marks
  - Average score
  - Grade assignment
- Visualizations:
  - Bar chart of student marks
  - Average comparison per subject
  - Grade distribution pie chart

---

## Technologies Used

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – for web interface
- [Pandas](https://pandas.pydata.org/) – for data handling
- [Matplotlib](https://matplotlib.org/) – for visualization

---

## File Structure

project/
├── app.py # Main Streamlit application
├── student_data.csv # Raw student data
├── cleaned_student_data.csv # Cleaned data (optional/preprocessed)
├── requirements.txt # Python dependencies
└── README.md # Project overview

---

## How to Run the Project

1. **Clone the repository** or download the ZIP.

2. **Install dependencies:**

```bash

pip install -r requirements.txt

streamlit run app.py

