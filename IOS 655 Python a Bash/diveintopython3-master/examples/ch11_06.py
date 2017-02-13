# ch11_06.py
# simple multiprocessing

import time
import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing. Process.__init__(self)
        self.running = False

    def run(self):
        counter = 0
        self.running = True
        while self.running:
            print('counter:', str(counter))
            time.sleep(2)
            counter += 1

    def stop(self):
        print('stopping process...')
        self.running = False
        self.join(1)


my_process = MyProcess()
my_process.daemon = True
my_process.start()

# python 3
input("Press Enter to stop...")

# python 2
#raw_input("Press Enter to stop...")

my_process.stop()

