# normalization

import numpy as np
from sklearn.preprocessing import Normalizer

features = np.array([[0.5, 9.4],
                     [0.09, 1.4],
                     [0.1, 2.4],
                     [0.2, 3.4],
                     [0.3, 4.4],
                     [0.5, 5.4]])

print(features)
# L2 norm => euclidean
normalizer = Normalizer(norm="l2")
norm_features = normalizer.transform(features)
print(norm_features)

# L2 norm => taxi
normalizer = Normalizer(norm="l1")
norm_features = normalizer.transform(features)
print(norm_features)

# max => divide into max value
normalizer = Normalizer(norm="max")
norm_features = normalizer.transform(features)
print(norm_features)

