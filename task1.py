import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("train.csv")

# Clean column names (THIS LINE FIXES EVERYTHING)
df.columns = df.columns.str.strip()

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Sort by date
df = df.sort_values('Order Date').reset_index(drop=True)

# Group sales by date
df_daily = df.groupby('Order Date')['Sales'].sum().reset_index()

# Check output
print(df_daily.head())

# Plot
plt.figure(figsize=(12,6))
plt.plot(df_daily['Order Date'], df_daily['Sales'])
plt.title("Total Daily Sales Over Time")
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()