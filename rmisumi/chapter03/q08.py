import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.01,5,100)
y=np.log(x)
y_masuo=np.log2(x)
y_seikin=np.log10(x)
plt.plot(x,y,color="blue")
plt.plot(x,y_masuo,color="red")
plt.plot(x,y_seikin,color="green")
plt.show()