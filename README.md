```
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗██████╗  ██████╗ ██╗  ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║██╔══██╗██╔═══██╗╚██╗██╔╝
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║██████╔╝██║   ██║ ╚███╔╝
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══██╗██║   ██║ ██╔██╗
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
```
-------------------------------------------------------------------------------
A command line interface program written in Python for networking research or testing pursposes

-------------------------------------------------------------------------------
# purpose
Inspired by an annoyance while setting up and troubleshooting for seed labs and school projects, we decide to build a python tool kit to assist in the troubleshooting and testing process, ranging from docker management to system management. 

## list of functionality 
- docker management 
  - build
  - restart 
  - kill 
  - learn module 
  - list all active docker session
  - find all active docker compose file
- networking toolset
  - ping 
  - network config check
  - sniffer
- system tool set 
  - lynis auditing

## Currently being implemented 
- system tool set 
  - reverse shell command generator

## Future implementation
- Networking tool sets  
    - scrapy usage 
      - Customizable DNS queries
      - Customizable ARP request, maybe send ARP packet
- system upgrade
  - threading implementation on subsequent processes
