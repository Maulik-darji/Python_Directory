from functools import reduce

n = int(input("Enter Number to Find Fact "))
result = reduce(lambda x, y: x*y, range(1, n+1), 1)
print(result)


# reduce(function iterable, initializer)