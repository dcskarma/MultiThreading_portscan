#!/usr/bin/env python3
import socket
import sys
from datetime import datetime
import threading

if len(sys.argv)==2:
    target= socket.gethostbyname(sys.argv[1])
else :
    print ("The Input is not valid")
print("__"*50)
print("Scaninig the target : "+ target)
print("Scanning started at  : {}".format(datetime.now()) )

def scan(p1, p2):
    try :
       for port in range(p1, p2):
        
           s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           socket.setdefaulttimeout(0.5)
           res = s.connect_ex((target,port))
           if res == 0:
              print ("port {} is open".format(port))
           s.close()
    except KeyboardInterrupt:

        print ('\n Exting to program')
        sys.exit()
    except socket.gaierror:
        print ("\n Hostname is Couldnot be Resolves")
        sys.exit()
    except socket.error:
        print ("\n Server not responding !!!")
        sys.exit()

    
if __name__ == "__main__":
    try:
            ft1 = threading.Thread(target=scan, args=(1,30))
            ft2 = threading.Thread(target=scan, args=(31,70))
            ft3 = threading.Thread(target=scan, args=(70,100))
            ft4 = threading.Thread(target=scan, args=(101,150))
            ft5 = threading.Thread(target=scan, args=(151,200))
            ft6 = threading.Thread(target=scan, args=(201,1000))


            ft1.join()
            ft2.join()
            ft3.join()
            ft4.join()
            ft5.join()
            ft6.join()
    
    except KeyboardInterrupt:

        print ("Exited from program")


    

print("Done")
