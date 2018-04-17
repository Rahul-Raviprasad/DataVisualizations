import matplotlib.pyplot as plt

x = [2,4,6]
y = [1,3,7]

x2 = [1,3,5]
y2 = [12,15,17]

plt.bar(x,y, label='Bar1', color='r')
plt.bar(x2,y2, label='Bar2', color='b')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Bar Chart')

plt.legend()

plt.show()
