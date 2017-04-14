from sklearn.datasets import load_iris
iris = load_iris()

iris.keys()
# output : dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
n_samples, n_features = iris.data.shape

print(n_samples, n_features)
# output: 150 4

#We can there are some 150 samples which have 5 different features each.
#The iris is a data set which comes with sklearn to play around with.
#iris.data is an array with 150 samples.

print(len(iris.data))
# output: 150
print(iris.data[0])
# output: [ 5.1  3.5  1.4  0.2]

print(iris.target)

# output:
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2]

print(iris.target_names)

# output: ['setosa' 'versicolor' 'virginica']

import numpy as np
import matplotlib.pyplot as plt

x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target, cmap=plt.get_cmap('RdYlBu', 3))

plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.clim(-0.5, 2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

plt.show()
print('end')
