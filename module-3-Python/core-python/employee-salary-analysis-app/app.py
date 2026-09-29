import pandas as pd
import matplotlib.pyplot as plt


employees = pd.DataFrame(
	{
		"name": [
			"Ava Patel",
			"Liam Chen",
			"Mia Johnson",
			"Noah Williams",
			"Sophia Garcia",
			"Ethan Brown",
			"Isabella Davis",
			"Lucas Wilson",
			"Amelia Martinez",
			"James Anderson",
			"Charlotte Taylor",
			"Benjamin Thomas",
		],
		"department": [
			"Engineering",
			"Engineering",
			"Engineering",
			"Sales",
			"Sales",
			"Sales",
			"Marketing",
			"Marketing",
			"Marketing",
			"Human Resources",
			"Human Resources",
			"Human Resources",
		],
		"salary": [
			92000,
			85000,
			98000,
			72000,
			68000,
			76000,
			70000,
			74000,
			78000,
			64000,
			67000,
			69000,
		],
	}
)

department_averages = employees.groupby("department")["salary"].mean()
overall_average = employees["salary"].mean()
above_average_employees = employees[employees["salary"] > overall_average]

print("Employee data:")
print(employees.to_string(index=False))
print("\nAverage salary by department:")
print(department_averages.to_string())
print(f"\nOverall average salary: ${overall_average:,.2f}")
print("\nEmployees earning above the overall average:")
print(above_average_employees.to_string(index=False))

department_averages.sort_values(ascending=False).plot(
	kind="bar",
	color="#3185a6",
	edgecolor="#235b73",
)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average salary ($)")
plt.xticks(rotation=30, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.35)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda value, _: f"${value:,.0f}"))
plt.tight_layout()
plt.show()
