n = int(input())

bean_dict = {}

for i in range(n):
    oishisa, num = map(int, input().split())
    saisyou = bean_dict.get(num, -1)

    if saisyou == -1 or oishisa < saisyou:
        bean_dict[num] = oishisa

result = -1

for v in bean_dict.values():
    if result < v:
        result = v

print(result)
