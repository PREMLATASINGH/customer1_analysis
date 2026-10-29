import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


customers = ["CUST001", "CUST002", "CUST003", "CUST004", "CUST005"]
customer_names = ["Amit Sharma", "Priya Singh", "John Doe", "Sara Khan", "Michael Lee"]
cities = ["New York", "Chicago", "Houston", "San Francisco", "Boston"]

products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Monitor"]
categories = ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"]
unit_prices = [900, 600, 80, 40, 200]


np.random.seed(42)
rows = 500

data = {
    "OrderID": [f"ORD{1000+i}" for i in range(rows)],
    "CustomerID": np.random.choice(customers, rows),
    "CustomerName": np.random.choice(customer_names, rows),
    "City": np.random.choice(cities, rows),
    "Product": np.random.choice(products, rows),
    "Category": np.random.choice(categories, rows),
    "Quantity": np.random.randint(1, 10, rows),
    "UnitPrice": np.random.choice(unit_prices, rows),
    "Discount": np.round(np.random.uniform(0, 0.30, rows), 2),
    "TransactionDate": pd.date_range(start="2024-01-01", periods=rows, freq="D")
}

df = pd.DataFrame(data)


df["TotalAmount"] = df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

df.to_csv("sales_data.csv", index=False)

print("sales_data.csv created successfully!")
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.columns)
print(df.isnull().sum())
print(df.shape)
