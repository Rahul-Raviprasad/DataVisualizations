import matplotlib.pyplot as plt

x = [1,2,6,7,23,12,22,3]
y = [3,4,5,23,5,6,7,12]

# marker generally is a dot, to say show a star you need to use marker='*', s is for size
plt.scatter(x, y, color='k', marker='*', s=500)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Scatter Plot')

plt.show()
