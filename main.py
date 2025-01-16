import pandas as pd

def main():
    data = read_file("ecommerce_sales (1).csv")
    convert_ids_to_int(data, "product_id")
    convert_ids_to_int(data, "customer_id")
    convert_ids_to_int(data, "order_id")
    fill_float_if_empty(data, "quantity")
    remove_if_empty(data, "quantity")
    fill_float_if_empty(data, "unit_price")
    fill_unknow_on_empty(data, "product_category")
    fill_unknow_on_empty(data, "country")
    print(data)

def read_file(file_name: str):
    return pd.read_csv(file_name)

def convert_to_int(id : any):
    try:
        print(id)
        id = int(id)
        return id
    except ValueError:
        return -1

def convert_ids_to_int(df: pd.DataFrame, key: str):
    df[key] = df[key].apply(convert_to_int)

def fill_float_if_empty(df: pd.DataFrame, key: str):
    df[key] = df[key].fillna(0.00)

def remove_if_empty(df: pd.DataFrame, key: str):
    df.drop(index=df[df[key] == 0].index, inplace=True)

def fill_unknow_on_empty(df: pd.DataFrame, key: str):
    df[key] = df[key].fillna("Unknown")

main()