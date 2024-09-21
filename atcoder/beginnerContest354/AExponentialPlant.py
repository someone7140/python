h = int(input())
result = 1
hSyokubutu = 1
keisuu = 1

while h >= hSyokubutu:
    keisuu = keisuu * 2
    hSyokubutu = hSyokubutu + keisuu
    result = result + 1

print(result)
