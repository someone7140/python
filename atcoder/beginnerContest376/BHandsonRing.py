n, q = map(int, input().split())
l = 1
r = 2

result = 0

for i in range(q):
    h, t_str = input().split()
    t = int(t_str)

    if h == "L":
        if t == l:
            continue

        # 右回りが可能か
        if t < l:
            if r > l or r < t:
                pass
            else:
                result = result + (n - l) + t
        else:
            if r > t or r < l:
                result = result + (t - l)

        # 左回りが可能か
        if t > l:
            if r < l or r > t:
                pass
            else:
                result = result + l + (n - t)
        else:
            if r < t or l < r:
                result = result + (l - t)
        l = t
    else:
        if t == r:
            continue
        # 右回りが可能か
        if t < r:
            if l > r or l < t:
                pass
            else:
                result = result + (n - r) + t
        else:
            if l > t or l < r:
                result = result + (t - r)

        # 左回りが可能か
        if t > r:
            if l < r or l > t:
                pass
            else:
                result = result + r + (n - t)
        else:
            if l < t or r < l:
                result = result + (r - t)
        r = t

print(result)
