# ch11_09
# concurrent.futures
# ProcessPoolExecutor

import multiprocessing
import concurrent.futures
import random
import time
import datetime


def perform(q, a, b, c):
    rand_val = random.uniform(0, 2)
    res = a * b * 10 - c * 2
    time.sleep(rand_val)

    q.put(res)


t1 = datetime.datetime.now()
m = multiprocessing.Manager()
q = m.Queue()
with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    for i in range(1, 15):
        val_a = random.randint(1, 10)
        val_b = random.randint(1, 10)
        val_c = random.randint(1, 10)
        executor.submit(perform, q, val_a, val_b, val_c)

print('Print results')
t2 = datetime.datetime.now()
while not q.empty():
    print(q.get())

t = t2 - t1
print('total time:', str(t.total_seconds()), 'seconds')
