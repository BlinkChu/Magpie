import matplotlib.pyplot as plt
from math import cos, sin, pi, exp, sqrt
import numpy as np

def normal(x,sigma):

    y = (1/(sqrt(2*pi*((sigma)**2)))) * exp(-(x**2)/(2*(sigma)**2))
    return y

def ori_fun(y):
    if y>3 or y<-3:
        return 0
    else:
        return sin(2*pi*y)+sin(20*pi*y)

gap_1 = 5000
gap_2 = 100
y = np.linspace(-3,3,gap_2)
yy = np.linspace(-7,7,gap_1)
result = []

sigma = 0.2
for i in yy:
    value = 0
    for j in y:
        value += ori_fun(j)*normal(i-j,sigma)*(6/gap_2)
    result.append(value)

plt.plot(yy ,result)
plt.show()