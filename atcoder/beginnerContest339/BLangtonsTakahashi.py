h, w, n = map(int, input().split())
grid = [["."] * w for i in range(h)]

direction = "ue"


class Zahyou:
    w = 0
    h = 0


zahyou = Zahyou()


def susumu(syubetu: str, val: int):
    global zahyou
    global h
    global w
    if syubetu == "tate":
        if (zahyou.h + val) == h:
            zahyou.h = 0
        elif (zahyou.h + val) == -1:
            zahyou.h = h - 1
        else:
            zahyou.h = zahyou.h + val
    else:
        if (zahyou.w + val) == w:
            zahyou.w = 0
        elif (zahyou.w + val) == -1:
            zahyou.w = w - 1
        else:
            zahyou.w = zahyou.w + val


def operation():
    global grid
    global direction
    global zahyou

    if grid[zahyou.h][zahyou.w] == ".":
        grid[zahyou.h][zahyou.w] = "#"
        if direction == "ue":
            direction = "migi"
            susumu("yoko", 1)
        elif direction == "migi":
            direction = "shita"
            susumu("tate", 1)
        elif direction == "shita":
            direction = "hidari"
            susumu("yoko", -1)
        else:
            direction = "ue"
            susumu("tate", -1)
    else:
        grid[zahyou.h][zahyou.w] = "."
        if direction == "ue":
            direction = "hidari"
            susumu("yoko", -1)
        elif direction == "migi":
            direction = "ue"
            susumu("tate", -1)
        elif direction == "shita":
            direction = "migi"
            susumu("yoko", 1)
        else:
            direction = "shita"
            susumu("tate", 1)


for i in range(n):
    operation()

print("\n".join(list(map(lambda row: "".join(row), grid))))
