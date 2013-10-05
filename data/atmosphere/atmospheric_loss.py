#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot
from scipy import constants

import csv

cdata = []
with open('../xray_attenuation/coeffs.csv', 'rb') as coeffs_file:
    creader = csv.DictReader(coeffs_file, skipinitialspace = True)
    for row in creader:
        cdata.append(row)

gdata = []
with open('../general/phys_props.csv', 'rb') as general_file:
    greader = csv.DictReader(general_file, skipinitialspace = True)
    for row in greader:
        gdata.append(row)

for r in xrange(len(gdata)):
    if gdata[r]['Property'] == 'Density':
        dens = gdata[r]
    if gdata[r]['Property'] == 'Mass':
        mass = gdata[r]


adata = []
with open('atmosphere.csv', 'rb') as atmos_file:
    areader = csv.DictReader(atmos_file, skipinitialspace = True)
    for row in areader:
        adata.append(row)

print 'Max altitude', adata[-1]['Altitude']

d = 2.0 * float(adata[0]['N2']) * float(mass['Nitrogen']) + 2.0*float(adata[0]['O2']) * float(mass['Oxygen']) + float(adata[0]['Ar']) * float(mass['Argon'])

d /= constants.Avogadro

print 'Density at ground level', d*1000

absorp = np.zeros((len(cdata), len(adata)))
for alt in xrange(len(adata)):
    for mev in xrange(len(cdata)):
        absorp[mev, alt] = ((2.0 * float(adata[alt]['N2']) * float(mass['Nitrogen']) * float(cdata[mev]['Nitrogen'])) +
                            (2.0 * float(adata[alt]['O2']) * float(mass['Oxygen']) * float(cdata[mev]['Oxygen'])) +
                            (float(adata[alt]['Ar']) * float(mass['Argon']) * float(cdata[mev]['Argon']))) / constants.Avogadro

dalt = float(adata[1]['Altitude']) - float(adata[0]['Altitude'])

res = np.zeros((len(cdata),))
res = 1.0 - res

alt_res = [10000.0, 20000.0, 30000.0, 40000.0, 60000.0]

res_res = {}

for alt in xrange(len(adata)-1, 0, -1):
    for mev in xrange(len(cdata)):
        
        res[mev] = res[mev] * (1.0 -  (dalt * 100 * float(absorp[mev,alt])))

    for x in alt_res:
        if abs(float(adata[alt]['Altitude']) - x) <= 1.0:
            res_res[str(x)] = res * 1.0

xrng = []
for x in xrange(len(cdata)):
    xrng.append(float(cdata[x]['MeV']))

for x in alt_res:
    pyplot.semilogx(xrng, res_res[str(x)], '-+', label=str(x/1000.0)+'km')

pyplot.xlabel('X-ray energy (MeV)')
pyplot.ylabel('Fraction transmitted')

pyplot.legend()
pyplot.show()

