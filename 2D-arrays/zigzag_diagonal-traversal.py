def diagonalOrder(matrix, ROW, COL):
    for line in range(1, (ROW + COL)):
        start_col = max(0, line - ROW)
        count = min(line, (COL - start_col), ROW)
        for j in range(0, count):
            print(matrix[min(ROW, line) - j - 1][start_col + j], end="\t")
        print()

def printMatrix(matrix, ROW, COL):
    for i in range(0, ROW):
        for j in range(0, COL):
            print(matrix[i][j], end="\t")
        print()

# Example
if __name__ == "__main__":
    ROW = int(input())
    COL = int(input())
    matrix = []
    for _ in range(ROW):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    print("Given matrix is ")
    printMatrix(matrix, ROW, COL)

    print("\nDiagonal printing of matrix is ")
    diagonalOrder(matrix, ROW, COL)
