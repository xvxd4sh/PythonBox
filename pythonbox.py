import sys

from helpbox import *
from utility import *


def main(argv):
    args = argv
    option = args.pop(0)

    if option in ["-h", "--help"]:
        gethelp()
        sys.exit()

    elif option in ["-n", "--network"]:
        print("Network utility tools activated")
        if len(args) >= 1:
            command = args.pop(0)
            if command == "ping":
                if len(args) >= 1:
                    ip_address = args.pop(0)
                else:
                    ip_address = None
                if ip_address is None:
                    print("you did not put an IP")
                    gethelp_ping()
                elif is_valid_ipv4_address(ip_address):
                    print("sending ping to", ip_address)
                    ping(ip_address)
                else:
                    gethelp_ping()
                    print("invalid IP Address")
            elif command == "check":
                network_pretty_print()
            else:
                gethelp_network()
        else:
            gethelp_network()

    elif option in ["-d", "--docker"]:
        print("Docker utility tools activated")
        if len(args) >= 1:
            command = args.pop(0)
            if command == "list":
                docker_ps()
            elif command == "find":
                print("finding active docker-compose file")
                find_docker_compose_file_print()
            elif command == "build":
                path = args.pop(0)
                if os.path.isdir(path):
                    docker_build(path)
                else:
                    gethelp_build()
            elif command == "restart":
                docker_restart()
            elif command == "kill":
                docker_kill()
            elif command == "learn":
                docker_learn()
            else:
                gethelp_docker()
        else:
            gethelp_docker()

    elif option in ["-s", "--system"]:
        print("System utility tool activated")
        if len(args) >= 1:
            command = args.pop(0)
            if command == "audit":
                system_audit()
            else:
                gethelp_system()
        else:
            gethelp_system()
    else:
        gethelp()


if __name__ == "__main__":
    getbanner()
    if len(sys.argv) >= 2:
        main(sys.argv[1:])
    else:
        gethelp()
