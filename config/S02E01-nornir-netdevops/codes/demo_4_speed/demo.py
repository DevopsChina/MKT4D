# /mnt/c/users/Administrator/OneDrive/文档/NetDevOps/git_repos/MKT4D/config/S02E01-nornir-netdevops/codes/demo_4_speed
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
import yaml
from jinja2 import Template
from nornir.core.task import Result
from netmiko import ConnectHandler
from nornir_netmiko import netmiko_file_transfer

def gen_j2(task_context):
    with open('demo.yaml', encoding='utf8') as yml_file:
        data = yaml.load(yml_file, Loader=yaml.CLoader)
    with open('demo.j2', encoding='utf8') as j2_file:
        template = Template(j2_file.read())

    config = template.render(**data)
    with open(f'configs/{task_context.host.name}.txt', encoding='utf8',mode='w') as f:
        f.write(config)

    return Result(host=task_context.host, result='ok')


def send_2_host(task_context):
    s_f = f'configs/{task_context.host.name}.txt'
    d_f = f'/{task_context.host.name}.txt'
    task_context.run(netmiko_file_transfer,source_file=s_f,dest_file=d_f)

    return 'ok'


def gen_j2_and_send_2_host(task):
    ...


if __name__ == '__main__':
    import time
    s = time.time()
    runner = {
        "plugin": "threaded",
        "options": {
            "num_workers": 50,
        },
    }
    inventory = {
        "plugin": "ExcelInventory",
        "options": {
            "excel_file": "inventory.xlsx",
        },
    }

    nr = InitNornir(runner=runner, inventory=inventory)
    result = nr.run(task=gen_j2)
    print_result(result)
    # # dev = nr.filter(name='www487.example.com')
    # result = nr.run(task=send_2_host)
    # e = time.time()
    # print_result(result)
    # print('time:',e-s)
