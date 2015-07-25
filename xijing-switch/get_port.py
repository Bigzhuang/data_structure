import telnetlib
import getpass
host=[
#'10.18.11.2',
'10.10.253.13'
]
username=raw_input('input userame:\n>>>')
telnetpass=getpass.getpass('input your telnet password:\n>>>')
enablepass=getpass.getpass('input your enable password:\n>>>')
for ip in host:
    tn=telnetlib.Telnet(ip)
    if tn.read_until('Username: '):
        tn.write(username+'\n')
    print 'ok'
    tn.read_until('Password: ')
    tn.write(telnetpass+'\n')
    tn.read_until('>')
    tn.write('en\n')
    tn.read_until('Password: ')
    tn.write(enablepass+'\n')
    tn.write('show por add\nexit\n')
    m=40*'+'+ip+40*'+'
    with open('makefile/port.txt','a+')as f:
        f.write(m)
        f.write(tn.read_all())