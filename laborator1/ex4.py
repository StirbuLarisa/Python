
def camel_to_snake(text):
    result = ""

    for i in text:
        if i.isupper():
            result = result + "_" + i.lower()
        else:
            result += i

    if result[0] == "_":
        result = result[1:]

    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    text = input("camel case text: ")

    result = camel_to_snake(text)

    print(f"snake case: {result}")


