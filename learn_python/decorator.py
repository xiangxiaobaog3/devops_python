import time

def timmer(f):
    def inner(*args, **kwargs):
        start_time = time.time()
        # 添加额外的功能：执行被装饰函数之前的操作
        r = f(*args, **kwargs)
        # 添加额外的功能：执行被装饰函数之前的操作 的
        end_time = time.time()
        print(f'测试执行效率{end_time-start_time}')
        return r
    return inner

@timmer
def index(name):
    time.sleep(3)
    print(f'2{name}')
    return 666



ret = index("xiang")
print(ret)
