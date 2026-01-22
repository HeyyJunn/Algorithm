import sys
from collections import deque

input = sys.stdin.read
n = int(input())

arr = list(range(1, 1+n))
dq = deque(arr)

while len(dq) != 1:
  dq.popleft()
  x = dq.popleft()
  dq.append(x)

print(dq[0])