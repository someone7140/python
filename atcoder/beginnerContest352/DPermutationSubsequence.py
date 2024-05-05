from collections import deque
from dataclasses import dataclass
from typing import List
import heapq


@dataclass
class PWithIndex:
    p: int
    index: int


n, k = map(int, input().split())
p_list = list(map(int, input().split()))
p_width_index_list: List[PWithIndex] = []

for i, p in enumerate(p_list):
    p_width_index_list.append(PWithIndex(p, i))

p_width_index_list.sort(key=lambda x: x.p)

min_heap: List[int] = []
max_heap: List[int] = []
heapq.heapify(min_heap)
heapq.heapify(max_heap)
already_delete_index = [0] * n
d = deque()
deque_len = 0
result = 999999999999999

if k == n:
    result = n - 1
else:
    for p_width_index in p_width_index_list:
        if deque_len < k:
            d.append(p_width_index.index)
            heapq.heappush(min_heap, p_width_index.index)
            heapq.heappush(max_heap, -p_width_index.index)
            deque_len = deque_len + 1
            if deque_len == k:
                temp_result = -min_heap[0] - max_heap[0]
                if temp_result < result:
                    result = temp_result
        else:
            deleted = d.popleft()
            already_delete_index[deleted] = 1
            d.append(p_width_index.index)

            if k == 1:
                heapq.heappop(min_heap)
                heapq.heappop(max_heap)
            else:
                if min_heap[0] == deleted:
                    while already_delete_index[min_heap[0]] != 0:
                        heapq.heappop(min_heap)
                if max_heap[0] == -deleted:
                    while already_delete_index[-max_heap[0]] != 0:
                        heapq.heappop(max_heap)

            heapq.heappush(min_heap, p_width_index.index)
            heapq.heappush(max_heap, -p_width_index.index)
            temp_result = -min_heap[0] - max_heap[0]
            if temp_result < result:
                result = temp_result

print(result)
