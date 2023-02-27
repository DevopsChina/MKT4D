from pathlib import Path

from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config


def push_configs(task_context, config_dir='configs'):
    """
    从指定文件夹内读取设备IP.txt的配置文件，推送给网络设备
    Args:
        config_dir: 配置文件的目录

    Returns:
        配置过程的回显

    """
    output = ''
    # 拼接配置文件路径，任何对象在format函数中使用的时候都会强制用str转为字符串
    config_file = '{}.txt'.format(Path(config_dir, task_context.host.hostname))
    # 获取netmiko连接
    net_conn = task_context.host.get_connection('netmiko', task_context.nornir.config)
    # 判断是否enable
    if net_conn.secret:
        net_conn.enabled()
    # 通过配置文件推送配置
    output = output + net_conn.send_config_from_file(config_file=config_file)
    # 保存配置
    output = output + net_conn.save_config()
    # 回显结果放入结果中，变更成功，配置发生了变化。
    return Result(host=task_context.host, result=output, changed=True)


if __name__ == '__main__':
    nr = InitNornir(config_file="nornir.yaml")
    result = nr.run(task=push_configs,
                    config_dir='configs',
                    name='推送配置到网络设备')
    print_result(result)
