def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 7, 8, 9, 10))
