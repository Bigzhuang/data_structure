from openpyxl import Workbook
import telnetlib
wb=Workbook()
ws = wb.active
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
f=open('c:\Users\Dazhuang\Desktop\linux','r')
for line in f.readlines():
    line=line.split()
    #print line
    if line!=[] and line[0].isdigit():
        mac=line[1]
        #print mac
        tn.write('show arp | in '+str(mac)+'\n')
tn.write('exit\n')
print tn.read_all()


