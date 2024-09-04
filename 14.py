import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

# Load the dataset
diabetes_df = pd.read_csv("D:\\BTECH IT SECOND YEAR FILES\\5.Foundation of Data Science\\FODS lab question paper\\rajendran\\Diabetes.csv")

# Display the first few rows of the dataset
print(diabetes_df.head())

# Specify the variable of interest
variable_of_interest = "Weight"

# Calculate and display the frequency of the variable of interest
frequency = diabetes_df[variable_of_interest].value_counts()
print(f"\nFrequency:\n{frequency}")

# Calculate and display the mean
mean_value = np.mean(diabetes_df[variable_of_interest])
print(f"\nMean: {mean_value}")

# Calculate and display the median
median_value = np.median(diabetes_df[variable_of_interest])
print(f"\nMedian: {median_value}")

# Calculate and display the mode
mode_value = diabetes_df[variable_of_interest].mode()[0]
print(f"\nMode: {mode_value}")

# Calculate and display the variance
variance_value = np.var(diabetes_df[variable_of_interest])
print(f"\nVariance: {variance_value}")

# Calculate and display the standard deviation
std_deviation_value = np.std(diabetes_df[variable_of_interest])
print(f"\nStandard Deviation: {std_deviation_value}")

# Calculate and display the skewness
skewness_value = skew(diabetes_df[variable_of_interest])
print(f"\nSkewness: {skewness_value}")

# Calculate and display the kurtosis
kurtosis_value = kurtosis(diabetes_df[variable_of_interest])
print(f"\nKurtosis: {kurtosis_value}")