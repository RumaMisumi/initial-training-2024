import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,2,100)
y=2**x
y_seikin=2**-x
plt.plot(x,y,color="blue")
plt.plot(x,y_seikin,color="red")
plt.show()