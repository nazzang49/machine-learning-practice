import numpy as np

# dot => dot product 내적곱
# matmul => matrix product 행렬곱
# https://m.blog.naver.com/PostView.nhn?blogId=cjh226&logNo=221356884894&proxyReferer=https:%2F%2Fwww.google.com%2F
a = np.asarray([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
b = np.asarray([1, 2, 3, 4])

print(a.shape)
print(b.shape)
print(a.ndim)
print(b.ndim)
print(np.dot(a, b))

# 2 => lowest
# 10 => largest
# 100 => element size
print(np.random.randint(2, 10, 100).reshape(5, 20))
# 2 => row
# 10 => col
# rand => 0 - 1
print(np.random.rand(2, 10))

