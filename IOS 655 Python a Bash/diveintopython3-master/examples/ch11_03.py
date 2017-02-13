# ch11_03.py
# thread synchronization

import time
import threading


class MyThread(threading.Thread):
    def __init__(self, name, o_lock):
        threading.Thread.__init__(self)
        self.name = name
        self.running = False
        self.value_lock = o_lock

    def run(self):
        global value
        self.running = True
        while self.running:
            self.value_lock.acquire()
            value += 1
            print('value:', str(value),' from ', self.name)
            self.value_lock.release()
            time.sleep(2)

    def stop(self):
        print('stopping ', self.name)
        self.running = False
        self.join(2)


global value
value = 0
value_lock = threading.Lock()

my_thread1 = MyThread('Thread 1',value_lock)
my_thread1.setDaemon(True)
my_thread2 = MyThread('Thread 2',value_lock)
my_thread2.setDaemon(True)

my_thread1.start()
my_thread2.start()
# python 3
input("Press Enter to stop...")

# python 2
#raw_input("Press Enter to stop...")

my_thread1.stop()
my_thread2.stop()

