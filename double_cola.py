def who_is_next(names, r):
    i = 1
    while (len(names) * i < r):
        r -= len(names) * i
        i *= 2
    return names[(r - 1) // i]



names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

print(who_is_next(['a', 'b', 'c'], 10), 'a')
print(who_is_next(names, 1), "Sheldon")
print(who_is_next(names, 52), "Penny")
print(who_is_next(names, 1802), "Penny")
print(who_is_next(names, 7230702951), "Leonard")
