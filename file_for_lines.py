file = open("ips.txt","r")
lines = file.readlines()
#print(lines)
for ip in lines:
    ip = ip.rstrip("\n")
    print(ip)
