from thread import MyThread

# main
if __name__ == '__main__':
    thread1 = MyThread()
    thread2 = MyThread()

    thread1.start()
    thread2.start()
