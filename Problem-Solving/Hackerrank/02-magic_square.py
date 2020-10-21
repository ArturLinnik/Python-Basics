
# Given a 3x3 matrix, convert it into a magic square with the minimum cost. The cost of every changed number is |a-b|.

def formingMagicSquare(s):
    
    pre = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]

    total_array = []

    for p in pre:
        total = 0
        for p_row, s_row in zip(p,s):
            for i, j in zip(p_row,s_row):
                if i != j:
                    # total += abs(i-j)
                    total += max([i, j]) - min([i, j])

        total_array.append(total)

    return min(total_array)

matrix = [[4,9,2],[3,5,7],[8,1,5]]

print(formingMagicSquare(matrix))

