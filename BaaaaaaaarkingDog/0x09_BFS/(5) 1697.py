import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
if N == K:
  print(0)
  sys.exit()
# print(f"debug: {N, K}")
dq = deque()

visited = [0] * 100_001

dq.append((N, 0))
visited[N] = 1

while dq:
  cur_N, cur_Time = dq.popleft()
  # print(f"cur_N: {cur_N}, cur_Time: {cur_Time}")
  dq_list = [cur_N + 1, cur_N - 1, 2 * cur_N]

  for d in range(3):
    next_N = dq_list[d]
  
    if next_N < 0 or next_N > 100_000:
      continue
    if visited[next_N] != 0:
      continue
    if next_N == K:
      print(cur_Time + 1)
      sys.exit()

    visited[next_N] = 1
    dq.append((next_N, cur_Time + 1))

  
  
