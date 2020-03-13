# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:20:22 2020

@author: anjan
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 



I0 = 1 #mean intensity of light source
I1 = 0.3 #constant of noise 
elements = 11 #number of laser outlets
attempts = 100000 # number of trials 
W = 0.01 #width of laser source
multiplier = [] #analogous to the multiplier in the experiment
chi = []
s = 10/math.sqrt(attempts)

object = [0,0,0,1,1,1,1,1,0,0,0] #The object exposed to wave intensities

for d in range(elements): 
    multiplier.append(0)

for j in range(elements): 
    chi.append(0)


for k in range(attempts):
    
    pos = 0
    position = []
    bucket = []
    wave_x=[]
    wave_y=[]

    wave = np.random.poisson(10,elements)   #laser source with noise

    randomizer = np.random.uniform(0, 1, elements)

    wave_ran = np.multiply(wave, randomizer)

    randomized_wave = np.around(wave_ran)

    for k in range(elements):
    
        q = np.random.binomial(randomized_wave[k], 0.999)
        wave_x.append(q)
        wave_y.append(randomized_wave[k]-q)
    
    bucket = np.multiply(object, wave_y) #interaction of laser wave intensities and object
    
    j = sum(bucket) #summing up the resultant array 

    multiplied = j*np.array(wave_x) #multiplying the sum of the interaction array with the original wave intensities 
     
    multiplier += multiplied #summing up consecutive trials
 

avg_multiplier = np.array(multiplier) #average of resulting intensity at each position
bac_multiplier = [(x) for x in avg_multiplier]

print(bac_multiplier)

#x = np.arange(0, 11, 1)
#y= np.piecewise(x, [x < 3, 3<=x], [0,1])
#z= np.piecewise(x, [x <= 7, x>7], [1,0])
#w=y*z    

#def tophat(x, a, b):
 #   return a*(w + b) 

#popt, pcov = curve_fit(tophat, x, bac_multiplier)
#popt

#plt.plot(tophat(x, *popt), 'r-')

plt.plot(bac_multiplier, "bo")


plt.ylabel("Ghost Image")
plt.xlabel("Points")
plt.show()

print(wave_x)
print(wave_y)
 

#for t in range(elements): 
 #       chi[t] = ((bac_multiplier[t]-object[t])*(bac_multiplier[t]-object[t]))/1
        
#chi_squared = sum(chi)

#print(chi_squared)

#print (wave)
#print(j)
