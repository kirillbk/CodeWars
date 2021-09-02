# Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue.
# The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue.
# Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.
# For example, Penny drinks the third can of cola and the queue will look like this:
# Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny

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
