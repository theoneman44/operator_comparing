import pandas as pd


reader1 = pd.read_excel('input_data.xlsx', sheet_name="Лист1")
reader1.to_csv('input_data_from.csv')

reader2 = pd.read_excel('links.xlsx', sheet_name="Лист1")
reader2.to_csv('links.csv')
