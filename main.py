import matplotlib.pyplot as plt
import numpy as np

X, Y = np.loadtxt('sample-bar.txt', delimiter=' ', unpack=True)

plt.bar(X, Y)
plt.title('Bar Graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


