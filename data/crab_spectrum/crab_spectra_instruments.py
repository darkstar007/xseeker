
import numpy as np

# Return photons cm^-2 s^-1
def calcflux(dn_de, energy):
    flux = np.sum(((dn_de[1:] + dn_de[:-1]) / 2.0) * (energy[1:] - energy[:-1]))
    return flux

def mpt(energy):
    return ((energy[1:] + energy[:-1]) / 2.0)

# These all return (dn_de, energy) om photons/cm^-2 s^-1 kev^-1, kev
def fermi():
    # numbers from http://arxiv.org/pdf/0911.2412v1.pdf
    
    N0_100Mev = 2.36e-10   # ph cm^-2 s^-1 MeV^-1
    gamma_100Mev = 1.97
    Ecutoff_100Mev = 5.8e9 # eV
    
    energies_100Mev = 10.0 ** np.arange(8.0,11.1, 0.001)
    dn_de_100Mev = N0_100Mev * ((energies_100Mev / 1e9) ** -gamma_100Mev)  * np.exp(- (energies_100Mev / Ecutoff_100Mev))
    
    #mpt_100Mev = (energies_100Mev[1:] + energies_100Mev[:-1]) / 2.0
    
    #flux_fermi = np.sum(((dn_de_100Mev[1:] + dn_de_100Mev[:-1]) / 2.0)*(energies_100Mev[1:] - energies_100Mev[:-1])/1e6)

    return (dn_de_100Mev/1000.0, energies_100Mev/1000.0)

def TTM():
    # TTM: From PhD
    
    N0_2kev = 9.9 # ph cm^-2 s^-1 keV^-1
    gamma_2kev = 2.13
    
    energies_2kev = np.arange(2.0,30, 0.1)
    dn_de_2kev = N0_2kev * (energies_2kev ** -gamma_2kev)
    #mpt_2kev = (energies_2kev[1:] + energies_2kev[:-1]) / 2.0
    
    #flux_ttm = np.sum(((dn_de_2kev[1:] + dn_de_2kev[:-1]) / 2.0)*(energies_2kev[1:] - energies_2kev[:-1]))

    return (dn_de_2kev, energies_2kev)


def integral():
    # Integral: From http://arxiv.org/pdf/0810.0646.pdf
    
    N0_int = 6.3e-4   # @100keV ph cm^-2 s^-1 kev^-1
    gamma0_int = 2.105
    gamma1_int = 2.22
    energies_int = 10.0 ** np.arange(np.log10(2.0), 3, 0.01)
    #energies1_int = 10.0 ** np.arange(2, 3, 0.01)
    v = np.where(energies_int >= 100)
    dn_de_int = N0_int * (energies_int / 100.0) ** - gamma0_int
    dn_de_int[v] = N0_int * (energies_int[v] / 100.0) ** - gamma1_int
    
    #mpt0_int = (energies0_int[1:] + energies0_int[:-1]) / 2.0
    #mpt1_int = (energies1_int[1:] + energies1_int[:-1]) / 2.0
    
    #flux_int = np.sum(((dn_de0_int[1:] + dn_de0_int[:-1]) / 2.0)*(energies0_int[1:] - energies0_int[:-1])) + np.sum(((dn_de1_int[1:] + dn_de1_int[:-1]) / 2.0)*(energies1_int[1:] - energies1_int[:-1]))

    return (dn_de_int, energies_int)


def comptel():
    # Comptel: From http://arxiv.org/pdf/astro-ph/9710211.pdf
    
    Ecutoff_1Mev = 41  # MeV
    N0_1Mev = 1.29e-4  # pht cm^-2 s^-1 MeV-1
    gamma_1Mev = 2.02
    energies_1Mev = 10.0 ** np.arange(0.0, 2, 0.01)
    dn_de_1Mev = N0_1Mev * ((energies_1Mev / 3.5) ** -gamma_1Mev)  * np.exp(- (energies_1Mev / Ecutoff_1Mev))

    #mpt_1Mev = (energies_1Mev[1:] + energies_1Mev[:-1]) / 2.0
    #flux_comp = np.sum(((dn_de_1Mev[1:] + dn_de_1Mev[:-1]) / 2.0)*(energies_1Mev[1:] - energies_1Mev[:-1]))

    return (dn_de_1Mev / 1000, energies_1Mev *1000.0)

    
