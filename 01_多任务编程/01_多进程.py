# 进程是资源分配的最小单位
import time
import multiprocessing
import os


# # 创建进程实列
# def confing():
#     for i in range(3):
#         print('confing')
#         time.sleep(1)
#
#
# def music():
#     for i in range(3):
#         print('music')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 通过进程创建进程对象
#     confing_process = multiprocessing.Process(target=confing)
#     music_process = multiprocessing.Process(target=music)
#
#     # 启动进程
#     confing_process.start()
#     music_process.start()


# 进程执带有参数的任务
# def confing(num, name):
#     for i in range(num):
#         print('confing')
#         print(name)
#         time.sleep(1)
#
#
# def music(count, name):
#     for i in range(count):
#         print('music')
#         print(name)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 通过进程创建进程对象
#     confing_process = multiprocessing.Process(target=confing, args=(3, '位置'))  # 位置参数
#     music_process = multiprocessing.Process(target=music, kwargs={'count': 3, 'name': '关键词'})  # 关键词参数
#     # 启动进程
#     confing_process.start()
#     music_process.start()


# # 获取进程的编号
# def confing():
#     print('confing子进程编号：%d' % os.getpid())
#     print('confing子进程编号：%d' % os.getppid())
#
#     for i in range(3):
#         print('confing')
#
#
# def music():
#     print('music子进程编号：%d' % os.getpid())
#     print('music父进程编号：%d' % os.getppid())
#     for i in range(3):
#         print('music')
#
#
# if __name__ == '__main__':
#     print('主进程编号：%d' % os.getpid())
#     confing_process = multiprocessing.Process(target=confing)
#     music_process = multiprocessing.Process(target=music)
#     confing_process.start()
#     music_process.start()


# # 进程间不共享全局变量
# data = []
#
#
# def write_data():
#     for i in range(3):
#         print(i)
#         data.append(i)
#     print('write_data', data)
#
#
# def read_data():
#     print('read_data', data)
#
#
# if __name__ == '__main__':
#     write_process = multiprocessing.Process(target=write_data)
#     read_process = multiprocessing.Process(target=read_data)
#
#     write_process.start()
#     time.sleep(1)
#     read_process.start()


# 主进程会等待所有的子进程执行结束再结束
# 设置守护主进程, 主进程结束后不在执行子进程
def work():
    for i in range(3):
        print("工作中.....")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work())
    # work_process.daemon = True
    work_process.start()

    time.sleep(0.2)
    work_process.terminate()
    print('主进程结束')
