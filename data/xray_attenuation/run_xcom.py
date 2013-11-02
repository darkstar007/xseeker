
from string import Template

cmd = Template("""$name
2
$chem_symbol
2
1
$file
1
""")

from subprocess import Popen, PIPE

symbols = ['H', 'Na', 'Mg', 'Ca', 'Ti', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
           'Pt', 'Au', 'Hg', 'Pb', 'U', 'Al', 'C', 'Ge', 'F', 'Cl', 'I',
           'Si', 'He', 'Ne', 'Ar', 'Xe', 'O', 'N']

for sym in symbols:
    cmd_args = {'name': sym, 'chem_symbol': sym, 'file': sym+'.txt'}
    cmd_str = cmd.substitute(cmd_args)
    p = Popen('./XCOM', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    print p.communicate(cmd_str)
    p.wait()
    
