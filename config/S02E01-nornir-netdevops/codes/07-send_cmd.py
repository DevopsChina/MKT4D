from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

if __name__ == '__main__':
    nr = InitNornir(config_file="nornir.yaml")
    results = nr.run(task=netmiko_send_command, command_string='display current-configuration')
    print_result(results)
