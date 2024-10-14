s = input()
t = input()

nagai = s if len(s) > len(t) else t
mijikai = t if len(s) > len(t) else s

loop = len(mijikai)
result = 0 if nagai == mijikai else loop + 1

for i in range(loop):
    if nagai[i] != mijikai[i]:
        result = i + 1
        break

print(result)
