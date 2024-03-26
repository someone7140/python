n = int(input())

aList = list(map(int, input().split()))

for i in range(n - 1):
    s, t = map(int, input().split())
    wari = aList[i] // s
    aList[i] = aList[i] - s * wari
    aList[i + 1] = aList[i + 1] + t * wari

print(aList[n - 1])
