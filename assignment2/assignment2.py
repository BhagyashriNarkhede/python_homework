#Task 2
import csv
import traceback
import os
import custom_module
from datetime import datetime



def read_employees():
    employees = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    employees["fields"] = row
                else:
                    rows.append(row)

        employees["rows"] = rows
        return employees

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")

        message = str(e)
        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")


#Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

#Task 4
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match,employees["rows"]))
    return matches

#Task 6
def employee_find_2(employee_id):
    matches = list(
    filter(lambda row: int(row[employee_id_column]) == employee_id,employees["rows"])
    )
    return matches
#task 7:
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(
        key=lambda row: row[last_name_column]
    )

    return employees["rows"]

#Task 8:

def employee_dict(row):
    employee = {}

    for index,field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee[field] = row[index]
    return employee      

#Task 9:

def all_employees_dict():
    all_employees = {}
    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)
    
    return all_employees

#task 10:
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

#task 12
def read_minutes_file(filename):
    minutes = {}
    rows = []

    try:
        with open(filename,"r") as file:
            reader = csv.reader(file)

            for index,row in enumerate(reader):
                if index == 0:
                    minutes["fields"] = row
                else:
                    rows.append(tuple(row)) 

        minutes["rows"] = rows
        return minutes
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")


def read_minutes():
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")

    return minutes1, minutes2
#minutes1, minutes2 = read_minutes()
#print(minutes1)
#print(minutes2)


#task 13:
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    return minutes1_set.union(minutes2_set)

#task 14
def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(


        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),minutes_list
        )
    )
    return minutes_list

#task 15

# Task 15

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    converted_list = list(
        map(
            lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
            minutes_list
        )
    )

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(minutes1["fields"])

        writer.writerows(converted_list)

    return converted_list

employees = read_employees()
print(employees)

employee_id_column = column_index("employee_id")

sort_by_last_name()
print(employees)

set_that_secret("my new secret")
print(custom_module.secret)

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

minutes_set = create_minutes_set()
print(minutes_set)

minutes_list = create_minutes_list()
print(minutes_list)


minutes_sorted = write_sorted_list()
print(minutes_sorted)

#print(employee_id_column)
#print(employee_dict(employees["rows"][0]))
#print(all_employees_dict())



