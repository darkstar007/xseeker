
def read_xcom_data():
    symbols = ['H', 'Na', 'Mg', 'Ca', 'Ti', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
               'Pt', 'Au', 'Hg', 'Pb', 'U', 'Al', 'C', 'Ge', 'F', 'Cl', 'I',
               'Si', 'He', 'Ne', 'Ar', 'Xe', 'O', 'N']
    
    data = {}
    for sym in symbols:
        fp = open('../xray_attenuation/'+sym+'.txt')
        data[sym] = {}
        data[sym]['Mev'] = []
        data[sym]['mu'] = []
        for ln in fp:
            bits = ln.split()
            if len(bits) == 8 or len(bits) < 10:
                try:
                    if len(bits) == 8:
                        data[sym]['Mev'].append(float(bits[0]))
                        data[sym]['mu'].append(float(bits[6]))
                        #if len(bits) == 10:
                        #data[sym]['Mev'].append(float(bits[2]))
                        #data[sym]['mu'].append(float(bits[9]))
                except ValueError, e:
                    pass

        fp.close()

    return data

