import socket
import os
import subprocess


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


def find_docker_compose_file():
    if verify_docker_installation():
        names = find_docker_names()
        print("------------------------------------------"
              "Docker Containers Compile files can be found at: ")
        for items in names:
            container_inspect = subprocess.run(["docker", "container", "inspect", items, "--format",
                                                "\'{{ index .Config.Labels \"com.docker.compose.project.working_dir\" }}\'"],
                                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("{} : {}".format(items, container_inspect.stdout))


def docker_ps():
    result = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)

#def docker_kill():
#todo - kill hanging docker instance

#def docker_learn():
#todo - help with common build tasks resources(common commands and what they mean, maybe they go into the help box)
