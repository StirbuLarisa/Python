def count_unique_and_duplicate_elements(lst):
    unique_elements = set()
    duplicate_elements = set()

    for item in lst:
        if item in unique_elements:
            duplicate_elements.add(item)
        else:
            unique_elements.add(item)

    return len(unique_elements), len(duplicate_elements)


my_list = [1, 2, 2, 3, 3, 4, 5, 5, 6]
result = count_unique_and_duplicate_elements(my_list)
print(result)