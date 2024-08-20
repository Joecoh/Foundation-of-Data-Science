import pandas as pd  # Import pandas as pd

# Sample data
data = {
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Display the expected output
print("Expected Output:")
print(df)
