import sys

data = sys.stdin.read().split()
n = int(data[0])
stack = list(map(int, data[1:1+n]))

# 5 6 9 5 4 3
# 0 1 2 3 4 5

temp = []
out = []
idx = 1
for x in stack:
  while temp and temp[-1][1] < x:
    temp.pop()
    
  if temp and temp[-1][1] > x:
    # temp.append((temp[-1][0], x))
    out.append(temp[-1][0])
  else:
    out.append("0")
  
  temp.append((str(idx), x))
  idx += 1

print(" ".join(out))





