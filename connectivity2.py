import platform, subprocess
from os import devnull

class Connectivity2:
    def check_connectivity(self, host):
        if "inux" in platform():
            return self.host_chk_linux(host)
        elif "indow" in platform():
            return self.host_chk_win(host)

    def host_chk_win(self, host):
        FNULL = open(devnull, 'w')
        if subprocess.call(['ping', '-n', 3, host], stdout=FNULL) == 0:
            return True
        return False
    
    def host_chk_linux(self, host):
        FNULL = open(devnull, 'w')
        if subprocess.call(['ping', '-c', '3', host], stdout=FNULL) == 0:
            return True
        return False