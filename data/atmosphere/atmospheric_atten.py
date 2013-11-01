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

print 'Density at ground level (kg/m^3)', d*1000


absorp = np.zeros((len(cdata), len(adata))) # This ends up in cm^-1
dens = np.zeros((len(adata),))

for alt in xrange(len(adata)):
    for mev in xrange(len(cdata)):
        absorp[mev, alt] = ((2.0 * float(adata[alt]['N2']) * float(mass['Nitrogen']) * float(cdata[mev]['Nitrogen'])) +
                            (2.0 * float(adata[alt]['O2']) * float(mass['Oxygen']) * float(cdata[mev]['Oxygen'])) +
                            (float(adata[alt]['Ar']) * float(mass['Argon']) * float(cdata[mev]['Argon']))) / constants.Avogadro
        
    dens[alt] = ((2.0 * float(adata[alt]['N2']) * float(mass['Nitrogen'])) +
                 (2.0 * float(adata[alt]['O2']) * float(mass['Oxygen'])) +
                 (float(adata[alt]['Ar']) * float(mass['Argon']))) / constants.Avogadro

alt_xrng = []
for alt in xrange(len(adata)):
    alt_xrng.append(float(adata[alt]['Altitude']))

pyplot.semilogy(alt_xrng, 1000*dens, '-+')
pyplot.show()

xrng = []
for x in xrange(len(cdata)):
    xrng.append(float(cdata[x]['MeV'])*1e6)

#pyplot.semilogx(xrng, np.exp(-100* absorp[:,0]), '-+')  # Plot out absorption for 100cm of air at ground level
#pyplot.show()

dalt = float(adata[1]['Altitude']) - float(adata[0]['Altitude'])

res = np.zeros((len(cdata),))
res = 1.0 - res

alt_res = [20000, 30000, 40000, 60000]
#out=open('test_output.txt', 'w')
#print xrng[len(cdata)/2],'eV'
res_res = {}
for x in alt_res:
    res_res[str(x)] = np.zeros((len(cdata),)) - 1

for alt in xrange(len(adata)-1, 0, -1):
    for mev in xrange(len(cdata)):
        res[mev] = res[mev] * np.exp(-dalt * 100.0 * absorp[mev,alt])
        #if mev == len(cdata)/2:
        #    out.write(str(adata[alt]['Altitude'])+','+str(np.exp(-dalt * 100.0 * absorp[mev,alt]))+'\n')
        for x in alt_res:
            if x == float(adata[alt]['Altitude']):
                res_res[str(x)][mev] = res[mev]
#out.close()
for x in alt_res:
    pyplot.semilogx(xrng, res_res[str(x)], '-+', label=str(x))

pyplot.xlabel('X-ray energy (eV)')
pyplot.ylabel('Transmission')

pyplot.legend()
pyplot.show()

