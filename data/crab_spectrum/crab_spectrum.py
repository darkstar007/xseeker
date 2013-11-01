#!/usr/bin/env python

import numpy as np

import matplotlib.pyplot as plt

import crab_spectra_instruments as csi

dn_de_comp, energy_comp = csi.comptel()
dn_de_int, energy_int = csi.integral()
dn_de_ttm, energy_ttm = csi.TTM()
dn_de_fermi, energy_fermi = csi.fermi()

########################################

flux_ttm = csi.calcflux(dn_de_ttm, energy_ttm)
flux_int = csi.calcflux(dn_de_int, energy_int)
flux_comp = csi.calcflux(dn_de_comp, energy_comp)
flux_fermi = csi.calcflux(dn_de_fermi, energy_fermi)

units = ' $photons\, s^{-1} cm^{-2}$)'
plt.loglog(energy_ttm, dn_de_ttm, '-og', alpha=0.7, label='TTM (flux='+format(flux_ttm, '.3f')+units)

plt.loglog(energy_int, dn_de_int, '-+r', label='Integral (flux='+format(flux_int, '.3f')+units)

plt.loglog(energy_comp, dn_de_comp, '-+c', label='COMPTEL (flux='+format(flux_comp, '.3g')+units)

plt.loglog(energy_fermi, dn_de_fermi, '-+b', label='FERMI LAT (flux='+format(flux_fermi, '.3g')+units)

plt.xlabel('$X/\gamma$-ray energy ($keV$)')
plt.ylabel('Flux ($photon s^{-1} cm^{-2} keV^{-1}$)') 

print 'Total integrated flux (2-30kev - TTM)', flux_ttm,'photons/s/cm^2'

print 'Total integrated flux (2keV-1Mev - Integral)', flux_int, 'photons/s/cm^2'

print 'Total integrated flux (1-100Mev Comptel)', flux_comp, 'photons/s/cm^2'

print 'Total integrated flux (100-111000Mev - Fermi-LAT)', flux_fermi,'photons/s/cm^2'

plt.legend()

#plt.loglog(energies[1:], dn_de[1:]*(energies[1:] - energies[:-1])*energies[1:]*1.6e-12)

plt.show()

