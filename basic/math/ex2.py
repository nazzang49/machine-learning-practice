import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix)

# info
print(matrix.shape)
print(matrix.size)
print(matrix.ndim)
print(matrix.nbytes)

# vectorize => custom function which is applied to whole elements
vectorize = np.vectorize(lambda i: i + 100)
print(vectorize(matrix))

# broadcasting => not a function, but similar with vectorize
print(matrix + 100)