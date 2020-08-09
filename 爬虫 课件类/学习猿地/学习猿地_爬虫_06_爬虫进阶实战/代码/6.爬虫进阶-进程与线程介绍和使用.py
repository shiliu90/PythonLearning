#
from multiprocessing import  Process
from threading import Thread
import time,os,threading


# 工作内容
def work(n):
    print(f'给{n}打销售电话,进程号:{os.getpid()},线程号:{threading.current_thread()}')
    time.sleep(3)
    print(f'销售电话结束:{n},进程号:{os.getpid()},线程号:{threading.current_thread()}')


userlist = ['刘德华','张学友','梁朝伟']

# 普通方式来完成
# 启动了一个进程，进程中有一个主线程
# for item in userlist:
#     work(item)


# 多进程 类似于 多个创建多个部门来完成这项工作
# plist = []
# for item in userlist:
#     # 循环创建进程
#     p = Process(target=work,args=(item,))
#     # 生成进程
#     p.start()
#     # 把创建的进程加入到列表中
#     plist.append(p)
#
# # 阻塞终止进程的执行
# [i.join() for i in plist]


# 多线程 类似与 给这个部门增加人手来参数工作

# plist = []
# for item in userlist:
#     # 循环创建 线程
#     p = Thread(target=work,args=(item,))
#     # 生成 线程
#     p.start()
#     # 把创建的 线程 加入到列表中
#     plist.append(p)
#
# # 阻塞终止 线程
# [i.join() for i in plist]


