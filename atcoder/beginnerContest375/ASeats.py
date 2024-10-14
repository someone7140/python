n = int(input())
s = input()

index = 0
result = 0
for moji in s:
    if index >= n - 2:
        break
    judge = moji + s[index + 1] + s[index + 2]
    if judge == "#.#":
        result = result + 1
    index = index + 1

print(result)
