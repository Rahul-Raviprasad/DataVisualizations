from sklearn.datasets import load_iris
iris = load_iris()

iris.keys() # checkout all the things the iris dataset has.
# output : dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
n_samples, n_features = iris.data.shape

print(n_samples, n_features)
# output: 150 4

# The features that we see in the iris example, could be say length of petals, colour, presence of a patterns or not width of the petal
# size of leaves etc. These features are in a dimension based on which we can classify or identify a flower to be of particular family.

# Features in iris dataset
# 1. Sepal length in cm
# 2. Sepal width in cm
# 3. petal length in cm
# 4. petal width in cm

# Target classes to predict
# 1. Iris Setosa
# 2. Iris Versicolor
# 3. Iris Virginica


# We can there are some 150 samples which have 5 different features each.
# The iris is a data set which comes with sklearn to play around with.
# iris.data is an array with 150 samples.

print(len(iris.data))
# output: 150

# printing the first row of our data, we can see the different lengths/ widths of the petals and sepals in the output
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
