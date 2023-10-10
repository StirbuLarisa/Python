def count_bits(number):
    #'0b' prefix
    binary_string = bin(number)[2:]

    count = binary_string.count('1')
    return count

if __name__ == '__main__':

    number = int(input("nr: "))
    result = count_bits(number)

    print(f"{number} are {result} biti cu valoarea 1")


