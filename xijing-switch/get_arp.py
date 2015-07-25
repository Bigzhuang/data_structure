import telnetlib
host=['10.18.11.2']
for ip in host:
    tn=telnetlib.Telnet(ip)
    tn.read_until('Username: ')
    tn.write('rayking\n')
    tn.read_until('Password: ')
    tn.write('rayking\n')
    tn.read_until('>')
    tn.write('en\n')
    tn.read_until('Password: ')
    tn.write('cisco\n')
    tn.write('show arp\nexit\n')
    with open('makefile/arp.txt','w+')as f:
        f.write(m)
        f.write(tn.read_all())