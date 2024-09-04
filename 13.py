import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Bivariate Analysis: Logistic Regression
# Assuming 'Glucose' is the independent variable and 'Outcome' is the dependent variable
X_logistic = diabetes_df[['Glucose']]
y_logistic = diabetes_df['Outcome']

# Split the data into training and testing sets
X_train_logistic, X_test_logistic, y_train_logistic, y_test_logistic = train_test_split(
    X_logistic, y_logistic, test_size=0.2, random_state=42
)

# Create and fit the logistic regression model
logistic_model = LogisticRegression()
logistic_model.fit(X_train_logistic, y_train_logistic)

# Make predictions on the test set
y_pred_logistic = logistic_model.predict(X_test_logistic)

# Evaluate the logistic regression model
accuracy_logistic = accuracy_score(y_test_logistic, y_pred_logistic)
print(f"\nLogistic Regression Accuracy: {accuracy_logistic}")

# Plot the logistic regression curve
plt.scatter(X_test_logistic, y_test_logistic, color='black')
plt.plot(X_test_logistic, logistic_model.predict_proba(X_test_logistic)[:, 1], color='blue', linewidth=3)
plt.title('Logistic Regression: Glucose vs Outcome')
plt.xlabel('Glucose')
plt.ylabel('Outcome Probability')
plt.show()