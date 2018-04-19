import matplotlib.pyplot as plt

slices = [1,2,6,7]
fruits = ['bananas', 'apples', 'oranges', 'watermelons']
plt.pie(slices, labels=fruits, colors=['k', 'r', 'b', 'g'])
plt.title('Fruits')
plt.show()
