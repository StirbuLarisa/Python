
def count_words(text):

    words = text.split()
    word_count = len(words)

    return word_count

if __name__ == '__main__':
    text = input("text: ")

    result = count_words(text)

    print(f"textul are {result} cuvinte")
