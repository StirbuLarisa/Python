def find_palindromes(numbers):
    palindromes = []
    for num in numbers:
        if str(num) == str(num)[::-1]:
            palindromes.append(num)

    num_palindromes = len(palindromes)

    if palindromes:
        max_palindrome = max(palindromes)
    else:
        max_palindrome = "no palindromes"

    return (num_palindromes, max_palindrome)

numbers = [123, 121, 345, 454, 678, 898]
result = find_palindromes(numbers)
print(result)

numbers = [123, 456]
result = find_palindromes(numbers)
print(result)