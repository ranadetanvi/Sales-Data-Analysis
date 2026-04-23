import matplotlib
matplotlib.use('TkAgg')   # Fix for VS Code plot display

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("sales.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Extract Month
df['Month'] = df['Date'].dt.month

# -----------------------------
# KPI Calculations
# -----------------------------
total_revenue = df['Sales'].sum()
total_orders = df['Orders'].sum()
total_customers = df['Customers'].sum()

print("\n===== KPI DASHBOARD =====")
print(f"Total Revenue: {total_revenue}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")

# -----------------------------
# Category Analysis
# -----------------------------
category_sales = df.groupby('Category')['Sales'].sum()

print("\n===== CATEGORY ANALYSIS =====")
print(category_sales)

# -----------------------------
# Monthly Trend
# -----------------------------
monthly_sales = df.groupby('Month')['Sales'].sum()

# -----------------------------
# Visualization
# -----------------------------

# 1. Bar Chart
plt.figure(figsize=(6,4))
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 2. Line Chart
plt.figure(figsize=(6,4))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# 3. Pie Chart (Fixed)
plt.figure(figsize=(5,5))

labels = category_sales.index
sizes = category_sales.values

plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Category Contribution")
plt.savefig("category_pie.png")
plt.show()

# -----------------------------
# Extra Metric
# -----------------------------
df['Avg_Order_Value'] = df['Sales'] / df['Orders']
avg_order_value = df['Avg_Order_Value'].mean()

# -----------------------------
# Insights
# -----------------------------
print("\n===== INSIGHTS =====")

print(f"Top Category: {category_sales.idxmax()}")
print(f"Lowest Category: {category_sales.idxmin()}")

print(f"Peak Month: {monthly_sales.idxmax()}")
print(f"Lowest Month: {monthly_sales.idxmin()}")

print(f"Average Order Value: {round(avg_order_value, 2)}")

print("Observation: Sales increase towards the end of the year.")
