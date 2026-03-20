import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = list(map(int, input().split()))
board_set = sorted(set(board))
board.sort()

used = [False] * N
path = []

def backtrack():
  if len(path) == M:
    print(* path)
    return
  
  prev = None

  for x in range(len(board)):
    if used[x] == True: continue
    if board[x] == prev: continue
    prev = board[x]
    used[x] = True
    path.append(board[x])
    backtrack()
    used[x] = False
    path.pop()

backtrack()