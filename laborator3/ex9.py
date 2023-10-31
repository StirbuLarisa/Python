def count_matching_args(*args, **kwargs): #Arbitrary Positional Arguments  &&  Arbitrary Keyword Arguments
    arg_set = set(args)
    kwarg_values = set(kwargs.values())

    count = 0
    for arg in arg_set:
        if arg in kwarg_values:
            count += 1

    return count

result = count_matching_args(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)