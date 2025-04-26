# week8_plottask.py
# Week 8 Assignment: Create a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function h(x)=x3 in the range 0 to 10. 
# Author: Faolán Hamilton

# Import the modules I need
# Matplotlib will visualise the chart
import matplotlib.pyplot as plt
# Numpy will make the numbers easier to manipulate
import numpy as np

# Histogram plot data
# A - Data for the histogram is created using a random number generator through numpy
random_numbers = np.random.default_rng(12345)
# The range for the numbers is set, along with the value at 1000
rints = random_numbers.integers(low=0, high=10, size = 1000)

# Setting the seed is important, this ensures the random numbers are the same each time
np.random.seed (1)

# Setting the mean, standard deviation and value
x = rints
normal_distribution = np.random.normal(5, 2, 1000)

plt.hist(x, normal_distribution)

plt.show()

'''
# Setting the mean, standard deviation and value
normal_distribution = plot_range.normal(5, 2, 1000)
plt.hist(x_value, y_value, normal_distribution)

# Making it look nicer
plt.title("Histogram")
plt.xlabel("x_value")
plt.ylabel("h(x) = x3")
plt.legend()

# Print the plot, only need to say show() using the matplotlib module
plt.show()

# References
# A - https://numpy.org/doc/stable/reference/random/generator.html
# B - numpy.random.Generator.normal - https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html
# C- Intermediate Python - Chapter 1: Matplotlib - https://app.datacamp.com/learn/courses/intermediate-python
#----------End----------

data = np.random.normal(5, 2, 1000)

xmin = 0
xmax = 10

# Plotting the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='b')

plt.show()
'''
