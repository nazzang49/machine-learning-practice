from sklearn.datasets import make_regression, make_classification, make_blobs

# make dataset for Linear Regression (supervised)
features, target, coefficients = make_regression(n_samples=100,
                                                 n_features=3,
                                                 n_informative=3,
                                                 # prediction value => actual number
                                                 n_targets=1,
                                                 noise=0.0,
                                                 coef=True,
                                                 random_state=1)

# 100 row / 3 col
print(features)
print(features.shape)
print("==============================")
# 100 row
print(target)
print(target.shape)
print("==============================")
print(coefficients)

# make dataset for Classification (supervised)
features, target = make_classification(n_samples=100,
                                       n_features=3,
                                       n_informative=3,
                                       n_redundant=0,
                                       # prediction value => ex) 0 or 1
                                       n_classes=2,
                                       # class ratio
                                       weights=[.25, .75],
                                       random_state=1)

# 100 row / 3 col
print(features)
print(features.shape)
print("==============================")
# 100 row
print(target)
print(target.shape)
print("==============================")

# make dataset for Clustering (non-supervised)
features, target = make_blobs(n_samples=100,
                              n_features=3,
                              centers=3,
                              cluster_std=0.5,
                              shuffle=True,
                              random_state=1)

# 100 row / 3 col
print(features)
print(features.shape)
print("==============================")
# 100 row
print(target)
print(target.shape)
print("==============================")

import matplotlib.pyplot as plt

# clustering visualization => scatter graph
plt.scatter(features[:, 0], features[:, 1], c=target)
plt.show()