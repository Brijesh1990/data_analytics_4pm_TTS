# third party module 
# third party module is installable 
# pip install modulename
# python -m pip install modulename
# module name of third party 

# pandas 
# numpy 
# matplotlib 
# seaborn 
# requests

import pandas as pd 
import matplotlib.pyplot as plt
data ={
    "name":["kalpit","dhruv","bhavika","om","dhruvraj","divraj"],
    "salary":[20000,21000,21800,22900,120025,21700]
    
}

# print using pandas 
df=pd.DataFrame(data)
print(df)
# create title 
plt.title("Employee Name and Salary")
plt.xlabel("Name")
plt.ylabel("Salary")
# bar chart 
plt.bar(df["name"], df["salary"])
# sum of salary of employee 
print('--------sum of salary-----------')
print("sum of salary :",df["salary"].sum())
# pie chart
# plt.pie(df["salary"], labels=df["name"], autopct="%1.1f%%")
# display matplotlib data 
plt.show()