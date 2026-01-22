import sys

input = sys.stdin.readline

n = int(input())
queue = []
out = []
head = 0

for _ in range(n):
  cmd = input().split()

  if cmd[0] == "push":
    queue.append(cmd[1])
  elif cmd[0] == "pop":
    if head == len(queue):
      # raise IndexError
      out.append("-1")
    else:
      out.append(queue[head])
      head += 1
  elif cmd[0] == "size":
    out.append(str(len(queue) - head))
  elif cmd[0] == "empty":
    out.append("1" if head == len(queue) else "0")
  elif cmd[0] == "front":
    out.append(queue[head] if head != len(queue) else "-1")
  elif cmd[0] == "back":
    out.append(queue[-1] if head != len(queue) else "-1")

print("\n".join(out))
