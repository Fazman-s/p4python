class Solution:
    def setZeroes(self, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    for i in range(COLS):
                        matrix[r][i] = "*" if matrix[r][i] else 0
                    for i in range(ROWS):
                        matrix[i][c] = "*" if matrix[i][c] else 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0

# Example
if __name__ == "__main__":
    solution = Solution()
    ROWS = int(input())
    COLS = int(input())
    matrix = []
    for _ in range(ROWS):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    solution.setZeroes(matrix)
    
    for r in range(ROWS):
        for c in range(COLS):
            print(matrix[r][c], end=" ")
        print()


'''
class Solution:
    def setZeroes(self, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in zero_rows:
            for c in range(COLS):
                matrix[r][c] = 0

        for c in zero_cols:
            for r in range(ROWS):
                matrix[r][c] = 0

# Example
if __name__ == "__main__":
    solution = Solution()
    ROWS = int(input())
    COLS = int(input())
    matrix = []
    for _ in range(ROWS):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    solution.setZeroes(matrix)
    
    for r in range(ROWS):
        for c in range(COLS):
            print(matrix[r][c], end=" ")
        print()
'''