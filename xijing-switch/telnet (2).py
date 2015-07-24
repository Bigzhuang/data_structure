import telnetlib,re
from openpyxl import Workbook
host='10.18.11.2'
tn=telnetlib.Telnet(host)
tn.read_until('Username: ')
tn.write('rayking'+'\n')
tn.read_until('Password: ')
tn.write('rayking'+'\n')
tn.read_until('>')
tn.write('en'+'\n')
tn.read_until('Password: ')
tn.write('cisco'+'\n')


#commande
tn.write('show por add\n')
tn.write('exit\n')
with open('show_port','w+') as f:
    f.write(tn.read_all())