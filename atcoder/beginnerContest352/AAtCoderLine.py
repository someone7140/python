n, x, y, z = map(int, input().split())

result = "No"
temp = x
while temp != y:
    if x < y:
        temp = temp + 1
    else:
        temp = temp - 1

    if temp == z:
        result = "Yes"
        break

print(result)
