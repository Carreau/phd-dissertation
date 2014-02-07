from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy
import numpy as np
from numpy import *
from mpl_toolkits.mplot3d import Axes3D

import pyximport
pyximport.install()
from d2d import model

import matplotlib.pyplot as plt

xtest = 45
ytest = xtest
xc = xtest //2
yc = ytest //2
rc = xtest*1/5
noise = 0.3
delta = rc/10.0
sizetest = (xtest,ytest)

#imshow(model(xc,yc,rc, delta,sizetest),cmap='gray', interpolation='nearest')

fig, (ax,ax2,ax3) = plt.subplots(ncols=3)

# normalize colorbar
ax.imshow(model(xc,yc,rc, delta,sizetest),cmap='gray')
data=  model(xc,yc,rc, delta,sizetest )+noise*np.random.normal(size=sizetest)
ax2.imshow(data, cmap='gray')
data2=  model(xc,yc,rc, delta,sizetest, k=.5 )+noise*np.random.normal(size=sizetest)
ax3.imshow(data2, cmap='gray')

fig.savefig('modl-2d-doublet.png', transparent=True, bbox_inches='tight');

def err(data,model):
    return (data*model).sum()

xyerrm = zeros_like(data)
from IPython.display import clear_output
for i in range(xtest):
#    clear_output()
    #print '\r\bi=',i,
    print '\ni=',i,
    for j in range(ytest):
        print '.',
        xyerrm[i,j] = err(data,model(i,j,rc,delta, sizetest))

pstring = 'noise-'#{noise}'.format(**locals())
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1);
ax2 = fig.add_subplot(2,2,2, projection='3d');
ax3 = fig.add_subplot(2,2,3);
ax4 = fig.add_subplot(2,2,4, projection='3d');
vmin = xyerrm.min()
vmax = xyerrm.max()
val = ax1.imshow((xyerrm-vmin)/(vmax-vmin), interpolation='nearest',cmap='jet')
#plt.colorbar(val )
ax1.set_title('corelation function of position')
ax1.set_xlabel('x-position of model  center')
ax1.set_ylabel('y-position of model  center')

X = np.arange(0, shape(xyerrm)[0])
Y = np.arange(0, shape(xyerrm)[1])
X, Y = np.meshgrid(X, Y)
surf = ax2.plot_surface(X, Y, xyerrm, rstride=1, cstride=1, cmap='jet', linewidth=0, antialiased=False)


xrerrm = zeros_like(data)

for i in range(xtest):
    print '\r\bi=',i,
    for j in range(0,ytest):
        print '.',
        xrerrm[j,i] = err(data,model(i,yc,j,delta, sizetest))


lerrm = (xrerrm)
vmin = lerrm.min()
vmax = lerrm.max()
val = ax3.imshow((lerrm-vmin)/(vmax-vmin), interpolation=None, cmap='jet', )
#plt.colorbar(val)
ax3.set_title('corelation function of position')
ax3.set_xlabel('x-position of model  center')
ax3.set_ylabel('radius of model')




X = np.arange(0, shape(xrerrm)[0])
Y = np.arange(0, shape(xrerrm)[1])
X, Y = np.meshgrid(X, Y)
surf = ax4.plot_surface(X, Y, xrerrm, rstride=1, cstride=1, cmap='jet', linewidth=0, antialiased=False)

fig.savefig('corrfun-{pstring}.png'.format(pstring=pstring), transparent=True, bbox_inches='tight')







