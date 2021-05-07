# import subprocess
# from os import devnull
# from platform import pl
# custom classes
from connectivity2 import Connectivity2

cn = Connectivity2()

with open('host_file.txt') as read_file:
    with open('results.txt', 'w') as write_file:
        for line in read_file:
            host = line.strip()
            if cn.check_connectivity(host):
                write_file.write(f"{host}, reachable!\n")
            else:
                write_file.write(f"{host} UNreachable\n")
