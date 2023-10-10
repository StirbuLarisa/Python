
def extract_number(text):
    is_num = False
    result = ""
    for i in text:
        if i.isdigit():
            result += i
            is_num = True
        elif is_num == True:
            break

    if result:
        return int(result)
    else:
        return "none"

if __name__ == '__main__':

    text = input("text: ");
    result = extract_number(text);
    print(result)