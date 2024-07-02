# importing the module
import numpy as np
  
# creating two matrices
k = [[2, 2], [8, 3]]
u = [[7, 9], [4, 6]]
print("Matrix k :")
print(k)
print("Matrix u :")
print(u)
  
# computing product
result = np.dot(k, u)
  
# printing the result
print("The matrix multiplication is :")
print(result)