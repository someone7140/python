n = int(input())


base_n(num_10, n):
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return str_n[::-1]


if n == 1:
    print(0)
else:
    goshin = base_n(n - 1, 5)
    result = ""

    for moji in list(goshin):
        result = result + str(int(moji) * 2)

    print(result)
