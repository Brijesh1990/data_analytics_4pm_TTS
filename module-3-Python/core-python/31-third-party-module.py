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
    "age":[20,21,21,22,25,21]
    
}

# print using pandas 
df=pd.DataFrame(data)
print(df)
# create title 
plt.title("Employee Name and Age")
plt.xlabel("Name")
plt.ylabel("Age")
# bar chart 
plt.bar(df["name"], df["age"])
# pie chart
# plt.pie(df["age"], labels=df["name"], autopct="%1.1f%%")
# display matplotlib data 
plt.show()