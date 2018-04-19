## Matplotlib

It is a very popular python library.

## Installation
on terminal /command prompt type: pip install matplotlib
you might need to change to pip3 if python 3 is not default.

## Importing matplotlib

Almost always we will be using pyplot, to draw a simple line chart, just provide the points, it will automatically add line from one to next.

```python
import matplotlib.pyplot as plt

# in plot method we generally plot Xs and Ys. These can be many (x,y) points
plt.plot([3,4,6],[5,6,2])

#this makes the actual plot to show
plt.show()

```

## Basic Features
We can simply call many of methods like xlabel(), ylabel(), title(), legend()-requires plots with labels etc on the plt as shown below.

```python
import matplotlib.pyplot as plt

x = [3,4,6]
y = [3,5,7]

x2 = [3,4,6]
y2 = [12,15,17]

# In plot method we generally plot Xs and Ys. These can be many (x,y) points
plt.plot(x,y, label='firstLine') # providing a label helps in identifying a line plot. this is later used by legend() method
plt.plot(x2,y2, label='secondLine')

# The labels that will be shown below and next to x and y axis
plt.xlabel('this is the xlabel')
plt.ylabel('cool y label')

#title shown at top, \n is used to show any subtitle if you need.
plt.title('title at the top\n this is a subtitle') #

# Legends: this simply adds legends based on the labels you have given to your plots.
plt.legend()

#this makes the actual plot to show
plt.show()

```

## Draw Bar chart
They are used mostly for comparison or to see the absolute value.

```python
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

```
another example
```python
import matplotlib.pyplot as plt

population_ages = [2,34,54,34,5,6,67,8,89,34,25,24,23]

ids = [x for x in range(len(population_ages))]

plt.bar(ids, population_ages)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Histogram')

plt.show()


```

## Histograms
Histograms are used to show distributions. Like say a population distribution. How many people are there between the age group of 20-30?


```python
import matplotlib.pyplot as plt

population_ages = [2,34,54,34,5,6,67,8,89,34,25,24,23]

bins = [0,30,60,90,120]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Histogram')

plt.show()

```

## Scatter plots

```python
import matplotlib.pyplot as plt

x = [1,2,6,7,23,12,22,3]
y = [3,4,5,23,5,6,7,12]

# marker generally is a dot, to say show a star you need to use marker='*', s is for size
plt.scatter(x, y, color='k', marker='*', s=500)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Scatter Plot')

plt.show()

```


## Stackplot

```python
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

```

## Pie Chart
```python
import matplotlib.pyplot as plt

slices = [1,2,6,7]
fruits = ['bananas', 'apples', 'oranges', 'watermelons']
plt.pie(slices, labels=fruits, colors=['k', 'r', 'b', 'g'])
plt.title('Fruits')
plt.show()

```
