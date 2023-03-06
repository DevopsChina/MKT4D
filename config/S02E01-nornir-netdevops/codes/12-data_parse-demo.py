from pathlib import Path

from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command


def parse_data(task_context, cmd, textfsm_templ):
    """
    执行指定命令，将配置回显中的数据使用textfsm进行提取
    Args:
        cmd: 执行的命令
        textfsm_templ: 解析模板

    Returns:
        解析后的数据

    """
    host_task_result_obj = task_context.run(netmiko_send_command,
                                            command_string=cmd,
                                            use_textfsm=True,
                                            textfsm_template=textfsm_templ)
    data = host_task_result_obj[0].result
    return Result(host=task_context.host, result=data)


if __name__ == '__main__':
    nr = InitNornir(config_file="nornir.yaml")
    result = nr.run(task=parse_data,
                    cmd='display interface brief',
                    textfsm_templ='huawei_display_interface_brief.textfsm',
                    name='解析端口列表')
    print_result(result)
