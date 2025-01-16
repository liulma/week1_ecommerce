import pandas as pd

class DataTransformation:
    def __init__(self, dataframe=None):
        if dataframe is not None:
            self.df = dataframe
        else:
            self.df = pd.read_csv('ecommerce_sales.csv')

        

    def summarize_by_category(self):
        self.df['total_sale'] = self.df['quantity'] * self.df['unit_price']
        summary = self.df.groupby('product_category').agg(
            total_sales=('total_sale', 'sum'),
            avg_quantity_sold=('quantity', 'mean')
        )
        return summary


    def sales_per_month_pivot(self):
        self.df['total_sale'] = self.df['quantity'] * self.df['unit_price']
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        
        self.df['month'] = self.df['order_date'].dt.to_period('M')
        # self.df['month'] = self.df['order_date'].dt.strftime('%B')

        summary = self.df.pivot_table(
            values='total_sale', 
            index='month', 
            columns='product_category', 
            aggfunc='sum'
        )
        return summary

    def add_normalized_unit_prices (self):
        # self.df = self.df.drop('total_sale', axis=1)
        self.df = self.df.drop('month', axis=1)
        avg_price = self.df['unit_price'].mean()
        self.df['normalized_price'] = ((self.df['unit_price'] / avg_price) * 100).apply(lambda x: f"{x:.1f}")
        # self.df['normalized_price'] = self.df['normalized_price'].apply(lambda x: f"{x:.1f}")
        return self.df
