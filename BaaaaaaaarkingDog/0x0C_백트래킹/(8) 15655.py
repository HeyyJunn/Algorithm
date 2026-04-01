import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = list(map(int, input().split()))
board.sort()

start = 0
used = [False] * (N + 1)
path = []

def backtrack(start):
  if len(path) == M:
    print(* path)
    return
  
  for x in range(start, N):
    if used[x] == True: continue

    used[x] = True
    path.append(board[x])

    backtrack(x + 1)

    used[x] = False
    path.pop()

backtrack(start)