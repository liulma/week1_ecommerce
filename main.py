import pandas as pd

def main():
    data = read_file("ecommerce_sales (1).csv")
    print(data.head(10))

    manipulated_data = data_manipulation(data)
    print(manipulated_data)

def read_file(file_name: str):
    return pd.read_csv(file_name)

def data_manipulation(data):
    data['total_price'] = data['quantity'] * data['unit_price']
    data['order_date'] = pd.to_datetime(data['order_date']) 
    data['order_weekday'] = data['order_date'].dt.day_name()
    data['order_month'] = data['order_date'].dt.month

    return data


main()