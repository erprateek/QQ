Let's set up a simple data analysis problem involving an SQLite database and then perform the analysis using a Python script.

Problem Description:
You have been given a dataset containing information about employees in a company. The SQLite database has two tables:

"employees":

Columns: id (integer, primary key), name (text), age (integer), department (text), salary (real).
"departments":

Columns: id (integer, primary key), name (text), location (text).
Your task is to write a Python script to perform the following data analysis tasks:

Connect to the SQLite database.
Display the top 5 highest-paid employees along with their department and location.
Calculate and display the average age of employees.
Find the department with the highest number of employees.
Calculate the total salary expenditure for each department and display it in descending order.
Plot a bar chart showing the number of employees in each department.