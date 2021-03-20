import numpy as np

# min / max
matrix = np.array([[1, 2, 3],
                   [5, 4, 6],
                   [7, 10, 9],
                   [7, 10, 9]])
print(np.min(matrix))
print(np.max(matrix))
# axis = 0 => check row space
# axis = 1 => check col space
print(np.min(matrix, axis=0))
print(np.min(matrix, axis=1))

# avg / var / std
print(np.mean(matrix))
print(np.var(matrix))
print(np.std(matrix))
print(np.var(matrix, axis=0, dtype='float64'))
print(np.std(matrix, axis=1, dtype='float64'))
# ddof => not biased value
print(np.std(matrix, axis=1, ddof=1, dtype='float64'))