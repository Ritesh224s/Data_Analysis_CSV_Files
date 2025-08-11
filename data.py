# -----------------------------
# Task 5: Data Analysis on CSV Files
# -----------------------------

# Step 1: Install required libraries (only for Colab)
# Uncomment the line below if running in Google Colab
# !pip install pandas matplotlib

# Step 2: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 3: Load CSV file
# Replace 'sales_data.csv' with your file name
data = pd.read_csv('sales_data.csv')

# Step 4: Display first few rows
print("First 5 Rows of Data:")
print(data.head())

# Step 5: Check data info
print("\nData Info:")
print(data.info())

# Step 6: Basic Statistics
print("\nBasic Statistics:")
print(data.describe())

# Step 7: Group data by 'Product' and calculate total sales
sales_by_product = data.groupby('Product')['Sales'].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)

# Step 8: Plot sales by product
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Step 9: Group by 'Region' and calculate total sales
sales_by_region = data.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:")
print(sales_by_region)

# Step 10: Plot sales by region
sales_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Sales Distribution by Region')
plt.ylabel('')
plt.show()
