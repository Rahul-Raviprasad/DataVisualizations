import matplotlib.pyplot as plt

population_ages = [2,34,54,34,5,6,67,8,89,34,25,24,23]

ids = [x for x in range(len(population_ages))]

plt.bar(ids, population_ages)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Histogram')

plt.show()
