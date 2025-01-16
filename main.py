import pandas as pd

def main():
    data = read_file("ecommerce_sales (1).csv")
    print(data.head(10))


def read_file(file_name: str):
    return pd.read_csv(file_name)

main()