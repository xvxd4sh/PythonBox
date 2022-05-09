import getopt
import sys

from helpbox import *
from utility import *


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hnd:", ["help", "network", "docker"])
    except getopt.GetoptError:
        print('error')
        sys.exit(2)
    for opt, args in opts:
        if opt in ["-h", "--help"]:
            gethelp()
            sys.exit()
        elif opt in ["-n", "--network"]:
            parameters = args[0]
            print(args)
            if parameters == "ping":
                ip_address = parameters[1:]
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
            else:
                gethelp_network()
        elif opt in ["-d", "--docker"]:
            print("Docker utility tools activated")
            parameters = args[0]
            if parameters == "list":
                docker_ps()
            elif parameters == "find":
                print("finding active docker-compose file")
                find_docker_compose_file_print()
            elif parameters == "build":
                docker_build(args[1])
            elif parameters == "restart":
                docker_restart()
            elif parameters == "kill":
                docker_kill()
            elif parameters == "learn":
                docker_learn()
            else:
                gethelp_docker()
        else:
            gethelp()


if __name__ == "__main__":
    getbanner()
    main(sys.argv[1:])
