import getopt
import sys

from helpbox import *
from utility import *


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hpd:", ["help", "ping", "docker"])
    except getopt.GetoptError:
        print('error')
        sys.exit(2)
    for opt, args in opts:
        if opt in ["-h", "--help"]:
            gethelp()
            sys.exit()
        elif opt in ["-p", "--ping"]:
            ip_address = args
            if is_valid_ipv4_address(ip_address):
                print("sending ping to", ip_address)
                ping(ip_address)
            else:
                if ip_address is None:
                    print("you did not put an IP")
                    gethelp_ping()
                else:
                    gethelp_ping()
                    print("invalid IP Address")
        elif opt in ["-d", "--docker"]:
            print("Docker utility tools activated")
            parameters = args
            if parameters == "ps":
                print("ps on docker is being executed")
            elif parameters == "ps-find":
                print("ps-find on docker is being executed")
            else:
                gethelp_docker()
        else:
            gethelp()


if __name__ == "__main__":
    getbanner()
    main(sys.argv[1:])
