import sys, getopt
from helpbox import * 
from utility import * 

def main(argv): 
   try:
      opts, args = getopt.getopt(argv,"hp:",["help","ping"])
   except getopt.GetoptError:
      print('error')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ["-h", "--help"]:
         print('this does nothing but ping and spinning banner rn')
         sys.exit()
      elif opt in ["-p", "--ping"]:
        IP = arg
        if is_valid_ipv4_address(IP):
            print("sending ping to",IP)
            ping(IP)
        else: 
            print("invalid IP Address")

    
if __name__ == "__main__": 
    gethelp()
    main(sys.argv[1:])