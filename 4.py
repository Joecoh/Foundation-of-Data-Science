import pandas as pd  # Import pandas as pd
import numpy as np  # Import numpy as np

# Sample data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'quality': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create a DataFrame
df = pd.DataFrame(exam_data, index=labels)

# Select specific columns and rows
selected_data = df.loc[['b', 'd','f', 'g'], ['score', 'quality']]

# Display the selected data
print("Selected specific columns and rows:")
print(selected_data)
