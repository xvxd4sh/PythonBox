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
    response = os.system("ping -n 1 " + address)
    if response == 0:
        print("Woo it is alive")
    else:
        print("it sure is stinky in here, cause its dead. ")


def verify_docker_installation() -> bool:
    result = subprocess.Popen(["docker", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result.wait()
    if result.returncode == 0:
        print("docker is installed")
        return True
    else:
        print("I believe that docker is not installed.")
        return False


def find_docker_names() -> list:
    names = list()
    result = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    resultparse = result.stdout.split("\n")
    for lines in resultparse:
        if len(lines) is not 0:
            linesplit = lines.split()
            names.append(linesplit[0])
    if names[0] == 'CONTAINER':
        names.pop(0)
    return names


def find_docker_compose_file_print():
    if verify_docker_installation():
        names = find_docker_names()
        print("------------------------------------------"
              "Docker Containers Compile files can be found at: ")
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
            temp.append("{}".format(container_inspect.stdout))
    #todo - parsing temp for final list
    return final_compose_file


def docker_ps():
    result = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)



# kill hanging docker instance
def docker_kill():
    docker_process = proc_find("docker-compose up")
    docker_pid = pid_find(docker_process)
    if len(docker_pid) > 0:
        for items in docker_pid:
            print("killing {} with a SIGTERM signal".format(items))
            os.kill(items, 15)
        waiting(25)
    else:
        print("No process ID has been successfully located")

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
            print("There is something wrong with your docker compose file ")
    else:
        print("Something is wrong with your path")


# todo - make a system to build based on a path
def docker_restart():
    #todo - use find_docker_compose_file_list() to start the initial process
    print("not done")

# def docker_learn():
# todo - help with common build tasks resources(common commands and what they mean, maybe they go into the help box)

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

