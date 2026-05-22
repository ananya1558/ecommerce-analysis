import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv('ecommerce.csv', encoding='latin1')

# Display First Rows
print(df.head())

# Dataset Info
print(df.info())

# Null Values
print(df.isnull().sum())

# Basic KPIs
total_sales = df['sales'].sum()
total_profit = df['profit'].sum()
total_orders = df['order_id'].nunique()

print(f"Total Sales: {total_sales}")
print(f"Total Profit: {total_profit}")
print(f"Total Orders: {total_orders}")

# Top Categories
category_sales = df.groupby('category')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=20)
plt.show()

# Monthly Sales Trend
df['order_date'] = pd.to_datetime(df['order_date'])

df['Month'] = df['order_date'].dt.month

monthly_sales = df.groupby('Month')['sales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid()
plt.show()

# Region-wise Profit
region_profit = df.groupby('region')['profit'].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=region_profit.index, y=region_profit.values)
plt.title('Region-wise Profit')
plt.xlabel('Region')
plt.ylabel('Profit')
plt.show()

# Top 10 Products
top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Products')
plt.xlabel('Sales')
plt.ylabel('Product')
plt.show()

# Discount Impact on Profit
plt.figure(figsize=(8,5))
sns.scatterplot(x=df['discount'], y=df['profit'])
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.show()

# Save Cleaned Dataset
df.to_csv('cleaned_ecommerce.csv', index=False)

print("Analysis Completed Successfully!")