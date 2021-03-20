import numpy as np

# random
print(np.random.rand(3))
print(np.random.rand(2, 3))
# 0 - 11 => 1 ~ 10 range
print(np.random.randint(0, 11, 3))

# custom random
# 0.0 => mean / 1.0 => std
print(np.random.normal(0.0, 1.0, 3))
# 0.0 => mean / 1.0 => scale
print(np.random.logistic(0.0, 1.0, 3))
# standard_normal => mean = 0.0 / std = 1.0
print(np.random.standard_normal((2, 3)))

# zero
print(np.zeros((2, 2), dtype='int64'))

# shuffle
random_matrix = np.random.randn(5)
np.random.shuffle(random_matrix)
print(random_matrix)

# permutation => totally new array
print(np.random.permutation(random_matrix))