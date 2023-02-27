from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command


if __name__ == '__main__':

    nr = InitNornir(config_file="nornir.yaml")
    print(nr)
    results = nr.run(task=netmiko_send_command, command_string='display version')
    print_result(results)
