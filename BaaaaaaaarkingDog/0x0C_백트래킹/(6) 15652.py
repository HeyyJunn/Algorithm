# HARDHARDHARDHARDHARD 
import sys
input = sys.stdin.readline

start = 1
N, M = map(int, input().split())
path = [] # 현재까지의 경로
used = [False] * (N + 1) # 사용 여부

def backtrack(start):
  if len(path) == M:
    print(* path)
    return

  for x in range(start, N+1):
    path.append(x)
    backtrack(x)
    path.pop()

backtrack(start)