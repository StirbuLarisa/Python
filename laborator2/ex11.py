def order_tuples(lst):
    def get_third_character(t):
        return t[1][2]

    return sorted(lst, key=get_third_character)

tuples = [('abc', 'bcd'), ('abc', 'zza')]

result = order_tuples(tuples)
print(result)