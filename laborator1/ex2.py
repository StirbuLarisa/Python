def count_vowels(string):

    vowels = set("aeiouAEIOU")
    vowel_count = 0

    for i in string:
        if i in vowels:
            vowel_count += 1

    return vowel_count


if __name__ == '__main__':
    string = input("text: ")
    result = count_vowels(string)
    print(f"are {result} vocale")
