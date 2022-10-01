def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    # doesn't include middle element 2 times for od matrix
    # sum = 0
    # index_y = 0
    # for row in matrix:
    #     index_x = 0
    #     for el in row:
    #         if index_x == index_y or (index_x + index_y == len(matrix)-1):
    #             sum += el
    #         index_x += 1
    #     index_y += 1
    # return sum

    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
        sum += matrix[i][-1 - i]
    return sum