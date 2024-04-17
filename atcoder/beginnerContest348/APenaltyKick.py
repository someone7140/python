n = int(input())

result = ""

for i in range(n):
    count = i + 1
    if count % 3 == 0:
        result = result + "x"
    else:
        result = result + "o"

print(result)
