from src.preprocess import load_data, clean_data, feature_engineering
from src.analysis import basic_stats, top_students, low_performers,study_vs_marks,attendance_vs_marks, group_analysis, insights

#main function to run project
def main():
    #file path
    path = "data/student_dataset.csv"

    # step 1: load data
    data = load_data(path)

    # step 2: clean data
    data = clean_data(data)

    # step 3: feature engineering
    data = feature_engineering(data)

    # step 4: analysis
    basic_stats(data)
    top_students(data)
    low_performers(data)
    study_vs_marks(data)
    attendance_vs_marks(data)
    group_analysis(data)
    insights()

#run program   
if __name__ == "__main__":
    main()