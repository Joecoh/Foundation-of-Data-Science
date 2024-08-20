import pandas as pd  # Import pandas as pd

# Sample data with arrays
data = {
    'Column1': [1, 2, 3, 4], 
    'Column2': ['A', 'B', 'C', 'D'], 
    'Column3': [10.5, 20.3, 15.2, 8.7]
}

# Add more columns as needed

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("Pandas DataFrame:")
print(df)
