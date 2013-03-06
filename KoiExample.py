#!/usr/bin/env python
"""
Illustrate colored contour plotting, using the KOI example.
"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

#
# Define range for x- and y-values and the step size delta
#
delta = 0.02
se = np.arange(0.0, 1.0+delta, delta)
p  = np.arange(0.0, 1.0+delta, delta)
#
# Create a meshgrid for Se (x-axis) and p (y-axis)
#
Se, P = np.meshgrid(se,p)
#
# Calculate z-values according to the KOI example
#
# Benefit = (1-P)*Sp*N
#            P is prevalence
#           Sp is spevificity
#            N is monetary benefit
#    Cost = P*(1.0-Se)*C
#           Se is sensitivity
#            C is monetary damage
#
#      ZZ = Benefit - Cost
Sp =   1.0
N  =  80.0
S  = 250.0
B  = (1.0-P)*Sp*N
C  = P*(1-Se)*S
#
ZZ = B-C
#
# now we rescale the z-values between 0 and 1 using Weibull function.
# scaling guarantees that the Weibull function has a value of 0.5 when 
# z is zero.
# A constant of abs(min(ZZ)) is added to the z-values to get positive figures
# of z. 
# Parameter estimation is done wiht DataGraph 
# for more details on DataGraph see www.visualdatatools.com/DataGraph/
# 
expo = ((ZZ+270)/277.55)**13.280823
ZZt  = 1-np.exp(-expo)
#
# Create a simple contpour plot
#
plt.figure()
#
# draw contour lines
#
CS = plt.contour(Se,P,ZZ)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Koi example')
plt.xlabel('Sensitivity')
plt.ylabel('Prevalence')
#
# fill with color [transformed values z (ZZt) are used] to guarantee that white
# color conincides with B=C, i.e the break even line
#
im = plt.imshow(ZZt, interpolation='bilinear', origin='lower',
        cmap=cm.PiYG,extent=(0,1,0,1))
plt.show()
