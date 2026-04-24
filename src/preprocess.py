import pandas as pd

# Loading dataset
def load_data(path):
    print("....Loading data....")
    data = pd.read_csv(path)

    # show first few rows
    print("\nFirst 5 Rows:")
    print(data.head())

    # show shape
    print("\nShape:")
    print(data.shape)

    # show column names
    print("\nColumns:")
    print(list(data.columns))

    return data


# Data Cleaning
def clean_data(data):
    print("\n....Cleaning Data....")

    # check missing values
    print("\nMissing values:")
    print(data.isnull().sum())

    # fill missing values
    data["Marks"] = data["Marks"].fillna(data["Marks"].mean())

    data["StudyHours"] = data["StudyHours"].fillna(data["StudyHours"].median())


    # Removing outliers
    data = data[(data["StudyHours"] <= 15) & (data["Marks"] <= 100)]

    return data


# Feature Engineering
def feature_engineering(data):
    print("\n....Feature Engineering....")
    print("\n....Creating new columns....")

    performance_list = []

    for m in data["Marks"]:
        if m >= 80:
            performance_list.append("Excellent")
        elif m >= 60:
            performance_list.append("Good")
        else:
            performance_list.append("Needs Improvement")
            

    # add new column
    data["Performance"] = performance_list

    # Effort score
    data["EffortScore"] = data["StudyHours"] * data["Attendance"]

    return data