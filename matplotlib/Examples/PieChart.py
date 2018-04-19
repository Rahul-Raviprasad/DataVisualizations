import matplotlib.pyplot as plt

slices = [1,2,6,7]
fruits = ['bananas', 'apples', 'oranges', 'watermelons']
plt.pie(slices,
        labels=fruits,
        colors=['k', 'r', 'b', 'g'],
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0))
plt.title('Fruits')
plt.show()
