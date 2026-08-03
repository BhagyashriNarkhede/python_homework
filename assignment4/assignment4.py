#task 1:
#create a dataFrame from a dictionary

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

print(task1_data_frame)

# Now Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

print(task1_with_salary)

# 3. Modify an existing column
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1

print(task1_older)

# Save the dataframe as a csv file
task1_older.to_csv("employees.csv", index=False)

#task2: Read data from csv file:

task2_employees = pd.read_csv("employees.csv")
print ("\nEmployees loaded from CSV:")
print(task2_employees)

#Read data from JSON file:

json_employees = pd.read_json("additional_employees.json")

print("\nEmployees loaded from JSON:")
print(json_employees)

# Combine DataFrames

more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)
print("\nCombined Employees:")
print(more_employees)

#task 3:Data Inspection:
first_three = more_employees.head(3)

print ("\nFirst Three Employees:")
print(first_three)

last_two = more_employees.tail(2)

print("\nLast Two Employees:")
print(last_two)

employee_shape = more_employees.shape

print("\nEmployee DataFrame Shape:")
print(employee_shape)

print("\nEmployee DataFrame Information:")
more_employees.info()

#task 4:Data cleaning
dirty_data = pd.read_csv("dirty_data.csv")
print("\nDirty data")
print(dirty_data)

clean_data = dirty_data.copy()

clean_data = clean_data.drop_duplicates()
print("\nAfter Removing Duplicates:")
print(clean_data)


clean_data["Age"] = pd.to_numeric(
    clean_data["Age"],
    errors="coerce"
)
print("\nAge Converted:")
print(clean_data)

clean_data["Salary"] = clean_data["Salary"].replace(
    ["unknown", "n/a"],
    pd.NA
)

clean_data["Salary"] = pd.to_numeric(
    clean_data["Salary"],
    errors="coerce"
)

print("\nSalary Converted:")
print(clean_data)


clean_data["Age"] = clean_data["Age"].fillna(
    clean_data["Age"].mean()
)

clean_data["Salary"] = clean_data["Salary"].fillna(
    clean_data["Salary"].median()
)

print("\nMissing Values Filled:")
print(clean_data)

clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"],format="mixed"
)

print("\nHire Date Converted:")
print(clean_data)

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()

clean_data["Department"] = (
    clean_data["Department"]
    .str.strip()
    .str.upper()
)

print("\nFinal Clean Data:")
print(clean_data)
