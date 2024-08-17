import matplotlib
import numpy as np
matplotlib.use('TkAgg')  # You can also try 'Qt5Agg' or 'Agg'
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 20)
y = x

plt.plot(x, y)
plt.show()
