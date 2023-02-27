from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result


def say_with_words(task_context, words):
    words_templ = "{}"
    words = words_templ.format(words)
    return Result(host=task_context.host, result=words)


def say_dev_name(task_context):
    words_templ = "This is {}."
    words = words_templ.format(task_context.host)
    return Result(host=task_context.host, result=words)


def grouping_say(task_context):
    task_context.run(task=say_with_words, words='Hello!',name='Say Hello')
    task_context.run(task=say_dev_name,name='Say Name')
    task_context.run(task=say_with_words, words='Bye!',name='Say Bye')
    result = 'Grouing task is done'
    return Result(host=task_context.host, result=result)


nr = InitNornir(config_file="nornir.yaml")
results = nr.run(task=grouping_say)
print_result(results)
