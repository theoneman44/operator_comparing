import pandas as pd
from config import XLSX


reader = pd.read_excel(XLSX, sheet_name="Лист1")
reader.to_csv('input_data_from.csv')
