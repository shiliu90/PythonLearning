# 线程池与进程池
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import threading
import os
import time


def work(n):
    print(f'给{n}打电话:进程号:{os.getpid()},线程号:{threading.current_thread()}')
    time.sleep(3)
    print(f'{n}通话结束:进程号:{os.getpid()},:线程号:{threading.current_thread()}')


userlist = ['刘德华','吴彦祖','梁朝伟','周杰伦','林俊杰']

# 1. 创建 线程池  推荐使用多线程或线程池
pool = ThreadPoolExecutor(max_workers=3)
# 1. 创建 进程池
# pool = ProcessPoolExecutor(max_workers=3)

# 2. 循环指派任务和参数
[ pool.submit(work,user) for user in userlist]

# 3 关闭 线程池 进程池
pool.shutdown()

# 作业任务：  豆瓣电影 Top 250
# 足球信息， 懂球帝，房价信息，二手车数据，....
# 不低于五万条


