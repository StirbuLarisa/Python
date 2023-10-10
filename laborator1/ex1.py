import math

def gcd(num):

    result = num[0];

    for n in num[1:]:
        result = math.gcd(result, n)

    return result


if __name__ == '__main__':

    num = []

    while len(num) < 2:
        list_of_numbers = input("numere:")
        num = list(map(int,list_of_numbers.split()))

        if len(num) < 2:
            print("trebuie minim 2 numere")
        else:
            result = gcd(num)
            print(f"{result}")
