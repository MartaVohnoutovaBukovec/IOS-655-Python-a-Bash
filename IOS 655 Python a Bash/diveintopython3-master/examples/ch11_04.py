# ch11_04.py
# thread synchronization

import time
import threading


class Worker(threading.Thread):
    def __init__(self, name, signal):
        threading.Thread.__init__(self)
        self.name = name
        self.signal = signal

    def run(self):
        print('waiting from ', self.name)
        self.signal.wait()
        print('processing from ', self.name)
        time.sleep(2)
        print('done from ', self.name)


signal_event = threading.Event()
my_thread1 = Worker('Thread 1', signal_event)
my_thread1.setDaemon(True)
my_thread2 = Worker('Thread 2', signal_event)
my_thread2.setDaemon(True)
my_thread3 = Worker('Thread 3', signal_event)
my_thread3.setDaemon(True)

my_thread1.start()
my_thread2.start()
my_thread3.start()

# waiting for 10 seconds
time.sleep(10)

# start process
print('Send a signal to start processing')
signal_event.set()

# python 3
input("Press Enter to stop...")

# python 2
#raw_input("Press Enter to stop...")

print('Done all')

