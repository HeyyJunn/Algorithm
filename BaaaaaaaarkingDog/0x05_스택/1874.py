import sys

data = sys.stdin.read().split()
n = int(data[0])
seq = list(map(int, data[1:1+n]))

stack = []
cnt = 1
out = []
possible = True 

for x in seq:
  while cnt <= x:
    stack.append(cnt)
    cnt += 1
    out.append("+")
  
  if stack and stack[-1] == x:
    stack.pop()
    out.append("-")
  else:
    possible = False
    break

if not possible:
  print("NO")
else:
  print("\n".join(out))




