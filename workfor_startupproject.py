#In this project, you’ll work as a data analyst for a tech startup that is looking to improve its operations after a global pandemic has taken the world by storm.

#You will apply data transformation techniques to make better sense of the company’s data and help answer important questions such as:

#Is the company in good financial health?Does the company need to let go of any employees?Should the company allow employees to work from home permanently?

import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

print(financial_data.head())
month = financial_data["Month"]
revenue = financial_data["Revenue"]
expenses = financial_data["Expenses"]

plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Revenue')
plt.show()

plt.clf()

plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Expenses')
plt.show()

expense_overview = pd.read_csv("expenses.csv")
print(expense_overview.head(7))

expense_categories = expense_overview["Expense"]
proportions = expense_overview["Proportion"]
expense_categories_2 = ["Salaries", 'Advertising', 'Office Rent', 'Other']
proportions_2 = [.62, .15, .15, .08]
plt.clf()

plt.pie(proportions_2, labels = expense_categories_2)
plt.title("Expense Proportions")
plt.axis("Equal")
plt.tight_layout()
plt.show()

expense_cut = 'Salaries'

employees = pd.read_csv("employees.csv")
print(employees.head())

sorted_productivity = employees.sort_values(by = ['Productivity'])
print(sorted_productivity.head())

employees_cut = sorted_productivity[0:100]
print(employees_cut)

transformation = "standardization"

commute_times = employees["Commute Time"]
print(commute_times.describe())
commute_times_log = np.log(commute_times)

plt.clf()
plt.hist(commute_times_log)
plt.title('Commute Times')
plt.xlabel("Commute Time")
plt.ylabel('Frequency')
plt.show()