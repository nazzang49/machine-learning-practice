import numpy as np
from scipy import sparse

# 2-dim matrix
matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])
print(matrix)
print(type(matrix))

# sparse matrix => can reduce the large cost of calculation
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)
print(type(matrix_sparse))

# sparse => dense
print(matrix_sparse.todense())
print(matrix_sparse.toarray())

# check data => array
print(type(matrix_sparse.data))
for value in matrix_sparse.data:
    print("value : {}".format(value))

# check index and value
for i, (b, e) in enumerate(zip(matrix_sparse.indptr, matrix_sparse.indptr[1:])):
    for idx in range(b, e):
        j = matrix_sparse.indices[idx]
        d = matrix_sparse.data[idx]
        print('({}, {}) = {}'.format(i, j, d))

