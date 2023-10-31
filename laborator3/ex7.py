def set_operations(*sets):
    result = {}
    set_list = list(sets)

    for i in range(len(set_list)):
        for j in range(i + 1, len(set_list)):
            set1 = set_list[i]
            set2 = set_list[j]
            key = f"{set1} | {set2}"
            result[key] = set1.union(set2)
            key = f"{set1} & {set2}"
            result[key] = set1.intersection(set2)
            key = f"{set1} - {set2}"
            result[key] = set1.difference(set2)
            key = f"{set2} - {set1}"
            result[key] = set2.difference(set1)

    return result

set1 = {1, 2}
set2 = {2, 3}
set3 = {1,2,3,4}
result = set_operations(set1, set2,set3)
for key, value in result.items():
    print(f"{key}: {value}")
