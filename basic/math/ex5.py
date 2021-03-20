import numpy as np

matrix = np.array([[1, 2, 3],
                   [5, 4, 6],
                   [7, 10, 9],
                   [7, 10, 9]])

# diagonal
# default => (i, i)
print(matrix.diagonal())

# offset => not default
print(matrix.diagonal(offset=0))
print(matrix.diagonal(offset=1))
print(matrix.diagonal(offset=2))
print(matrix.diagonal(offset=-1))
print(matrix.diagonal(offset=-2))