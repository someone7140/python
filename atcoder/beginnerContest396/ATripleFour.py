n = int(input())
a_list = list(map(int, input().split()))

before = None
count = 0
result = "No"
for a in a_list:
    if before == None:
        count = count + 1
        before = a
    elif before == a:
        count = count + 1
        before = a
        if count >= 3:
            result = "Yes"
            break
    else:
        before = a
        count = 1

print(result)
