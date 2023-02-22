from nornir import InitNornir
from nornir_netmiko import netmiko_send_config
from nornir_utils.plugins.functions import print_result

if __name__ == '__main__':
    nr = InitNornir(config_file="nornir.yaml")
    dev01 = nr.filter(name='netdevops01')
    result = dev01.run(task=netmiko_send_config,
                       config_file=f'configs/192.168.137.201.txt',
                       name='推送配置到网络设备')
    print_result(result)
