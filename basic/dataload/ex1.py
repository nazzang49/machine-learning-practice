from sklearn import datasets

digits = datasets.load_digits()
print(digits)
# dict_keys(['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])
print(digits.keys())

# input data
features = digits.data
print(features)

# output data (label)
target = digits.target
print(target)

print("==============================")

# check first sample
print(features[0])

print(datasets.load_boston())
print(datasets.load_iris())



