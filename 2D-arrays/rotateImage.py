def rotate(matrix):
    n = len(matrix)


    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    for i in range(n):
        matrix[i] = matrix[i][::-1]


n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


rotate(matrix)


for row in matrix:
    print(*row)
