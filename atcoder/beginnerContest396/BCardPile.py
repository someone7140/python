from typing import List


q = int(input())
card_list: List[str] = []
result_list: List[str] = []

for i in range(q):
    q = list(input().split())
    if q[0] == "1":
        card_list.append(q[1])
    else:
        if len(card_list) == 0:
            result_list.append("0")
        else:
            popped_card = card_list.pop(-1)
            result_list.append(popped_card)

print("\n".join(result_list))
