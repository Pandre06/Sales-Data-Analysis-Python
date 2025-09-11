import pandas as pd

DATA_FILE = '../data/sales_data.csv'  # Adjust path if needed

def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    return df

def calculate_revenue(df):
    df['Revenue'] = df['Quantity'] * df['Price']
    total_revenue = df['Revenue'].sum()
    return total_revenue

def top_selling_products(df, top_n=5):
    product_revenue = df.groupby('Product')['Revenue'].sum()
    top_products = product_revenue.sort_values(ascending=False).head(top_n)
    return top_products

def sales_over_time(df):
    monthly_sales = df.resample('ME', on='Date')['Revenue'].sum()
    return monthly_sales

def main():
    print("Loading sales data...")
    df = load_data(DATA_FILE)54
    
    print("\n🔍 Data Preview (first 5 rows):")
    print(df.head())

    print("Calculating total revenue...")
    total_revenue = calculate_revenue(df)
    print(f"Total Revenue: ${total_revenue:,.2f}")

    print("\nTop Selling Products:")
    top_products = top_selling_products(df)
    print(top_products.to_string())

    print("\nSales Over Time (Monthly):")
    monthly_sales = sales_over_time(df)
    print(monthly_sales.to_string())

if __name__ == "__main__":
    main()
