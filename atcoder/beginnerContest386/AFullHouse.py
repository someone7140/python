from typing import Dict


abcd_list = list(map(int, input().split()))
card_dict: Dict[int, int] = {}

for card in abcd_list:
    count = card_dict.get(card, 0)
    card_dict[card] = count + 1

one_count = 0
two_count = 0

index = 0
for card in card_dict.keys():
    if index == 0:
        one_count = card_dict[card]
    else:
        two_count = card_dict[card]
    index = index + 1

if one_count == 2 and two_count == 2:
    print("Yes")
elif one_count == 3 and two_count == 1:
    print("Yes")
elif one_count == 1 and two_count == 3:
    print("Yes")
else:
    print("No")
