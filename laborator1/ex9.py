
def most_common_letter(string):

    string = string.lower()
    #dictionar
    letter_count = {}

    for i in string:
        if i.isalpha():
            if i in letter_count:
                letter_count[i] += 1
            else:
                letter_count[i] = 1

    most_common = max(letter_count, key=letter_count.get)

    return most_common, letter_count[most_common]

if __name__ == '__main__':

    string = input("text: ")

    letter, occurence = most_common_letter(string)

    print(f"{letter} apare de {occurence} ori")