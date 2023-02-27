from nornir import InitNornir
from nornir.core.inventory import Host
from nornir.core.task import AggregatedResult, MultiResult, Result, Task


class RealTimePrintResult:
    def task_started(self, task: Task) -> None:
        print(f">>> starting: {task.name}")

    def task_completed(self, task: Task, result: AggregatedResult) -> None:
        print(f">>> completed: {task.name}")

    def task_instance_started(self, task: Task, host: Host) -> None:
        pass

    def task_instance_completed(
        self, task: Task, host: Host, result: MultiResult
    ) -> None:
        print(f"  - {host.name}: - {result.result}")

    def subtask_instance_started(self, task: Task, host: Host) -> None:
        pass  # to keep example short and sweet we ignore subtasks

    def subtask_instance_completed(
        self, task: Task, host: Host, result: MultiResult
    ) -> None:
        pass  # to keep example short and sweet we ignore subtasks

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
    nr_with_processors = nr.with_processors(processors=[RealTimePrintResult()])
    results = nr_with_processors.run(task=say_hello)