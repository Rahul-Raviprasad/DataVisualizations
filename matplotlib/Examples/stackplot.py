import matplotlib.pyplot as plt

x = [1,2,6,7]
y1 = [3,4,5,23]
y2 = [4,6,7,2]
y3 = [20,3,10,2]

# Empty list are used because we really dont want to draw any plots. We simply need them for legends
# this is because stackplot doesn't support how to draw a legend
plt.plot([],[], label='y1', linewidth=5, color='k')
plt.plot([],[], label='y2', linewidth=5, color='r')
plt.plot([],[], label='y3', linewidth=5, color='b')

plt.stackplot(x, y1,y2,y3, colors=['k', 'r', 'b'])

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.title('Stack Plot')

plt.show()
