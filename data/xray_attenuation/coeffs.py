#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot

import csv

cdata = []
with open('coeffs.csv', 'rb') as coeffs_file:
    creader = csv.DictReader(coeffs_file, skipinitialspace = True)
    for row in creader:
        cdata.append(row)

cdata2 = []
with open('coeffs2.csv', 'rb') as coeffs2_file:
    c2reader = csv.DictReader(coeffs2_file, skipinitialspace = True)
    for row in c2reader:
        cdata2.append(row)

print cdata2[0].keys()
gdata = []
with open('../general/phys_props.csv', 'rb') as general_file:
    greader = csv.DictReader(general_file, skipinitialspace = True)
    for row in greader:
        gdata.append(row)

for r in xrange(len(gdata)):
    if gdata[r]['Property'] == 'Density':
        dens = gdata[r]

plots = ['Iron', 'Water', 'Lead', 'Uranium', 'Aluminium']

xrng = []
yplot = {}

for p in plots:
    yplot[p] = []

for x in xrange(len(cdata)):
    xrng.append(float(cdata[x]['MeV']))
    for p in plots:
        yplot[p].append(float(cdata[x][p]))

xrng2 = []
yplot2 = {}
for p in plots:
    yplot2[p] = []
for x in xrange(len(cdata2)):
    xrng2.append(float(cdata2[x]['MeV']))
    for p in plots:
        yplot2[p].append(float(cdata2[x][p]))

for p in plots:
    #yplot[p] = np.exp(-0.1 * (np.array(yplot[p]) * float(dens[p]) / 1000.0))    # To convert answer for 1mm of target
    #yplot[p] = -np.log(0.01) / ((np.array(yplot[p]) * float(dens[p]) / 1000.0))    # cm of material to get 1% transmission
    yplot[p] = -0.1 * np.log(0.01) / ((np.array(yplot[p])))    # Mass of material to get 1% transmission for 1m^2 slab
    yplot2[p] = -0.1 * np.log(0.01) / ((np.array(yplot2[p])))    # Mass of material to get 1% transmission for 1m^2 slab


    pyplot.semilogx(xrng, yplot[p], '-+', label=p)
    pyplot.semilogx(xrng2, yplot2[p], '-+', label='NIST '+p)

#pyplot.semilogx(xrng, yplot[plots[2]], '-+b', label=plots[2])
#pyplot.semilogx(xrng, yplot[plots[3]], '-+c', label=plots[3])
#pyplot.semilogx(xrng, yplot[plots[4]], '-+k', label=plots[4])

pyplot.xlabel('X-ray energy (MeV)')
#pyplot.ylabel('cm$^{-1}$')
pyplot.ylabel('Mass of material for 1% transmission ($kg/m^{2}$)')
#pyplot.ylabel('Thickness of material for 1% transmission (cm)')
#pyplot.ylabel('Fraction Transmitted (1mm of material)')
pyplot.legend()
pyplot.show()

    
                
