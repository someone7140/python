from dataclasses import dataclass, field
from typing import List


n, m = map(int, input().split())

machi_set = set()


@dataclass
class Douro:
    start: int
    end: int
    cost: int


list_douro: List[Douro] = []

for i in range(m):
    a, b, c = map(int, input().split())
    machi_set.add(a)
    machi_set.add(b)
    list_douro.append(Douro(a, b, c))

machi_len = len(machi_set)
result = -1


def saiki_douro(
    index: int,
    tuuka_count_dict: dict,
    cost: int,
    tuuka_total_count: int,
    tuuka_two_count: int,
):
    global result
    global list_douro

    if tuuka_total_count == machi_len and tuuka_two_count == machi_len - 2:
        if result < cost:
            result = cost
    elif index > m - 1:
        return
    else:
        # そのまま次へ
        saiki_douro(
            index + 1, tuuka_count_dict.copy(), cost, tuuka_total_count, tuuka_two_count
        )
        # 道路を通れるパターン
        douro = list_douro[index]
        if (
            tuuka_count_dict.get(douro.start, 0) < 2
            and tuuka_count_dict.get(douro.end, 0) < 2
        ):
            new_tuuka_total_count = tuuka_total_count
            new_tuuka_two_count = tuuka_two_count
            new_dict = tuuka_count_dict.copy()

            if tuuka_count_dict.get(douro.start, 0) == 0:
                new_tuuka_total_count = new_tuuka_total_count + 1
            new_dict[douro.start] = tuuka_count_dict.get(douro.start, 0) + 1
            if new_dict[douro.start] == 2:
                new_tuuka_two_count = new_tuuka_two_count + 1

            if tuuka_count_dict.get(douro.end, 0) == 0:
                new_tuuka_total_count = new_tuuka_total_count + 1
            new_dict[douro.end] = tuuka_count_dict.get(douro.end, 0) + 1
            if new_dict[douro.end] == 2:
                new_tuuka_two_count = new_tuuka_two_count + 1

            new_cost = cost + douro.cost
            saiki_douro(
                index + 1,
                new_dict,
                new_cost,
                new_tuuka_total_count,
                new_tuuka_two_count,
            )


saiki_douro(0, {}, 0, 0, 0)
print(result)
