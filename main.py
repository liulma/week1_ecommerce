from data_transformation import DataTransformation
import pandas as pd

def main():
    data = read_file("ecommerce_sales (1).csv")
    print(data.head(10))
    
    convert_ids_to_int(data, "product_id")
    convert_ids_to_int(data, "customer_id")
    convert_ids_to_int(data, "order_id")
    fill_float_if_empty(data, "quantity")
    remove_if_zero(data, "quantity")
    fill_float_if_empty(data, "unit_price")
    fill_unknow_on_empty(data, "product_category")
    fill_unknow_on_empty(data, "country")
    print(data)
    
    manipulated_data = data_manipulation(data)
    print(manipulated_data)

    data_transformation = DataTransformation(data)
    category_summary = data_transformation.summarize_by_category()
    print(category_summary)
    sales_per_month = data_transformation.sales_per_month_pivot()
    print (sales_per_month)
    normalized_prices = data_transformation.add_normalized_unit_prices()
    print (normalized_prices)


def read_file(file_name: str):
    return pd.read_csv(file_name)

def convert_to_int(id : any):
    try:
        id = int(id)
        return id
    except ValueError:
        return -1

def convert_ids_to_int(df: pd.DataFrame, key: str):
    df[key] = df[key].apply(convert_to_int)

def fill_float_if_empty(df: pd.DataFrame, key: str):
    df[key] = df[key].fillna(0.00)

def remove_if_zero(df: pd.DataFrame, key: str):
    df.drop(index=df[df[key] == 0].index, inplace=True)

def fill_unknow_on_empty(df: pd.DataFrame, key: str):
    df[key] = df[key].fillna("Unknown")
    
def data_manipulation(data):
    data['total_price'] = data['quantity'] * data['unit_price']
    data['order_date'] = pd.to_datetime(data['order_date']) 
    data['order_weekday'] = data['order_date'].dt.day_name()
    data['order_month'] = data['order_date'].dt.month

    return data

main()