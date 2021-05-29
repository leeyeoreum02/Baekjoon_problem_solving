# https://www.acmicpc.net/problem/16170

# answer

from datetime import datetime

now = datetime.utcnow()

print(now.year, now.month, now.day, sep='\n')