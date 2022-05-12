import random
from traceback import print_exc

help_banner = ["""
                 ________________
                |                |_____    __
                |  PythonBox !   |     |__|  |_________
                |________________|     |::|  |        /
   /\**/\       |                \.____|::|__|      <
  ( o_o  )_     |                      \::/  \._______\ 
   (u--u   \_)  |
    (||___   )==\ 
  ,dP"/b/=( /P"/b\ 
  |8 || 8\=== || 8
  `b,  ,P  `b,  ,P
    """     """`   
"""
    , """
.s5SSSs.                                                  .s5SSSs.  .s5SSSs.          
      SS. .s5 s.  .s5SSSSs. .s    s.  .s5SSSs.  .s    s.        SS.       SS. .s5 s.  
sS    S%S     SS.    SSS          SS.       SS.       SS. sS    S%S sS    S%S     SS. 
SS    S%S ssS SSS    S%S    sS    S%S sS    S%S sSs.  S%S SS    S%S SS    S%S ssS SSS 
SS .sS::'  SSSSS     S%S    SSSs. S%S SS    S%S SS `S.S%S SS .sSSS  SS    S%S  SSSSS  
SS          SSS      S%S    SS    S%S SS    S%S SS  `sS%S SS    S%S SS    S%S SSS SSS 
SS          `:;      `:;    SS    `:; SS    `:; SS    `:; SS    `:; SS    `:; SSS `:; 
SS          ;,.      ;,.    SS    ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. SSS ;,. 
`:          ;:'      ;:'    :;    ;:' `:;;;;;:' :;    ;:' `:;;;;;:' `:;;;;;:' `:; ;:' 
                                                                                      
"""
    , """
'########::'##:::'##:'########:'##::::'##::'#######::'##::: ##:'########:::'#######::'##::::'##:
 ##.... ##:. ##:'##::... ##..:: ##:::: ##:'##.... ##: ###:: ##: ##.... ##:'##.... ##:. ##::'##::
 ##:::: ##::. ####:::::: ##:::: ##:::: ##: ##:::: ##: ####: ##: ##:::: ##: ##:::: ##::. ##'##:::
 ########::::. ##::::::: ##:::: #########: ##:::: ##: ## ## ##: ########:: ##:::: ##:::. ###::::
 ##.....:::::: ##::::::: ##:::: ##.... ##: ##:::: ##: ##. ####: ##.... ##: ##:::: ##::: ## ##:::
 ##::::::::::: ##::::::: ##:::: ##:::: ##: ##:::: ##: ##:. ###: ##:::: ##: ##:::: ##:: ##:. ##::
 ##::::::::::: ##::::::: ##:::: ##:::: ##:. #######:: ##::. ##: ########::. #######:: ##:::. ##:
..::::::::::::..::::::::..:::::..:::::..:::.......:::..::::..::........::::.......:::..:::::..::
"""
    , """
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗██████╗  ██████╗ ██╗  ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║██╔══██╗██╔═══██╗╚██╗██╔╝
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║██████╔╝██║   ██║ ╚███╔╝ 
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══██╗██║   ██║ ██╔██╗ 
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                              
"""
    , """
.-------.  ____     __ ,---------. .---.  .---.     ,-----.    ,---.   .--. _______       ,-----.     _____     __   
\  _(`)_ \ \   \   /  /\          \|   |  |_ _|   .'  .-,  '.  |    \  |  |\  ____  \   .'  .-,  '.   \   _\   /  /  
| (_ o._)|  \  _. /  '  `--.  ,---'|   |  ( ' )  / ,-.|  \ _ \ |  ,  \ |  || |    \ |  / ,-.|  \ _ \  .-./ ). /  '   
|  (_,_) /   _( )_ .'      |   \   |   '-(_{;}_);  \  '_ /  | :|  |\_ \|  || |____/ / ;  \  '_ /  | : \ '_ .') .'    
|   '-.-'___(_ o _)'       :_ _:   |      (_,_) |  _`,/ \ _/  ||  _( )_\  ||   _ _ '. |  _`,/ \ _/  |(_ (_) _) '     
|   |   |   |(_,_)'        (_I_)   | _ _--.   | : (  '\_/ \   ;| (_ o _)  ||  ( ' )  \: (  '\_/ \   ;  /    \   \    
|   |   |   `-'  /        (_(=)_)  |( ' ) |   |  \ `"/  \  ) / |  (_,_)\  || (_{;}_) | \ `"/  \  ) /   `-'`-'    \   
/   )    \      /          (_I_)   (_{;}_)|   |   '. \_/``".'  |  |    |  ||  (_,_)  /  '. \_/``".'   /  /   \    \  
`---'     `-..-'           '---'   '(_,_) '---'     '-----'    '--'    '--'/_______.'     '-----'    '--'     '----' 
                                                                                                                     
"""]


def getbanner():
    num = random.randint(0, 4)
    print(help_banner[num])

def gethelp():
    print("----------------------------------------------------\n"
          "usage: pythonbox [options] [command]\n"
          "\n"
          "options:\n"
          "         -h, --help --------------- Print help text\n"
          "         -n, --network ------------ Utilize a networking module to conduct networking tasks\n"
          "         -d, --docker ------------- Utilize a docker module to conduct docker management\n"
          "         -s, --system ------------- Utilize a system module to conduct a system administrator tasks\n"
          )

def gethelp_network():
    print("----------------------------------------------------\n"
          "usage: pythonbox --network [commands]\n"
          "\n"
          "commands: \n"
          "          check ------------------- conduct a network check (network-interface)\n"
          "          ping -------------------- Utilize ICMP packet to see if a host is online\n"
          "          sniff ------------------- utilize a network interface to sniff packets\n"
          "          rev_shell --------------- Create a bash reverse shell string to run remotely\n"
          )

def gethelp_rev_shell():
    print("----------------------------------------------------\n"
          "usage: pythonbox --network rev_shell [IP address] [Port]\n"
          "\n"
          "IP address : IPV4 address (format [0-255].[0-255].[0-255].[0-255])\n"
          "Port : Port (0-65535)\n"
          )

def gethelp_ping():
    print("----------------------------------------------------\n"
          "usage: pythonbox --network ping [IP address]\n"
          "\n"
          "IP address : IPV4 address (format [0-255].[0-255].[0-255].[0-255])\n"
          )

def gethelp_docker():
    print("----------------------------------------------------\n"
          "usage: pythonbox --docker [commands]\n"
          "\n"
          "commands: \n"
          "          list -------------------- list all running containers\n"
          "          find -------------------- list all running container and their docker compose file\n"
          "          build ------------------- build your docker container from a path\n"
          "          restart ----------------- restart your current running docker container\n"
          "          kill -------------------- kill your current docker containers\n"
          "          learn ------------------- learn common commands from different docker function\n"
          )

def gethelp_build():
    print("----------------------------------------------------\n"
          "usage: pythonbox --docker build [path]\n"
          "\n"
          "path : location of the docker-compose file\n"
          )


def gethelp_system():
    print("----------------------------------------------------\n"
          "usage: pythonbox --system [commands]\n"
          "\n"
          "commands: \n"
          "          audit ------------------- conduct a system audit with lynis\n")

def gethelp_sniff():
    print("----------------------------------------------------\n"
          "usage: pythonbox --network sniff [network-interface] [filter]\n"
          "\n"
          "Network-interface ------------------- the name of the network interface you are sniffing\n"
          "filter ------------------------------ (optional) filter to \n")