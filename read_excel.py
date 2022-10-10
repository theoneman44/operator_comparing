import pandas as pd


reader = pd.read_excel('input_data.xlsx', sheet_name="Лист1")
reader.to_csv('input_data_from.csv')
