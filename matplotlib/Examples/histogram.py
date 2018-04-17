import matplotlib.pyplot as plt

population_ages = [2,34,54,34,5,6,67,8,89,34,25,24,23]

bins = [0,30,60,90,120]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Histogram')

plt.show()
