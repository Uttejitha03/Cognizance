import numpy as np
def generate(value):
    return 3**value
arr = np.array([])
for value in range(0, 20):
    # Appends the new value to the end of the numpy array
    arr = np.append(arr, [generate(value)])
print(arr)