def count_characters(text):
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

text = "Ana has apples."
result = count_characters(text)
print(result)