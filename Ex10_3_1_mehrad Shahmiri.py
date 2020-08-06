import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
f = (np.exp((-x)/10))*np.sin(np.pi*x)
g = x*np.exp(-x/3)    
plt.figure()
plt.plot(x, f,label='f')
plt.plot(x, g,label='g')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
