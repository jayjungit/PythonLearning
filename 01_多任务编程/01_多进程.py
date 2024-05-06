# 进程是资源分配的最小单位
import time
import multiprocessing


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
def confing(num, name):
    for i in range(num):
        print('confing')
        print(name)
        time.sleep(1)


def music(count, name):
    for i in range(count):
        print('music')
        print(name)
        time.sleep(1)


if __name__ == '__main__':
    # 通过进程创建进程对象
    confing_process = multiprocessing.Process(target=confing, args=(3, '位置'))  # 位置参数
    music_process = multiprocessing.Process(target=music, kwargs={'count': 3, 'name': '关键词'})  # 关键词参数
    # 启动进程
    confing_process.start()
    music_process.start()

