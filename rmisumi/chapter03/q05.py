import numpy as np
for i in range(0, 361):
    sin_h= np.sin(np.radians(i))
    cos_h = np.cos(np.radians(i))
    tan_h= np.tan(np.radians(i)) 
    print(i,sin_h,cos_h,tan_h)
#弧度法（ラジアン）であらわすために、0-360度をnp.radiansを用いて、ラジアンであらわしてから、np.sinなどの関数を用いて計算する。