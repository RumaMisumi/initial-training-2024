import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,100)
y=x**3-6*x**2+9*x-3
plt.plot(x,y,label="y=x**3-6*x**2+9*x-3",color="blue")
plt.show()
y_hikakin=(x+2)**3-6*(x+2)**2+9*(x+2)-3+2
plt.plot(x,y_hikakin,label="y=x**3-6*x**2+9*x-3",color="red")
plt.show()