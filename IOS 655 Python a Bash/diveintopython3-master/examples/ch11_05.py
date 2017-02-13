# ch11_05.py
# queue

import time
import threading
import queue


class Worker(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        while True:
            if self.q.empty():
                print('thread stopped')
                break
            job = self.q.get()
            print('run job', str(job), ' from', self.name)
            time.sleep(1)
            self.q.task_done()


q = queue.Queue()
# generate jobs
print('populate jobs')
for i in range(15):
    q.put(i)


my_thread1 = Worker('Thread 1', q)
my_thread1.setDaemon(True)
my_thread2 = Worker('Thread 2', q)
my_thread2.setDaemon(True)
my_thread3 = Worker('Thread 3', q)
my_thread3.setDaemon(True)

my_thread1.start()
my_thread2.start()
my_thread3.start()

my_thread1.join()
my_thread2.join()
my_thread3.join()

# python 3
input("Press Enter to stop...")

# python 2
#raw_input("Press Enter to stop...")

print('Done all')

