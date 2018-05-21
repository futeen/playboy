# import os
# #fork只能用于linux/unix中
# pid = os.fork()
# print("bobby")
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))


import multiprocessing

#多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)#start之前无进程id
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    #使用线程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())#进程数量等于CPU数量
    # result = pool.apply_async(get_html, args=(3,))#异步提交任务
    #
    # #等待所有任务完成
    # pool.close()#关闭pool，不再接收新的任务
    # pool.join()
    #
    # print(result.get())

    #imap，对应之前executor中的map方法，类似函数编程中的map函数
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))
