def find_items(x, *lists):  # *pt numar variabil de argumente, ca fiecare lista sa fie tratata individual
    occurrences = {}
    for lst in lists:
        for item in lst:
            if item in occurrences:
                occurrences[item] += 1
            else:
                occurrences[item] = 1
    result=[]
    for item, count in occurrences.items():
        if count == x:
            result.append(item)

    return result

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x = 2

print(find_items(x,list1,list2,list3,list4))