
def is_palindrome(number):

    return number == number[::-1]


if __name__ == '__main__':

   number = input("numar: ")

   if is_palindrome(number):
       print(f"{number} este palindrom")
   else:
       print(f"{number} nu este palindrom")

