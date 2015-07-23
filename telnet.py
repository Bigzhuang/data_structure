import telnetlib
host=['10.18.11.2']

tn=telnetlib.Telnet(host[0])
tn.read_until('Username: ')
tn.write('rayking\n')
#print 'ok'
tn.read_until('Password: ')
tn.write('rayking\n')
tn.read_until('>')
tn.write('en\n')
tn.read_until('Password: ')
tn.write('cisco\n')
tn.write('show int statu\nexit\n')
#print tn.read_all()

with open('hehe.txt','a+')as f:
	f.write(tn.read_all())