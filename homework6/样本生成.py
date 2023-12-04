import numpy
import matplotlib.pyplot

mu, sigma = 0, 0.1 # 均值和标准差
s = numpy.random.normal(mu, sigma, 100)
count, bins, ignored = matplotlib.pyplot.hist(s, 10, density=True)
matplotlib.pyplot.show()

