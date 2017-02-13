# ch11_01.py
# simple threading

import time
import threading

global running


def perform():
    global running

    counter = 0
    running = True
    while running:
        print('counter:', str(counter))
        time.sleep(2)
        counter += 1


my_thread = threading.Thread(target=perform)
my_thread.setDaemon(True)
my_thread.start()

# python 3
input("Press Enter to stop...")

# python 2
#raw_input("Press Enter to stop...")

running = False
my_thread.join(2)

