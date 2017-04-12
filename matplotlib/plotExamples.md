## Pyplot Examples

## General approach


#### Code explanation
Format string 3rd argument :'ro': The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is ‘b-‘, which is a solid blue line

The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.

```python
import matplotlib.pyplot as plt

# for the plot method to draw a 2 Axis graph. we generally pass 3 arguments x, y, 'format string'.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

```

## references
1. Tutorial: https://matplotlib.org/users/pyplot_tutorial.html
2. Documentation: https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
