s = input()
sLen = len(s)
sList = list(s)
sSet = set()

for i in range(sLen):
    temp_result = sList[i]
    sSet.add(temp_result)
    for j in range(i + 1, sLen):
        temp_result = temp_result + sList[j]
        sSet.add(temp_result)

print(len(sSet))
