from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result


def say_hello(task_context):
    """
    让每台设备来和大家打个招呼
    :param task_context:用于上下文相关信息的管理，比如设备信息，nornir的配置等等
    :return:返回打招呼的字符串
    """
    words_templ = "Hello!I'm a network device. My name is {}"
    words = words_templ.format(task_context.host.name)
    return Result(host=task_context.host, result=words)

if __name__ == '__main__':

    nr = InitNornir(config_file="nornir.yaml")
    results = nr.run(task=say_hello)
    print_result(results)