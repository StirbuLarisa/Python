def spiral_order(matrix):

    result = ""
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        # de la stanga la dreapta
        for col in range(left, right + 1):
            result += matrix[top][col]
        top += 1

        # de sus in jos
        for row in range(top, bottom + 1):
            result += matrix[row][right]
        right -= 1

        # daca mai sunt coloane sau randuri
        if top <= bottom:
            # de la dreapta la stanga
            for col in range(right, left - 1, -1):
                result += matrix[bottom][col]
            bottom -= 1

        if left <= right:
            # de jos in sus
            for row in range(bottom, top - 1, -1):
                result += matrix[row][left]
            left += 1

    return result


if __name__ == '__main__':
    matrix = [
        ["f", "i", "r", "s"],
        ["n", "_", "l", "t"],
        ["o", "b", "a", "_"],
        ["h", "t", "y", "p"]
    ]

    matrix1 = [
        ["1", "2", "3"],
        ["10", "11", "4"],
        ["9", "12", "5"],
        ["8", "7", "6"]
    ]

    string = spiral_order(matrix)
    string1 = spiral_order(matrix1)
    print(string)
    print(string1)
