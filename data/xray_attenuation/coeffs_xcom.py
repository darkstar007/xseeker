
from read_xcom_data import read_xcom_data

data = read_xcom_data()

print len(data['O']['Mev']), len(data['N']['Mev']), len(data['Ar']['Mev'])
print data['O']['Mev']
print data['N']['Mev']
print data['Ar']['Mev']
