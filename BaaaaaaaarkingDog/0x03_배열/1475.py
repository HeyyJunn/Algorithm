import sys
input = sys.stdin.readline

s = input().strip()  

num_list = [0] * 9

for i in s:
  idx = int(i)
  if idx == 9: num_list[6] += 1
  else: num_list[idx] += 1

num_list[6] = (num_list[6] + 1) // 2
print(max(num_list))