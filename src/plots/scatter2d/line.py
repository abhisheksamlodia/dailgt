import sys
import matplotlib.pyplot as plt
plt.rcParams.update({"text.usetex" : True,
                     'text.latex.preamble' : r'\usepackage{amsmath}',
                     "font.family" : "Times New Roman",
                     "xtick.direction" : "in", 
                     "ytick.direction" : "in",
                     "xtick.top" : True,
                     "ytick.right" : True,
                     "legend.edgecolor" : "black",
                     "figure.figsize" : [10,8],
                     'legend.fancybox': True,
                     'legend.labelspacing': 0.7,
                     'legend.fontsize': 'large',
                     'legend.framealpha': 1.0})
from matplotlib.ticker import ScalarFormatter
y_formatter = ScalarFormatter(useOffset=False)
import seaborn as sns
sns.set_context("talk")

def plot(xdata,  ydata, yerror, xmin, xmax, labels, title, labelx, labely, filename):
    """
    args:
        xdata (list of 1-dimensional numpy array of floats) -> list of multiple datasets for x-axis
        ydata (list of 1-dimensional numpy array of floats) -> list of multiple datasets for y-axis
        yerror (list of 1-dimensional numpy array of floats) -> list of multiple datasets for y-errorbars
        xmin (float or int) -> minimum value of the x-range
        xmax (float or int) -> maximum value of the y-range
        labels (list of strings) -> legend name for each dataset in the list
        title (string) -> title for the plot
        labelx (string) -> label name for x-axis
        labely (string) -> label name for y-axis
        filename (str) -> filename to save the plots - needs full path
    returns:
        plots the data and shows it on the screen
        plots the data and saves it as well 
    """
    if (len(xdata) == len(ydata)) and (len(xdata) == len(labels)):
        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(y_formatter)
        
        if len(yerror) == 0:
            for i in range(len(xdata)):
                x, y = xdata[i], ydata[i]
                ax.plot(x, y, "--o", label = labels[i])
        elif len(yerror) == len(xdata):
            for i in range(len(xdata)):
                x, y = xdata[i], ydata[i]
                ax.errorbar(x, y, "--o", label = labels[i])
        else:
            print("Error! mismatch in the number of datasets and number of errorbar dataset")
            sys.exit(1)

        plt.xlabel(labelx, fontsize=32)
        plt.ylabel(labely, fontsize=32)
        plt.legend(fontsize=22)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)
        plt.title(title, fontsize=32)
        plt.xlim(xmin,xmax)
        plt.tight_layout()
        plt.savefig(filename)
        plt.show()

        return None
    
    else:
        print("Error! mismatch in the number of datasets and number of labels")
        sys.exit(1)