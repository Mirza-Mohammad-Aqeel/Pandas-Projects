
import pandas as pd
student_database = pd.read_csv('pandas_01_student_database_cleaner.csv')
student_database.drop_duplicates()
student_database.drop_na()

employee_database = pd.read_csv('pandas_02_employee_salary_analyzer.csv')
employee_database.drop_duplicates()
employee_database.drop_na()

movie_database = pd.read_csv('pandas_03_movie_dataset_investigator.csv')
movie_database.drop_duplicates()
movie_database.drop_na()

e_commerce_sales = pd.read_csv('pandas_04_ecommerce_sales_cleaner.csv')
e_commerce_sales.drop_duplicates()
e_commerce_sales.drop_na()

school_attendace = pd.read_csv('pandas_05_school_attendance_analyzer.csv')
school_attendace.drop_duplicates()
school_attendace.drop_na()

gaming_dataset = pd.read_csv('pandas_06_gaming_dataset_investigation.csv')
gaming_dataset.drop_duplicates()
gaming_dataset.drop_na()

tech_database = pd.read_csv('pandas_07_tech_product_cleaner')
tech_database.drop_duplicates()
tech_database.dropna()
tech_database['Brand'] = tech_database['Brand'].replace({"lenovo":"Lenovo"})
tech_database['Brand'] = tech_database['Brand'].replace({"DELL":"Dell"})
tech_database['Brand'] = tech_database['Brand'].replace({"hp":"Hp"})
tech_database['Brand'] = tech_database['Brand'].replace({"HP":"Hp"})

customer_p_database = pd.read_csv('pandas_08_customer_purchase_analysis.csv')
customer_p_database.drop_duplicates()
customer_p_database.dropna()

sports_stats_database = pd.read_csv('pandas_09_sports_statistics_analyzer.csv')
sports_stats_database.drop_duplicates()
sports_stats_database.dropna()

final_database = pd.read_csv('pandas_10_full_data_cleaning_challenge.csv')
final_database.dropna()
final_database.drop_duplicates()
final_database['category'] = final_database['category'].replace({"a":"A","b":"B","c":"C"})
final_database['status'] = final_database['status'].replace({"INACTIVE":"Inactive","active":"Active"})
final_database['record_id'] = final_database['record_id'].abs().astype(int)
final_database['age'] = final_database['age'].abs.astype(int)
final_database['score'] = final_database['score'].abs.astype(int)
final_database['income'] = final_database['income'].abs.astype(float)
final_database['visits'] = final_database['visits'].abs.astype(int)
final_database['amount'] = final_database['amount'].abs.astype(int)

# Student Database

print(f"Student Database =")
print()
print(student_database.to_string())
print()

print(f"Average Math Score = {student_database['Math'].mean()}")
print(f"Average Physics Score = {student_database['Physics'].mean()}")
print(f"Average Chemistry Score = {student_database['Chemistry'].mean()}")
print(f"Average Computer Score = {student_database['Computer_Science'].mean()}")
print()

print(f"Highest score in Math = {student_database['Math'].max()}")
print(f"Highest score in Physics = {student_database['Physics'].max()}")
print(f"Highest score in Chemistry = {student_database['Chemistry'].max()}")
print(f"Highest score in Computer Science = {student_database['Computer_Science'].max()}")
print()

print(f"Lowest score in Math = {student_database['Math'].min()}")
print(f"Lowest score in Physics = {student_database['Physics'].min()}")
print(f"Lowest score in Chemistry = {student_database['Chemistry'].min()}")
print(f"Highest score in Computer Science = {student_database['Computer_Science'].min()}")
print()

# Employee Salary Analyzer

print(f"Employee Database =")
print()
print(employee_database.to_string())
print()

print(f"Highest salary = {employee_database['Salary'].max()}")
print(f"Lowest salary = {employee_database['Salary'].min()}")
print()

print(f"Employees with High performance =")
print()
print(employee_database[employee_database['Performace'] == "Excellent"])
print()

print(f"Employees with High salaries =")
print()
print(employee_database[employee_database['Salary'] > 80000])
print()

# Movie Dataset Investigator

print(f"Movie Database =")
print()
print(movie_database.to_string())
print()

print(f"Highest rated Movies =")
print()
print(employee_database[employee_database['Rating'] > 7])
print()

print("Highest revenue making Movies =")
print()
print(employee_database[employee_database['Revenue_Million'] > 19])
print()

print(f"Oldest movies =")
print()
print(employee_database[employee_database['Year'] < 1995])
print()


print(f"Newest movies =")
print()
print(employee_database[employee_database['Year'] > 1995])
print()

print(f"Highest costing Movies =")
print()
print(employee_database[employee_database['Budget_Million'] > 20])
print()

# E-Commerce Sales Cleaner

print(f"E-Commerce Sales =")
print()
print(e_commerce_sales.to_string())
print()

print("Most Expensive Products =")
print()
print(e_commerce_sales[e_commerce_sales['Price'] > 90])
print()

print(f"Most Quantive Products =")
print()
print(e_commerce_sales[e_commerce_sales['Quantity'] > 4])
print()

print(f"Revenues =")
print()
print(e_commerce_sales[e_commerce_sales['Price'] * e_commerce_sales['Quantity']])
print()

# School Attendance Analyzer

print(f"Student Attendace Database =")
print()
print(school_attendace.to_string())
print()

print(f"Best attendance =")
print()
print(school_attendace[school_attendace['Days_Present'] > 150])
print()

print(f"Best attendance =")
print()
print(school_attendace[school_attendace['Days_Present'] < 130])
print()

print(f"Class Averages =")
print()
print(school_attendace[school_attendace['Days_Present'].mean()])
print()

# Gaming Dataset Investigation

print(f"Games Database =")
print()
print(gaming_dataset.to_string())
print()

print(f"Most popular Games =")
print()
print(gaming_dataset[gaming_dataset['Players_Millions'] > 8])
print()

print(f"Expense Games =")
print()
print(gaming_dataset[gaming_dataset['Price'] > 11])
print()

print(f"Highest rated Games =")
print()
print(gaming_dataset[gaming_dataset['Rating'] > 8])
print()

print(f"Expense Games with Low ratings =")
print()
print(gaming_dataset[gaming_dataset['Price'] > 11 & gaming_dataset['Rating'] < 5])
print()

print(f"Oldest genres =")
print()
print(gaming_dataset[gaming_dataset['Release_Year'] < 2010])
print()

# Tech Product Dataset Cleaner

print(f"Tech Products Database =")
print()
print(tech_database.to_string())
print()

print(f"Products with High ram = ")
print()
print(tech_database[tech_database['Ram_GB'] > 64])
print()

print(f"Products with High storage = ")
print()
print(tech_database[tech_database['Storage_GB'] > 256])
print()

print(f"Most Expensive Products = ")
print()
print(tech_database[tech_database['Price'] > 1000])
print()

print(f"Products with most Battery hours = ")
print()
print(tech_database[tech_database['Battery_Hours'] > 5])
print()

# Customer Purchase Analysis

print(f"Customer Purchases Database =")
print()
print(customer_p_database.to_string())

print(f"Oldest Customers =")
print()
print(customer_p_database[customer_p_database['Age'] > 50])
print()

print(f"Most Expensive Purchases =")
print()
print(customer_p_database[customer_p_database['Price'] > 50])
print()

print(f"Recent Purchases =")
print()
print(customer_p_database[customer_p_database['Purchase_Date'] < "2026-5-1"])
print()

print(f"Total spendings =")
print()
print(customer_p_database[customer_p_database['Quantity'] * customer_p_database['Price']])
print()

# Sports Statistics Analyzer

print(f"Sports Statistics Database =")
print()
print(sports_stats_database.to_string())
print()

print(f"Top Assist Players =")
print()
print(sports_stats_database[sports_stats_database['Assists'] > 100])
print()

print(f'Most match-player Players =')
print()
print(sports_stats_database[sports_stats_database['Matches'] > 30])
print()

print(f"Longest matches =")
print()
print(sports_stats_database[sports_stats_database['Minutes_Per_Game'] > 30.0])
print()

# Pandas Data Cleaning Challenge

print(f"Final Database =")
print()
print(final_database.to_string())
print()

print(f"Oldest ages = ")
print()
print(final_database[final_database['age'] > 65])
print()

print(f"Highest incomes =")
print()
print(final_database[final_database['income'] > 89000])
print()

print(f"Highest visits =")
print()
print(final_database[final_database['visits'] > 60])
print()

print(f"Highest scores =")
print()
print(final_database[final_database['score'] > 50.0])
print()



