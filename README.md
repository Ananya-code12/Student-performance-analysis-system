# Student Performance Analysis System

---------This project is created for mini project submission. --------

## Objective

The main objective of this project is to analyze student data and understand how study hours and attendance affect their marks.
This project helps in finding patterns and improving student performance using basic data analysis.

## Dataset Description

The dataset contains the following columns:

* StudyHours → Number of hours studied per day
* Attendance → Attendance percentage of student
* Marks → Marks obtained by student

## Steps Performed

1. Data Loading
   The dataset is loaded using pandas and basic information is displayed.

2. Data Cleaning
   Missing values are handled and unwanted data (outliers) is removed.

3. Feature Engineering
   New columns are created:

   * Performance (Excellent / Good / Needs Improvement)
   * EffortScore (StudyHours × Attendance)

4. Data Analysis

   * Top 5 students are identified
   * Students with low marks are found
   * Study hours and attendance are compared with marks

## Key Insights

1. Higher attendance generally leads to better marks.
2. Low attendance leads to poor performance.
3. Study hours help improve marks.
4. Effort score shows overall hard work.
5. Balance of study and attendance is important.

## How to Run

Step 1: Install required libraries
pip install -r requirements.txt

Step 2: Run the program
python main.py

## Project Structure

student-performance-analysis/
│
├── data/
│   └── student_dataset.csv
│
├── src/
│   ├── preprocess.py
│   ├── analysis.py
│
├── main.py
├── requirements.txt
├── README.md

