from dataclasses import dataclass
from typing import Dict

n, m = map(int, input().split())


@dataclass
class CellIndex:
    max_b_index: int
    max_w_index: int


x_dict: Dict[int, CellIndex] = {}
y_dict: Dict[int, CellIndex] = {}

result = "Yes"
for i in range(m):
    xyc_list = list(input().split())
    x = int(xyc_list[0])
    y = int(xyc_list[1])
    color = xyc_list[2]
    x_cell_index = x_dict.get(x, None)
    y_cell_index = y_dict.get(y, None)
    # xの判定
    max_b_index = None
    if x_cell_index != None:
        max_b_index = x_cell_index.max_b_index
    elif y_cell_index != None:
        max_b_index = y
    if max_b_index == None:
        if color == "B":
            new_x_cell_index = CellIndex(y, -1)
        else:
            new_x_cell_index = CellIndex(-1, y)
        x_dict[x] = new_x_cell_index
    else:
        if color == "B":
            if max_b_index < y:
                result = "No"
                break
            else:
                if max_b_index < y:
                    new_x_cell_index = CellIndex(y, x_cell_index.max_w_index)
                    x_dict[x] = new_x_cell_index
        else:
            if max_b_index > y:
                result = "No"
                break
            else:
                if max_b_index < y:
                    new_x_cell_index = CellIndex(x_cell_index.max_b_index, y)
                    x_dict[x] = new_x_cell_index
    # yの判定
    max_b_index = None
    if y_cell_index != None:
        max_b_index = y_cell_index.max_b_index
    elif x_cell_index != None:
        max_b_index = x
    if max_b_index == None:
        if color == "B":
            new_y_cell_index = CellIndex(x, -1)
        else:
            new_y_cell_index = CellIndex(-1, x)
        y_dict[y] = new_y_cell_index
    else:
        if color == "B":
            if max_b_index < x:
                result = "No"
                break
            else:
                if max_b_index < x:
                    new_y_cell_index = CellIndex(x, y_cell_index.max_w_index)
                    y_dict[y] = new_y_cell_index
        else:
            if max_b_index > x:
                result = "No"
                break
            else:
                if max_b_index < x:
                    new_y_cell_index = CellIndex(y_cell_index.max_b_index, x)
                    y_dict[y] = new_y_cell_index

print(result)
