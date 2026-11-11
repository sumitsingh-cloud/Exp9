
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Sumit", "Shuvam", "Shivam", "Bala", "Divaya", "Esha", "Gita"],
    "Salary": [2000, 3000, 4000, 1900, 4500, 2500, 3600],
    "E-ID": [101, 102, 103, 104, 105, 106, 107]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display
print("Employee Dataset")
print(df)

# Bar Chart
plt.figure()
plt.bar(df["Name"], df["Salary"])
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Salary: Bar Chart")
plt.show()

# Line Chart
plt.figure()
plt.plot(df["Name"], df["Salary"], marker="o")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Salary: Line Chart")
plt.show()

# Pie Chart
plt.figure()
plt.pie(df["Salary"], labels=df["Name"], autopct="%1.1f%%")
plt.title("Employee Salary: Pie Chart")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(df["E-ID"], df["Salary"])
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.title("Employee ID: Scatter Chart")
plt.show()

# Histogram
plt.figure()
plt.hist(df["Salary"], bins=5)
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.title("Salary Distribution: Histogram")
plt.show()
