# Myos Corp -- 2018
#
# This Project Just Show a Way to code Sin(), Cos(), and Exp()
# Using Boork Taylor's work on polynomial functions
#
# Created by Louis Lamalle and Quentin Dieppe
#

import matplotlib.pyplot as plt
from exponential import *
from cosinus import *
from sinus import *

def cos_graph():
    xlist = []
    ylist = []
    xplist = []
    yplist = []
    xelist = []
    yelist = []

    for i in range(628):
        xlist.append(cosinus(i * 0.01, 100))
        ylist.append(i * 0.01)
        xplist.append(sinus(i * 0.01, 100))
        yplist.append(i * 0.01)
        if i < 180 :
            xelist.append(exponential(i * 0.01, 100))
            yelist.append(i * 0.01)
    return (xlist, ylist, xplist, yplist, xelist, yelist)

if __name__ == '__main__' :
    xlist, ylist, xplist, yplist, xelist, yelist = cos_graph()
    plt.title("Graphical Representation Of  my_Exp(), my_Sin() and my_Cos()")
    pltcos = plt.plot(ylist, xlist, color="blue", label="my_cosinus")
    pltsin = plt.plot(yplist, xplist, color="red", label="my_sinus")
    pltexp = plt.plot(yelist, xelist, color="green", label="my_exponential")
    plt.legend(["my_cos()", "my_sin()", "my_exp()"])
    plt.show()
