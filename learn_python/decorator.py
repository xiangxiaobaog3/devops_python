import time

# 作为一个函数
# 返回包装原始函数调用的一个子函数
def mydecorator(function):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        # 添加额外的功能：执行被装饰函数之前的操作
        result = function(*args, **kwargs)
        # 添加额外的功能：执行被装饰函数之前的操作 的
        end_time = time.time()
        print(f'测试执行效率{end_time-start_time}')
        return result
    # 返回wrapper作为装饰函数
    return wrapped

@mydecorator
def index(name):
    time.sleep(3)
    print(f'2{name}')
    return 666

ret = index("xiang")
print(ret)


# 作为一个类
class DecoratorAsClass:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # 添加额外的功能：执行被装饰函数之前的操作
        result = self.function(*args, **kwargs)
        # 添加额外的功能：执行被装饰函数之前的操作 的
        # 并返回结果
        return result


# 参数化装饰器
def repeat(number=3):
    """ 多次重复执行装饰函数
    返回最后一次原始函数调用的值作为结果
    :param number: 重复次数，默认值是3
    :return:
    """
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

@repeat(2)
def foo():
    print("foo")
foo()