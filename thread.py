import threading
import time


class MyThread(threading.Thread):
    # 继承Thread类
    def run(self):
        for i in range(0, 5):
            print(i)
            time.sleep(1)
