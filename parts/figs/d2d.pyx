import cython
import numpy as np

def model(int x0,int y0,int r0, float delta,size , k=0):
    zer = np.zeros(size)
    r=r0
    g = lambda d: np.exp((-(d-r)**2)/delta)+(0 if d<r-delta/2 else ((d-r+delta/2)*k/delta if d < r+delta/2 else k))
    dd= lambda x,y: np.sqrt(x**2+y**2)

    for i in range(size[0]):
        for j in range(size[1]):
            zer[i,j] = g(dd(i-x0,j-y0))
    return zer
