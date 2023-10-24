def find_obstructed_seats(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    obstructed_seats = []

    for i in range(rows):
        for j in range(cols):
            current_height = matrix[i][j]
            obstructed = False

            for k in range(i - 1, -1, -1):
                if matrix[k][j] >= current_height:
                    obstructed = True
                    break

            if obstructed:
                obstructed_seats.append((i, j))

    return obstructed_seats

matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]]

result = find_obstructed_seats(matrix)
print(result)