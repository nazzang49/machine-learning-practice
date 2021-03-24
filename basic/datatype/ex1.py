import numpy as np
from sklearn import preprocessing

# numerical data
feature = np.array([
    [-100, 50000000],
    [-10, 540],
    [-200, 360]
])
print(feature.shape)

# MinMaxScaler for NN
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
# change scale of feature (each columns)
print(scaler.fit_transform(feature))

# StandardScaler for general => mean = 0 / std = 1
scaler = preprocessing.StandardScaler()
print(scaler.fit_transform(feature))

# RobustScaler for many outlier => use median / IQR
scaler = preprocessing.RobustScaler()
print(scaler.fit_transform(feature))