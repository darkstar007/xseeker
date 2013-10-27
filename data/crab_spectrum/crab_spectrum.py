#!/usr/bin/env python

import numpy as np

import matplotlib.pyplot as plt

# numbers from http://arxiv.org/pdf/0911.2412v1.pdf

N0 = 2.36e-10   # ph cm^-2 s^-1 MeV^-1

gamma = 1.97

ecutoff = 5.8e9 # eV

energies = 10.0 ** np.arange(8.0,11.1, 0.001)
#energies = np.arange(2.0,30, 0.01)

dn_de = N0 * ((energies / 1e9) ** -gamma)  * np.exp(- (energies / ecutoff))
#dn_de = N0 * (energies ** -gamma)

mpt = (energies[1:] + energies[:-1]) / 2.0

plt.loglog(mpt/1e6, ((dn_de[1:] + dn_de[:-1]) / 2.0)*(energies[1:] - energies[:-1])/1e6)
plt.xlabel('$\gamma$-ray energy ($MeV$)')
plt.ylabel('Flux ($photon/s/cm^{2}/bin$)') 
print 'Total integrated flux', np.sum(((dn_de[1:] + dn_de[:-1]) / 2.0)*(energies[1:] - energies[:-1])/1e6),'photons/s/cm^2'
#plt.loglog(energies[1:], dn_de[1:]*(energies[1:] - energies[:-1])*energies[1:]*1.6e-12)

plt.show()

