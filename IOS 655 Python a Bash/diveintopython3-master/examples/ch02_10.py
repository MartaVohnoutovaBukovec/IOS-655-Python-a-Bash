# ch02_10.py

import time

# get current time
now = time.time()  # utc
print(now)
# display readable current time
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(now)))
print(time.timezone)

