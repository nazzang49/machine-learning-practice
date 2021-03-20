import numpy as np

matrix = np.array([[1, 2, 3],
                   [5, 4, 6],
                   [7, 10, 9],
                   [7, 10, 9]])

# reshape
reshaped_matrix1 = matrix.reshape(2, 6)
print(reshaped_matrix1)
print(reshaped_matrix1.shape)

# -1 => automatically at the most
reshaped_matrix2 = matrix.reshape(-1)
print(reshaped_matrix2)
print(reshaped_matrix2.shape)

# transpose
print(matrix.T)

# col vector => row vector
print(np.array([
    [1],
    [2],
    [3],
    [4],
    [5]]).T)

matrix = np.array([[[1, 2],
                    [3, 4],
                    [5, 6]],

                  [[7, 8],
                   [9, 10],
                   [11, 12]]])
# 2, 3, 2
print(matrix.shape)
# 2, 2, 3
print(matrix.transpose((0, 2, 1)).shape)

# flatten => multi dimensions to 1-dim
flatten = matrix.flatten()
reshape = matrix.reshape(-1)
print(flatten)
print(reshape)

# flatten => totally new array
matrix[0][1][1] = 300
print(flatten)
print(reshape)