import sys
import math
input = sys.stdin.readline

N,M = map(int, input().split())
path = []
used = [False] * (N + 1) 

def backtrack(start):
  if len(path) == M:
    print(*path)
    return
  
  for num in range(start, N + 1):
    if used[num] == True: continue
    
    used[num] = True
    path.append(num)

    backtrack(num + 1)

    used[num] = False
    path.pop()

backtrack(1)