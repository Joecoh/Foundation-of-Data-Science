import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt

# Load the dataset (replace 'your_dataset.csv' with the actual file path)
diabetes_df = pd.read_csv('D:\\BTECH IT SECOND YEAR FILES\\3.Foundation of Data Science\\FODS lab question paper\\diabetes.csv')

# Display the first few rows of the dataset
print(diabetes_df.head())

# Bivariate Analysis: Linear Regression
# Assuming 'Glucose' is the independent variable and 'Outcome' is the dependent variable
X = diabetes_df[['Glucose']]
y = diabetes_df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred_linear = linear_model.predict(X_test)

# Evaluate the linear regression model
mse_linear = mean_squared_error(y_test, y_pred_linear)
print(f"\nLinear Regression Mean Squared Error: {mse_linear}")

# Plot the linear regression line
plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred_linear, color='blue', linewidth=3)
plt.title('Linear Regression: Glucose vs Outcome')
plt.xlabel('Glucose')
plt.ylabel('Outcome')
plt.show()