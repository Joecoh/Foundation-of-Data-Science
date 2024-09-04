import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset (replace 'your_dataset.csv' with the actual file path)
diabetes_df = pd.read_csv('D:\\BTECH IT SECOND YEAR FILES\\5.Foundation of Data Science\\FODS lab question paper\\diabetes.csv')

# Display the first few rows of the dataset
print(diabetes_df.head())

# Bivariate Analysis: Multiple Regression
# Assuming 'Glucose', 'BMI', and 'Age' as independent variables and 'Outcome' as the dependent variable
X = diabetes_df[['Glucose', 'BMI', 'Age']]
y = diabetes_df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the multiple regression model
multiple_regression_model = LinearRegression()
multiple_regression_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred_multiple_regression = multiple_regression_model.predict(X_test)

# Evaluate the multiple regression model
mse_multiple_regression = mean_squared_error(y_test, y_pred_multiple_regression)
print(f"\nMultiple Regression Mean Squared Error: {mse_multiple_regression}")

# Print the coefficients and intercept
coefficients = multiple_regression_model.coef_
intercept = multiple_regression_model.intercept_
print(f"\nCoefficients: {coefficients}")
print(f"Intercept: {intercept}")