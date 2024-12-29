from typing import Dict, List


n = int(input())
h_list = list(map(int, input().split()))

takasa_index_dict: Dict[int, List[int]] = {}
for i in range(n):
    h = h_list[i]
    index_list = takasa_index_dict.get(h)
    if index_list == None:
        takasa_index_dict[h] = [i]
    else:
        takasa_index_dict[h].append(i)

result = 1

for k in takasa_index_dict.keys():
    index_list = takasa_index_dict.get(k)
    len_list = len(index_list)
    if len_list > 1:
        if len_list > 2:
            for i in range(len_list - 2):
                temp_result = 2
                index_1 = index_list[i]
                temp_next_i = i + 1
                temp_next_index_3 = i + 2
                index_2 = index_list[temp_next_i]
                index_3 = index_list[temp_next_index_3]
                while temp_next_i < len_list - 1:
                    sabun_1 = index_2 - index_1
                    sabun_2 = index_3 - index_2
                    if sabun_1 == sabun_2:
                        temp_result = temp_result + 1
                        index_1 = index_2
                        index_2 = index_3
                        if temp_next_index_3 == len_list - 1:
                            if result < temp_result:
                                result = temp_result
                            break
                        temp_next_index_3 = temp_next_index_3 + 1
                        index_3 = index_list[temp_next_index_3]
                    else:
                        if sabun_1 < sabun_2:
                            # 最初に戻る
                            index_1 = index_list[i]
                            temp_next_i = temp_next_i + 1
                            temp_next_index_3 = temp_next_i + 1
                            if temp_next_index_3 == len_list:
                                if result < temp_result:
                                    result = temp_result
                                break
                            index_2 = index_list[temp_next_i]
                            index_3 = index_list[temp_next_index_3]
                            if result < temp_result:
                                result = temp_result
                            temp_result = 2
                        else:
                            if temp_next_index_3 < len_list - 1:
                                temp_next_index_3 = temp_next_index_3 + 1
                                index_3 = index_list[temp_next_index_3]
                            else:
                                # 最初に戻る
                                index_1 = index_list[i]
                                temp_next_i = temp_next_i + 1
                                temp_next_index_3 = temp_next_i + 1
                                if temp_next_index_3 == len_list:
                                    if result < temp_result:
                                        result = temp_result
                                    break
                                index_2 = index_list[temp_next_i]
                                index_3 = index_list[temp_next_index_3]
                                if result < temp_result:
                                    result = temp_result
                                temp_result = 2

print(result)
