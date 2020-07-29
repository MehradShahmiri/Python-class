import numpy as np
import matplotlib.pyplot as plt
#1
x=10
#2
y=pow(x,2)
#3
q=60
#4
s= np.sin(q)
c= np.cos(q)
#radians
#5
meshPoints = np.linspace(-1,1,500)
#6
meshPoints[53]
#7
plt.plot(meshPoints,np.sin(2*np.pi*meshPoints))
plt.show()
