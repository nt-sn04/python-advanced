def get_sum(a: int, b: int, c: int = 3, *args, **kwargs):
    print(a, b)
    print(c)
    print(args)
    print(kwargs)
    print(type(kwargs))


nums = [1, 2, 3]
data = {'d': 4, 'f': 9} # -> d=4, f=9

get_sum(1, 2, 3, *nums, **data)
