import numpy as np
import matplotlib.pyplot as plt

h0=10
t = np.linspace(0, 2, 1000, endpoint=True)
s = 9.81*t**2/2
h = h0-s

plt.plot(t,s)
plt.plot(t,h)

plt.show()