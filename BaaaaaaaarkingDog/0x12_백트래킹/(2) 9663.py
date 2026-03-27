import sys
input = sys.stdin.readline

N = int(input())
row = [0] * N
ans = 0

def is_promissing(x):
  # (x, i)
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
      return False
    
  return True

def func1(x):
  global ans
  if x == N:
    ans += 1
    return
  else:
    for i in range(N):
      row[x] = i # (x, i)

      if is_promissing(x): 
        func1(x + 1) # 다음행으로 이동
    
  return

func1(0)
print(ans)