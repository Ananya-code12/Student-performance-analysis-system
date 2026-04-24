# basic stats
def basic_stats(data):
    print("\nBasic statistics:")

    print(data.describe())

# top 5 students based on marks
def top_students(data):
    print("\nTop 5 students based on marks:")

    top = data.sort_values(by="Marks", ascending=False).head(5)
    print(top)

# low performers
def low_performers(data):
    print("\nStudents with marks less than 50:")

    low = data[data["Marks"] < 50]
    print(low)

# study vs marks
def study_vs_marks(data):
    print("\nStudy hours vs marks:")

    print(data[["StudyHours", "Marks"]])

# attendance vs marks
def attendance_vs_marks(data):
    print("\nAttendance vs marks:")

    print(data[["Attendance", "Marks"]])

# group-based analysis
def group_analysis(data):
    print("\nAverage marks based on attendance:")

    print(data.groupby("Attendance")["Marks"].mean())

    print("\nAverage marks based on performance:")

    print(data.groupby("Performance")["Marks"].mean())

# insights
def insights():
    print("\nInsights:")

    print("1. Higher attendance generally leads to better marks.")
    
    print("2. Low attendance leads to poor performance.")
    
    print("3. Study hours help improve marks.")

    print("4. Effort score shows overall hard work.")

    print("5. Balance of study and attendance is important.")
              