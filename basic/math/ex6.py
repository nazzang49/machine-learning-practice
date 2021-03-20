import numpy as np

matrix = np.array([[1, -1, 3],
                   [1, 1, 6],
                   [3, 8, 9]])

# 고유값 / 고유벡터 at n x n matrix
# https://darkpgmr.tistory.com/105
eigen_values, eigen_vectors = np.linalg.eig(matrix)
print(eigen_values)
print(eigen_vectors)

# dot
print(np.dot(np.array([1, 2, 3]), np.array([4, 5, 6])))

# add
print(np.add(np.array([1, 2, 3]), np.array([4, 5, 6])))

# sub
print(np.subtract(np.array([1, 2, 3]), np.array([4, 5, 6])))

# matmul
print(np.matmul(matrix, matrix))

# inverse matrix
matrix = np.array([[1, 4],
                   [2, 5]])
print(np.linalg.inv(matrix))
print(np.matmul(matrix, np.linalg.inv(matrix)))