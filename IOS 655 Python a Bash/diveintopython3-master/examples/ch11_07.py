# ch11_07.py
# multiprocessing synchronization

import time
import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self, name, shared_dt):
        multiprocessing. Process.__init__(self)
        self.name = name
        self.running = False
        self.shared_data = shared_dt

    def run(self):
        self.running = True
        while self.running:
            time.sleep(1)
            with self.shared_data.get_lock():
                self.shared_data.value += 1
                print('value:', str(self.shared_data.value), ' from ', self.name)

    def stop(self):
        print('stopping ', self.name)
        self.running = False
        self.join(1)


shared_data = multiprocessing.Value('i', 0, lock=True)

my_process1 = MyProcess('Process 1', shared_data)
my_process1.daemon = True
my_process2 = MyProcess('Process 2', shared_data)
my_process2.daemon = True

my_process1.start()
my_process2.start()

# python 3
input("Press Enter to stop...")

# python 2
#raw_input("Press Enter to stop...")

my_process1.stop()
my_process2.stop()

