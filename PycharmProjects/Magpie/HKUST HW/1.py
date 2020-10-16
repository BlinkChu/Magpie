import matplotlib.pyplot as plt
from math import cos, sin, pi
import numpy as np
gap_1 = 5000
gap_2 = 70
y = np.linspace(-3,3,gap_2)
yy = np.linspace(-7,7,gap_1)

# cor_fun = np.sin(2*pi*x)*np.sin(2*pi*x+)
inter = 0

def ori_fun(y):
    if y>3 or y<-3:
        return 0
    else:
        return sin(2*pi*y)
result = []
for i in yy:
    value = 0
    for j in y:
        value += ori_fun(j)*ori_fun(j+i)*(6/gap_2)
    result.append(value)

plt.plot(yy ,result)
plt.show()
