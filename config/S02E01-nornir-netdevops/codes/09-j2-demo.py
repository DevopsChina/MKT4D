from pathlib import Path

import pandas as pd
from nornir import InitNornir
from nornir.core.task import Result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file


def get_complex_data_from_excel(file='data.xlsx'):
    # 通过表格获取数据，参考jinja2篇章代码
    data = {}
    df_dict = pd.read_excel(file, sheet_name=None)
    for i in df_dict:
        data[i] = df_dict[i].to_dict(orient='records')
    return data


def gen_config_by_j2(task_context,
                     j2_template,
                     j2_data_dir='j2_data',
                     j2_template_dir='j2_template',
                     configs_dir='configs'):
    """
    通过表格文件和Jinja2模板渲染生成标准化配置
    Args:
        j2_template: 调用的jinja2模板
        j2_data_dir: 承载数据的表格文件所放目录
        j2_template_dir: jinja2模板所存放的目录
        configs_dir: 渲染生成的模板放置的目录


    Returns:渲染生成的配置的路径
    """
    # 拼接数据表格文件路径
    data_file = '{}.xlsx'.format(task_context.host.hostname)
    data_file = str(Path(j2_data_dir, data_file))
    # 获取表格中的数据
    data = get_complex_data_from_excel(data_file)

    # 通过nornir_jinja2渲染生成配置
    multi_result = task_context.run(task=template_file,
                                    template=j2_template,
                                    path=j2_template_dir,
                                    data=data)
    config_str = multi_result[0].result

    # 根据IP生成配置文件的名称
    file_name = '{}.txt'.format(task_context.host.hostname)
    # 如无，创建文件夹
    Path(configs_dir).mkdir(exist_ok=True)
    file_name = str(Path(configs_dir, file_name))
    # 使用nornir_utils的write_file将配置写入文件
    task_context.run(write_file, filename=file_name, content=config_str)

    return Result(host=task_context.host, result=file_name)


if __name__ == '__main__':
    nr = InitNornir(config_file="nornir.yaml")
    result = nr.run(task=gen_config_by_j2, j2_template='interface_config.j2')
    print_result(result)
