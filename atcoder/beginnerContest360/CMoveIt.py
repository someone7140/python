from queue import PriorityQueue
from typing import Dict


n = int(input())
a_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

a_dict: Dict[int, PriorityQueue] = {}
result = 0
for i in range(n):
    queue = a_dict.get(a_list[i], PriorityQueue())
    queue.put(w_list[i])
    a_dict[a_list[i]] = queue

for k in a_dict:
    queue = a_dict[k]
    size = queue.qsize()
    for i in range(size - 1):
        result = result + queue.get()

print(result)
