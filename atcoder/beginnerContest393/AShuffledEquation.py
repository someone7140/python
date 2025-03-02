s_list = list(input().split())

if s_list[0] == "sick" and s_list[1] == "sick":
    print("1")
elif s_list[0] == "sick" and s_list[1] == "fine":
    print("2")
elif s_list[0] == "fine" and s_list[1] == "sick":
    print("3")
else:
    print("4")
