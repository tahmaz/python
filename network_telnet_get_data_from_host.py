import getpass
import telnetlib
import time

timestr =  time.strftime("%Y%m%d-%H%M%S")
user = "test"
password="testpass"
file = open("ips.txt","r")
lines = file.readlines()
#print(lines)
for ip in lines:
    ip = ip.rstrip("\n")
    print(ip)
    tn = telnetlib.Telnet(ip)
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"show context all\n")
    tn.write(b"exit\n")
    sample=open(timestr +".txt","a")
    print(tn.read_all().decode('ascii'),file=sample)
    sample.close()