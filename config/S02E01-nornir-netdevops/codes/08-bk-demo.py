from datetime import date

from nornir import InitNornir
from nornir.core.task import Result
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file


def config_backup(task_context):
    cmds = task_context.host.data['cmds']
    cmds = cmds.split(',')
    date_str = date.today().strftime('%Y%m%d')
    ip = task_context.host.hostname
    for cmd in cmds:
        cmd_multi_result_objs = task_context.run(task=netmiko_send_command, command_string=cmd)
        output = cmd_multi_result_objs[0].result
        filepath = '{}_{}_{}.txt'.format(date_str, ip, cmd)
        file_multi_result_objs = task_context.run(task=write_file,
                                                  filename=filepath,
                                                  content=output)

    return Result(host=task_context.host, result=cmds)


if __name__ == '__main__':
    nr = InitNornir(config_file="nornir.yaml")
    results = nr.run(task=config_backup)
    print_result(results)
