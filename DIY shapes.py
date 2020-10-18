# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:45:05 2020

@author: Bienica Yzabelle
"""
#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal,stats
N = 200                         #pixels, in this case, the image is NxN
x = np.linspace(-2,2,num = N)   # -2 to 2 cm as global coordinates
y = x                           # square global and image coordinates
X,Y = np.meshgrid(x,y)          #X and Y for corresponding image coordinates

#%% Formulas for graphs and images

# CIRCULAR APERTURE
# this was the example in uvle
circ = np.sqrt(X**2 + Y**2)
circle = np.zeros(np.shape(circ))
circle[np.where(circ<0.5)] = 1

''' SINUSOID
The sine equation shifted to rise by 1 unit, and rescaled to 1/2, 
so the amplitude is [0,1].
The frequency w=4 is specified in the equation, as well. '''
sine = (1/2)*(np.sin(4*np.pi*X) + 1)

''' VERTICAL GRATINGS
a square wave appears like a periodic grating when viewed along the z axis,
thus my choice of equation'''
grating = signal.square(5*np.pi*X)

'''square aperture
We initialize a square image first.
The x and y coordinates are specified as boundaries. 
Within these, we set the pixel value to 1 (white). 
This is now the square aperture.'''
square = np.zeros(X.shape)
square[((-1 < X) & (X < 1))&((-1<Y)&(Y<1))]=1

'''ANNULUS
a matrix of zeros is initialized. The white value is limited from R=1.75 to R=2'''
annulus = np.zeros(X.shape)
annulus[np.where((circ<2) &(circ>1.75))] = 1

'''GRADED TRANSMITTANCE
We do a 2D normal distribution, but limit this result only to R<1.75.
The rest remains black or zero.'''
dist = stats.norm.pdf(circ)
aperture = np.zeros(X.shape)
aperture[np.where(circ<1.75)] = 1
gauss = aperture*dist

#%% image production

#display as an 2D image
R = gauss                         # specify the image you want to see
plt.imshow(R, cmap = 'Greys_r')#    #show the image for checking 

#display as a 3D surface in Cartesian coordinates
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_surface(X,Y,R)

#save image as different file types
#I have to specify a grey colormap or white becomes yellow, and black, purple
# plt.imsave("gauss.jpg",R,cmap='Greys_r')
# plt.imsave("gauss.bmp",R,cmap='Greys_r')
# plt.imsave("gauss.png",R,cmap='Greys_r')
# plt.imsave("gauss.tiff",R,cmap='Greys_r')