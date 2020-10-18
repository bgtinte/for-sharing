# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:00:03 2020

@author: Bienica Yzabelle
"""

import numpy as np
import matplotlib.pyplot as plt
N = 1200
M= 1200
x = np.linspace(-10,10,num = N)
y = x
X,Y = np.meshgrid(x,y)
Rd, Gn, Bl = np.ones((N,N)), np.ones((N,N)), np.ones((N,N))
#draw colored circles
Rt, Rc, deg = 2, 3, 30
Rn = Rc-0.5
xt, yt = Rt*np.cos(deg*np.pi/180), Rt*np.sin(deg*np.pi/180)
R = np.sqrt((X)**2 + (Y+Rt)**2)
Rd[np.where((R<Rc) & (R>Rn))]=0
Gn[np.where((R<Rc) & (R>Rn))]=0
Bl[np.where((R<Rc) & (R>Rn))]=0
R = np.sqrt((X-2*xt)**2 + (Y-yt)**2)
Rd[np.where((R<Rc) & (R>Rn))]=0
Bl[np.where((R<Rc) & (R>Rn))]=0
R = np.sqrt((X+2*xt)**2 + (Y-yt)**2)
Bl[np.where((R<Rc) & (R>Rn))]=0
R = np.sqrt((X+4*xt)**2 + (Y+Rt)**2)
Rd[np.where((R<Rc) & (R>Rn))]=0
Gn[np.where((R<Rc) & (R>Rn))]=0
R = np.sqrt((X-4*xt)**2 + (Y+Rt)**2)
Gn[np.where((R<Rc) & (R>Rn))]=0
Bl[np.where((R<Rc) & (R>Rn))]=0
I = np.zeros((N,N,3))
I[...,0] = Rd
I[...,1] = Gn
I[...,2] = Bl
fig = plt.figure()
plt.imshow(I)

rgbim = I*255
img = rgbim.astype(np.uint8)
plt.imsave("coloredcircle.jpg",img)
plt.imsave("coloredcircle.bmp",img)
plt.imsave("coloredcircle.png",img)
plt.imsave("coloredcircle.tiff",img)
