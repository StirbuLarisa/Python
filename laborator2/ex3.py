def operations(a, b):
    a_set = set(a)
    b_set = set(b)

    intersection = list(a_set & b_set)
    union = list(a_set | b_set)
    difference_a_b = list(a_set - b_set)
    difference_b_a = list(b_set - a_set)

    return intersection, union, difference_a_b, difference_b_a

a = [1, 2, 3, 4, 5, 'a', 'b']
b = [4, 5, 6, 7, 8, 'b', 'c']
intersection, union, difference_a_b, difference_b_a = operations(a, b)

print("intersectie:", intersection)
print("reuniune:", union)
print("diferenta A - B:", difference_a_b)
print("diferenta B - A:", difference_b_a)