import numpy as np

# Original array
original_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Border width
border_width = 1

# Adding a border to the array
array_with_border = np.pad(original_array, pad_width=border_width, mode='constant', constant_values=0)

# Display the original array and the array with border
print("Original Array:")
print(original_array)

print("\nArray with Border:")
print(array_with_border)
