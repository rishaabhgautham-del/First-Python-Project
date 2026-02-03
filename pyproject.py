#number, name, salary, department, find the sum of employee salary based on department
import pandas as pd

data_emp = pd.DataFrame(
    [[120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130], 
     ["Tim", "Bob", "Harry", "Sam", "Mike", "Kit", "Blake", "Art", "Mark", "Lee", "John"],
     [62300, 145900, 201800, 78400, 389600, 456200, 273100, 118500, 334700, 492000, 500000], 
     ["Marketing", "Production", "Finance", "HR", "Finance", "Finance", "Marketing", "Production", "HR", "HR", "Production"]], 
    columns = ["Number", "Name", "Salary", "Department"], index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

#can use groupby and agg of sum to find
data_emp = data_emp.T
grouped = data_emp.groupby("Department").agg('sum')



#1. Load dataset from csv file (without using pandas, and with using pandas, use pandas from excel file, w/o header name, pipe seperated, and json file)
data_loaded = pd.read_csv("City_of_Los_Angeles_Youth_Programs_2023-2024.csv") #with using pandas

import csv



#2. Display records from department A alone
finance_data = data_emp.groupby('Finance')
print(finance_data)
#3. Summary statistics of people who are getting more than $5,000 in salary (Who are working in city of SA)
new_dataset = data_emp[
#4. 
