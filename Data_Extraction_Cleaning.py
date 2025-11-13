import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

# Read the API keys and download the dataset
api = KaggleApi()
api.authenticate()
api.dataset_download_files('harshsingh2209/supply-chain-analysis', path='./data', unzip=True)
print("dataset downloaded")

# read the resulting CSV file with pandas
df = pd.read_csv('supply_chain_data.csv')
print(df.head())

#Inspect the columns' data types
df.info()

#Remove unnecessary columns
df.drop(columns=['Customer demographics', 'Inspection results', 'Defect rates'], inplace=True)

#Check for null values in the dataset
df.isnull().sum()

#Specifying the column names that I want to use
new_cols_dict = {
    'Product type': 'Product_type',
    'Number of products sold': 'Products_sold',
    'Revenue generated': 'Revenue',
    'Stock levels' : 'Stock_levels',
    'Lead times' : 'Supplier_Lead_time',
    'Order quantities' : 'Order_quantities',
    'Shipping times' : 'Shipping_times',
    'Shipping carriers' : 'Shipping_carriers',
    'Shipping costs' : 'Shipping_costs',
    'Supplier name' : 'Supplier_name',
    'Lead time' : 'Delivery_lead_time',
    'Production volumes' : 'Production_volumes',
    'Manufacturing lead time' : 'Manufacturing_lead_time',
    'Manufacturing costs' : 'Manufacturing_costs',
    'Transportation modes' : 'Transportation_modes',
}

#Renaming the columns to those specified in the previous dictionary
df.rename(columns=new_cols_dict, inplace=True)
print(df)

#Check for unique values in dimension columns
columns_to_check = ['Product_type', 'Supplier_name', 'Location', 'Transportation_modes']

unique_values = {col: df[col].unique() for col in columns_to_check}

print(unique_values)

#download the Excel file with the modified dataset
df.to_excel('supply_chain_data.xlsx', sheet_name='Data', index=False)
