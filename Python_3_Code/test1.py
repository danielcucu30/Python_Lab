from __future__ import print_function, unicode_literals
 
my_str2 = "someting else"

my_str3 =  ''' THIS
is some
test
'''

ip_addr = '192.168.1.1'
octets = ip_addr.split(".")

print (octets)
port1 = 80
port2 = 443 
#ip_addr1 = '172.16.1.1'
ip_addr2 = '172.31.17.90' 
#ip_addr3 = '217.88.17.1'

print ("\n")
print ("-" * 80)
print ("-" * 80)
#print ("{ip:^20}{ip2:^20}{my_ip3:^20}".format(ip2 = ip_addr1, ip = ip_addr2, my_ip3 =ip_addr3))
#print ("{:10}{:10}{:10}{:10}".format(*octets))
#print ("%s %s"  % (ip_addr, ip_addr2))
print (f"My IP address is : {ip_addr:^20}{port1:^8}")
print (f"My Ip address is : {ip_addr2:^20}{port2:^8}")
print ("\n") 

#print (my_str)
#print (my_str3)
#print (repr(my_str3))
#print ("hello world")
#print ("hello world")

#try:
 #  ip_addr = raw_input ("Enter address   ")
#except NameError:
 #  ip_addr = input ("Enter Address   ")
#print (ip_addr)

