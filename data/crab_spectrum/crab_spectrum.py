#!/usr/bin/env python

import numpy as np

import matplotlib.pyplot as plt

# numbers from http://arxiv.org/pdf/0911.2412v1.pdf

N0_100Mev = 2.36e-10   # ph cm^-2 s^-1 MeV^-1
gamma_100Mev = 1.97
Ecutoff_100Mev = 5.8e9 # eV

energies_100Mev = 10.0 ** np.arange(8.0,11.1, 0.001)
dn_de_100Mev = N0_100Mev * ((energies_100Mev / 1e9) ** -gamma_100Mev)  * np.exp(- (energies_100Mev / Ecutoff_100Mev))

mpt_100Mev = (energies_100Mev[1:] + energies_100Mev[:-1]) / 2.0

flux_fermi = np.sum(((dn_de_100Mev[1:] + dn_de_100Mev[:-1]) / 2.0)*(energies_100Mev[1:] - energies_100Mev[:-1])/1e6)

# TTM: From PhD

N0_2kev = 9.9 # ph cm^-2 s^-1 keV^-1
gamma_2kev = 2.13

energies_2kev = np.arange(2.0,30, 0.1)
dn_de_2kev = N0_2kev * (energies_2kev ** -gamma_2kev)
mpt_2kev = (energies_2kev[1:] + energies_2kev[:-1]) / 2.0

flux_ttm = np.sum(((dn_de_2kev[1:] + dn_de_2kev[:-1]) / 2.0)*(energies_2kev[1:] - energies_2kev[:-1]))

# Integral: From http://arxiv.org/pdf/0810.0646.pdf

N0_int = 6.3e-4   # @100keV ph cm^-2 s^-1 kev^-1
gamma0_int = 2.105
gamma1_int = 2.22
energies0_int = 10.0 ** np.arange(np.log10(2.0), 2, 0.01)
energies1_int = 10.0 ** np.arange(2, 3, 0.01)
dn_de0_int = N0_int * (energies0_int / 100.0) ** - gamma0_int
dn_de1_int = N0_int * (energies1_int / 100.0) ** - gamma1_int

mpt0_int = (energies0_int[1:] + energies0_int[:-1]) / 2.0
mpt1_int = (energies1_int[1:] + energies1_int[:-1]) / 2.0

flux_int = np.sum(((dn_de0_int[1:] + dn_de0_int[:-1]) / 2.0)*(energies0_int[1:] - energies0_int[:-1])) + np.sum(((dn_de1_int[1:] + dn_de1_int[:-1]) / 2.0)*(energies1_int[1:] - energies1_int[:-1]))

# Comptel: From http://arxiv.org/pdf/astro-ph/9710211.pdf

Ecutoff_1Mev = 41  # MeV
N0_1Mev = 1.29e-4  # pht cm^-2 s^-1 MeV-1
gamma_1Mev = 2.02
energies_1Mev = 10.0 ** np.arange(0.0, 2, 0.01)
dn_de_1Mev = N0_1Mev * ((energies_1Mev / 3.5) ** -gamma_1Mev)  * np.exp(- (energies_1Mev / Ecutoff_1Mev))
mpt_1Mev = (energies_1Mev[1:] + energies_1Mev[:-1]) / 2.0
flux_comp = np.sum(((dn_de_1Mev[1:] + dn_de_1Mev[:-1]) / 2.0)*(energies_1Mev[1:] - energies_1Mev[:-1]))

########################################

units = ' $photons\, s^{-1} cm^{-2}$)'
plt.loglog(mpt_2kev*1000, ((dn_de_2kev[1:] + dn_de_2kev[:-1]) / 2.0), '-og', alpha=0.7, label='TTM (flux='+format(flux_ttm, '.3f')+units)

plt.loglog(mpt0_int*1000, ((dn_de0_int[1:] + dn_de0_int[:-1]) / 2.0), '-+r', label='Integral (flux='+format(flux_int, '.3f')+units)
plt.loglog(mpt1_int*1000, ((dn_de1_int[1:] + dn_de1_int[:-1]) / 2.0), '-+r')

plt.loglog(mpt_1Mev*1e6, ((dn_de_1Mev[1:] + dn_de_1Mev[:-1]) / 2.0)/1000.0, '-+c', label='COMPTEL (flux='+format(flux_comp, '.3g')+units)

plt.loglog(mpt_100Mev, ((dn_de_100Mev[1:] + dn_de_100Mev[:-1]) / 2.0)/1000.0, '-+b', label='FERMI LAT (flux='+format(flux_fermi, '.3g')+units)

plt.xlabel('$X/\gamma$-ray energy ($eV$)')
plt.ylabel('Flux ($photon/s/cm^{2}/keV$)') 

print 'Total integrated flux (2-30kev - TTM)', flux_ttm,'photons/s/cm^2'

print 'Total integrated flux (2keV-1Mev - Integral)', flux_int, 'photons/s/cm^2'

print 'Total integrated flux (1-100Mev Comptel)', flux_comp, 'photons/s/cm^2'

print 'Total integrated flux (100-111000Mev - Fermi-LAT)', flux_fermi,'photons/s/cm^2'

plt.legend()

#plt.loglog(energies[1:], dn_de[1:]*(energies[1:] - energies[:-1])*energies[1:]*1.6e-12)

plt.show()

