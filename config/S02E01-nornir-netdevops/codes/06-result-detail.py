from nornir import InitNornir
from nornir.core.task import Result


def get_dev_platform(task_context):
    return Result(host=task_context.host, result=task_context.host.platform)


def get_dev_info(task_context):
    dev_info = {
        'name': task_context.host.name,
        'ip': task_context.host.hostname,
    }
    # task上下文调用run方法，执行结果返回的是当前设备调用的task函数的所有结果即MultiResult对象
    host_task_result_obj = task_context.run(get_dev_platform)
    # 由于task函数可以组合调用，最顶层调用位于MultiResult对象最前列
    # 我们用类似列表的索引方式，访问索引0即可获取我们调用的task函数的执行结果
    # 然后取其result属性获取实际返回的载荷结果，
    # 也可以访问其failed等属性，了解其是否失败或者此次任务是否对设备配置产生影响
    platform = host_task_result_obj[0].result
    dev_info['platform'] = platform
    return Result(host=task_context.host, result=dev_info)


if __name__ == '__main__':

    nr = InitNornir(config_file="nornir.yaml")
    nr_results = nr.run(task=get_dev_info)
    print(nr_results, type(nr_results))

    # AggregatedResult对象类似字典，我们可以通过调用其items方法对其循环，
    # 返回的结果是一个元组，两个值对应Host对象和当前Host对象的所有task任务执行结果MultiResult对象
    for host, host_results in nr_results.items():
        print('#' * 20, '这是一个设备的所有task的执行结果MultiResult对象', '#' * 20)
        print(host_results)
        print(type(host_results))
        print('-' * 20, '接下来我们循环迭代一个设备所有task任务的执行结果', '-' * 20)
        # MultiResult对象类似列表，我们直接可以进行for循环，可以使用索引号访问其某次task执行的结果Result对象
        for host_task_result_obj in host_results:
            print('~' * 20, '这是一台设备一个task任务的执行结果Result对象', '~' * 20)
            print(type(host_task_result_obj))
            print(host_task_result_obj)
            print('+' * 20, '这是一台设备一个task任务的执行结果Result对象的result属性', '+' * 20)
            print(type(host_task_result_obj.result))
            print(host_task_result_obj.result)
