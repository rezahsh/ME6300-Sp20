#!/usr/bin/env python3.5

import numpy as np
import matplotlib.pyplot as plt

utop=41.54           # velocity of top stream
ubot=22.4            # velocity of bottom stream
dy=0.015;            # momentum thickness (estimate)
U0=utop-ubot         # Reference velocity
freq=0.017*U0/dy     # frequency from Strouhal number = 0.017 
ampu=0.1             # u dir. sine wave ampiltude
ampv=0.2             # v dir. sine wave ampiltude
ampw=0.1             # w dir. sine wave ampiltude
tend=0.3             # end time
dt=0.001             # time increment


ampu=ampu*U0
ampv=ampv*U0
ampw=ampw*U0
av=2*np.pi*freq

# top stream
f=open('tableutop.dat','w')
print("(",file=f)
for t in np.arange(0,tend+dt,dt):
        sum=np.sin(av*t)+np.sin(av*t*2)+np.sin(av*t/2)+np.sin(av*t*4)+np.sin(av*t/4)
        print("(","{:5.3f}".format(t),"(",ampu*sum+utop," ",ampv*sum," ",ampw*sum,"))", file=f)
print(")",file=f)

# bottom stream
f=open('tableubot.dat','w')
print("(",file=f)
for t in np.arange(0,tend+dt,dt):
        sum=np.sin(av*t)+np.sin(av*t*2)+np.sin(av*t/2)+np.sin(av*t*4)+np.sin(av*t/4)
        print("(","{:5.3f}".format(t),"(",ampu*sum+ubot," ",ampv*sum," ",ampw*sum,"))", file=f)
print(")",file=f)

print('... wrote tableutop.dat and tableubot.dat ...')
