import sys
from collections import deque
input = sys.stdin.readline

cmd = input().split() # N: 큐의 크기 M: 뽑아내려고 하는 수의 개수
index = list(map(int, input().split())) # 뽑아 내려고 하는 수들의 index
# n, m = cmd[0], cmd[1] ** str 임 **
n, m = map(int, cmd)
dq = deque(list(range(1, n+1)))

# print(f"debug: {n} {m}")

cnt = 0

for i in range(m):
  idx = dq.index(index[i])
  left, right = idx, len(dq) - idx
  
  if left <= right:
    while dq[0] != index[i]:
      dq.rotate(-1)
      cnt += 1
    dq.popleft()
  else:
    while dq[-1] != index[i]:
      dq.rotate(1)
      cnt += 1
    dq.rotate(1)
    cnt += 1
    dq.popleft()

print(cnt)

    
    
    
    
    



  


  
