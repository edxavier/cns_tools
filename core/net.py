import platform    # For getting the operating system name
import subprocess  # For executing a shell command


def ping(host_ip: str):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host_ip]
    """Envia un mensaje icmp
        :return: 0 Exito ; 1 Falla
    """
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0