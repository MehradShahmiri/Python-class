import numpy as np
import matplotlib.pyplot as plt

#3.2
z=[0.8,1,1.2]
for r0 in z:
    q=np.linspace(0, 2*np.pi, 1000)
    r = r0 + np.cos(q)
    x = r*np.cos(q)
    y = r*np.sin(q)
    plt.polar(q,x,label='x')
    plt.polar(q,y,label='y')
    plt.polar(q,r,label='r')
    plt.title(r0)
    plt.legend()
    plt.show()

