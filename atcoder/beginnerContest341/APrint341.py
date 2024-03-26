n = int(input())

loop_count = n * 2 + 1

result = ""
for i in range(loop_count):
    if i % 2 == 0:
        result = result + "1"
    else:
        result = result + "0"

print(result)
