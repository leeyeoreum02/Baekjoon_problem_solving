# https://www.acmicpc.net/problem/10699

# answer

import time

now = time.localtime()

print('{}-{:02d}-{:02d}'.format(now.tm_year, now.tm_mon, now.tm_mday))