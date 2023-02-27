from nornir import InitNornir

if __name__ == '__main__':
    # 普通筛选，可以多个字段
    nr = InitNornir(config_file="nornir.yaml")
    huawei_devs = nr.filter(platform='huawei')  # 直接按字段进行筛选，可同时筛选多个字段，这些字段之间是且的关系
    print(huawei_devs.inventory.hosts)

#########################################自定义筛选函数######################
from nornir import InitNornir


# 定义筛选函数
def huawei_bj_filter(host):
    if host.platform == 'huawei' and host['city'] == 'beijing':
        return True
    return False


if __name__ == '__main__':
    nr = InitNornir(config_file="nornir.yaml")
    # 调用筛选函数，赋值filter_func为我们定义的筛选函数即可
    huawei_beijing_devs = nr.filter(filter_func=huawei_bj_filter)
    print(huawei_beijing_devs.inventory.hosts)

#################################筛选对象与逻辑计算###########################
from nornir import InitNornir
from nornir.core.filter import F

if __name__ == '__main__':
    nr = InitNornir(config_file="nornir.yaml")
    # 逻辑非运算，使用~
    nr_devs = nr.filter(~F(city='shanghai'))
    # 逻辑且运算，使用&
    nr_devs = nr.filter(F(platform='huawei') & F(city='beijing'))
    # 逻辑或运算，使用|
    nr_devs = nr.filter(F(city='beijing') & F(city='shanghai'))
