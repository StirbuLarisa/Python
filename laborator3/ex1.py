
def operations_on_sets (list1, list2):
    a = set(list1)
    b = set(list2)

    intersection = a.intersection(b)
    union = a.union(b)
    diff_a_b = a.difference(b)
    diff_b_a = b.difference(a)

    result = [intersection,union,diff_a_b,diff_b_a]

    return result

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
result = operations_on_sets(a, b)
print(result)