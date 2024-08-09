matrix = [[2, 3, 4],[5, 7, 8],[9, 1, 6]]
diagonal_elements = [matrix[i][i] for i in range(len(matrix)) if matrix[i][i] % 2 != 0]
print("the answer is:",diagonal_elements)
