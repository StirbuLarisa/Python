def zip_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    result = []

    for i in range(max_length):
        items = []
        for lst in lists:
            if i < len(lst):
                items.append(lst[i])
            else:
                items.append(None)
        result.append(tuple(items))

    return result

list1 = [1, 2, 3, 8]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

print(zip_lists(list1, list2, list3))