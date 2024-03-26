n = int(input())
aList = map(int, input().split())

initialCount = 0
sum = 0

for a in aList:
    sum = sum + a
    if sum < 0:
        initialCount = initialCount - sum
        sum = 0

print(sum)
