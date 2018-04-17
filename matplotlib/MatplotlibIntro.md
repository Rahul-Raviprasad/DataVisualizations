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

## Histograms
Histograms are used to show distributions. Like say a population distribution. How many people are there between the age group of 20-30?