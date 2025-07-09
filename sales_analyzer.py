import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales(filename):
    # Bug 1: Wrong file extension assumption
    data = pd.read_excel(filename)  # File is actually CSV
    
    # Bug 2: Column name doesn't exist
    data['date'] = pd.to_datetime(data['order_date']) 
    
    # Bug 3: Logic error in quarter calculation
    data['quarter'] = data['date'].dt.month // 4 + 1
    
    # Bug 4: Trying to group by non-existent column
    quarterly_sales = data.groupby(['quarter', 'product_type'])['sales'].sum()
    
    return quarterly_sales

def plot_sales_trends(data):
    # Bug 5: Undefined variable
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data['month'], monthly_data['total_sales'])
    plt.title('Sales Trends')
    plt.show()

def calculate_profit_margin(data):
    # Bug 6: Division by zero potential
    data['profit_margin'] = (data['profit'] / data['sales_amount']) * 100
    return data

# Bug 7: File doesn't exist
result = analyze_sales('sales_data_2024.xlsx')
print(result)

# Bug 8: Calling function with wrong parameter
plot_sales_trends() 