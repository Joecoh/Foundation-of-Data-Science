import pandas as pd  # Import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 30, 22, 35], 
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

# Create a Pandas DataFrame
df = pd.DataFrame(data) 

# Print the DataFrame
print("Pandas DataFrame:")
print(df)
