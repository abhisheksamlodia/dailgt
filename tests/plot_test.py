from plots.scatter2d import line
import numpy as np
data = np.loadtxt("tests/plot_test.txt")
xdata = [data[:,0]]
ydata = [data[:,2]]
yerrors = [data[:,3]]
#yerrors = []
xmin = 65
xmax = 4100
labels = ["data"]
title = "Jack-Knife Error Analysis"
xlabel = "Number of Jack-Knife Bins"
ylabel = "Jack-Knife Errorbar"
filename = "tests/plot_test.pdf"

line.plot(xdata, ydata, yerrors, xmin, xmax, labels, title, xlabel, ylabel, filename)
