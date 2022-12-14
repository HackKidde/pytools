import sys
import socket
from datetime import datetime
from unittest import result

#Target Define Function
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IPv4
else:
    print("Syntax : python scanner.py <ip>") 

#Add a Banner 
print("-" * 50)
print("Scanning Target" + target)
print("Time Started" + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,80):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #Returns an Error Indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nQuitting ...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't Connect to Server.")
    sys.exit()
