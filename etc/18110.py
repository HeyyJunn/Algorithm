import sys
import math
data = sys.stdin.read().split()

n = int(data[0])
rates = sorted(map(int, data[1:1+n]))


count_ratio = int((n * 0.15) + 0.5)

if n == 0:
  print(0)
elif count_ratio != 0:
  trimmed_list = rates[count_ratio:n-count_ratio]
  result = int(sum(trimmed_list) / len(trimmed_list) + 0.5)
  print(result)
else:
  trimmed_list = rates[:]
  result = int(sum(trimmed_list) / len(trimmed_list) + 0.5)
  print(result)

