from dataclasses import dataclass
from typing import Dict, List, Set, Tuple
from fractions import Fraction


n = int(input())


@dataclass
class Dice:
    fraction_dict: Dict[int, Fraction]
    fraction_items: List[Tuple[int, Fraction]]
    key_set: Set[int]
    count_len: int
    dice_len: int


dice_list: List[Dice] = []

for i in range(n):
    ka_list = list(map(int, input().split()))
    k = ka_list.pop(0)
    count_len = 0
    count_dict: Dict[int, int] = {}
    for a in ka_list:
        get_count = count_dict.get(a, None)
        if get_count == None:
            count_dict[a] = 1
            count_len = count_len + 1
        else:
            count_dict[a] = get_count + 1
    fraction_items: List[Tuple[int, Fraction]] = []
    fraction_dict: Dict[int, Fraction] = {}
    dice_len = len(ka_list)
    key_set = set()
    for k, v in count_dict.items():
        fraction_value = Fraction(v, dice_len)
        fraction_items.append([k, fraction_value])
        fraction_dict[k] = fraction_value
        key_set.add(k)

    dice_list.append(
        Dice(
            fraction_dict=fraction_dict,
            fraction_items=fraction_items,
            count_len=count_len,
            dice_len=len(ka_list),
            key_set=key_set,
        )
    )

result_fraction = Fraction(0)
for i in range(n - 1):
    dice1 = dice_list[i]
    for j in range(i + 1, n):
        temp_result = Fraction(0)
        dice2 = dice_list[j]
        min_dice = dice2 if dice1.count_len > dice2.count_len else dice1
        max_dice = dice1 if dice1.count_len > dice2.count_len else dice2

        for k in min_dice.key_set.intersection(max_dice.key_set):
            min_dice_fraction = min_dice.fraction_dict.get(k)
            max_dice_fraction = max_dice.fraction_dict.get(k)
            temp_result2 = min_dice_fraction * max_dice_fraction
            temp_result = temp_result + temp_result2
        if temp_result > result_fraction:
            result_fraction = temp_result

print(float(result_fraction))
