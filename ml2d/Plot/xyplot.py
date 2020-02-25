#!/usr/bin/env python3.5

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from itertools import cycle

# input
time = 2000
graph1 = 'singleGraph1'
simFile = '../postProcessing/'+graph1+'/'+str(time)+'/line_U.xy'
sim = np.loadtxt(simFile).transpose()

# plot options
fontsize = 16
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : fontsize}
matplotlib.rc('font', **font)
points = ["o","d","s","v","^"]
pointcycler = cycle(points)

#
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111)

ls = '-'

markerstyle = next(pointcycler)
ax.plot(sim[1],sim[0],linestyle=ls,marker=markerstyle,markersize=6,markeredgecolor='none',label = "sss")

#markerstyle = next(pointcycler)
#ax.plot(dat[0],dat[1],linestyle=ls,marker=markerstyle,markersize=4,markeredgecolor='none',label = "measured")

#ax.plot([0,.6],[0,0],color='grey',ls='-.')

ax.set_xlabel("U (m/s)")
ax.set_ylabel("y (mm)")
ax.legend(loc='upper right',handlelength=4,numpoints=3,prop={'size':fontsize-1})
ax.grid('on')

#ax.legend(ncol=2, bbox_to_anchor=(0.1,1.17),handlelength=3, loc='upper left',prop={'size':fontsize-2})

width = 6.
aspect = 4./3.
fig.set_size_inches(aspect*width,width)

plt.show()
