n_list = list(input())

count1 = 0
count2 = 0
count3 = 0

for n in n_list:
    if n == "1":
        count1 = count1 + 1
    if n == "2":
        count2 = count2 + 1
    if n == "3":
        count3 = count3 + 1

if count1 == 1 and count2 == 2 and count3 == 3:
    print("Yes")
else:
    print("No")
