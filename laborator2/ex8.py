def generate_character_lists(x=1, strings=[], flag=True):
    result = []
    for string in strings:
        char_set = set()
        for char in string:
            if (ord(char) % x == 0) == flag:
                char_set.add(char)
        result.append(list(char_set))
    return result

x = 2
strings = ["test", "hello", "lab002"]
flag = False

result = generate_character_lists(x, strings, flag)
print(result)

result = generate_character_lists(x, strings, True)
print(result)