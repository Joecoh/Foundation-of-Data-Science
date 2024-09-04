# READ FROM TEXT FILE:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the data is in a CSV file
file_path = 'path/to/iris_data.csv'
iris_data_csv = pd.read_csv(file_path)

# READ FROM EXCEL FILE:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the data is in an Excel file
excel_file_path = 'path/to/iris_data.xlsx'
iris_data_excel = pd.read_excel(excel_file_path)

# READ FROM WEB FILE:

import numpy as np
import pandas as pd

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list'
df = pd.read_html(url)

df[0]

match = "Metcalf Bank"