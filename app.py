# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------- Helper Function: Calculate Total, Average, and Grade ----------

def calculate_metrics(df):
    subjects = ['Math', 'Science', 'English', 'History', 'Computer']

    # Calculate total marks
    df['Total'] = df[subjects].sum(axis=1)

    # Calculate average marks
    df['Average'] = df['Total'] / len(subjects)

    # Assign grades based on average
    df['Grade'] = df['Average'].apply(assign_grade)

    return df

# ----------------------------- Helper Function: Grade Logic -----------------------------
def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'

# ----------------------------- Plot: Subject-wise Average Marks (Bar Chart) -----------------------------
def plot_subject_wise_avg(df):
    # Calculate average for each subject
    subject_avg = df[['Math', 'Science', 'English', 'History', 'Computer']].mean()

    # Create bar chart
    fig, ax = plt.subplots()
    subject_avg.plot(kind='bar', ax=ax, color='skyblue')

    ax.set_title("Subject-wise Average Marks")
    ax.set_ylabel("Average Marks")
    ax.set_ylim(0, 100)  # Set Y-axis from 0 to 100

    # Display chart in Streamlit
    st.pyplot(fig)

# ----------------------------- Plot: Grade Distribution (Pie Chart) -----------------------------
def plot_grade_distribution(df):
    # Count how many students got each grade
    grade_counts = df['Grade'].value_counts()

    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title("Grade Distribution")

    # Display chart in Streamlit
    st.pyplot(fig)

# ----------------------------- Main Streamlit App -----------------------------
def main():
    # Set Streamlit page settings
    st.set_page_config(page_title="Student Performance Dashboard", layout="centered")
    st.title("📊 Student Performance Dashboard")

    # Upload CSV or use default file
    uploaded_file = st.file_uploader("cleaned_student_data", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.info("Using default dataset: cleaned_student_data.csv")
        df = pd.read_csv("cleaned_student_data.csv")

    # Calculate total, average, and grade
    df = calculate_metrics(df)

    # Show student performance table
    st.subheader("📋 Student Performance Table")
    st.dataframe(df[['StudentID', 'Name', 'Math', 'Science', 'English', 'History', 'Computer', 'Total', 'Average', 'Grade']])

    # Show Topper
    topper = df.loc[df['Average'].idxmax()]
    st.subheader("🏆 Topper Highlight")
    st.markdown(f"**{topper['Name']}** is the topper with an average score of **{topper['Average']:.2f}** and grade **{topper['Grade']}**.")

    # Charts and Visualizations
    st.subheader("📈 Visualizations")
    col1, col2 = st.columns(2)

    with col1:
        plot_subject_wise_avg(df)

    with col2:
        plot_grade_distribution(df)

# ------------------ Run the app ------------------
if __name__ == "__main__":
    main()
