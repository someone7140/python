n, r = map(int, input().split())

rating = r
for i in range(n):
    d, a = map(int, input().split())
    if d == 1:
        if rating >= 1600 and rating <= 2799:
            rating = rating + a
    else:
        if rating >= 1200 and rating <= 2399:
            rating = rating + a

print(rating)
