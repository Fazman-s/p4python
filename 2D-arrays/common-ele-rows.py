
def findCommon(mat):

    column = [N - 1] * M
    min_row = 0 

    while column[min_row] >= 0:
 
        for i in range(M):
            if mat[i][column[i]] < mat[min_row][column[min_row]]:
                min_row = i

        eq_count = 0 

        # Traverse current last column elements again to update it
        for i in range(M):
            if mat[i][column[i]] > mat[min_row][column[min_row]]:
                if column[i] == 0:
                    return -1
                column[i] -= 1  # Reduce last column index by 1
            else:
                eq_count += 1

        # If equal count becomes M, return the value
        if eq_count == M:
            return mat[min_row][column[min_row]]
    return -1

if __name__ == "__main__":
    M = int(input())
    N = int(input())
    mat = []
    for _ in range(M):
        row_values = list(map(int, input().strip().split()))
        mat.append(row_values)

    result = findCommon(mat)
    if result == -1:
        print("No common element")
    else:
        print("Common element is", result)

def findCommon(mat):

    column = [N - 1] * M
    min_row = 0 

    while column[min_row] >= 0:
 
        for i in range(M):
            if mat[i][column[i]] < mat[min_row][column[min_row]]:
                min_row = i

        eq_count = 0  # eq_count is the count of elements equal to the minimum in the current last column.

        for i in range(M):
            if mat[i][column[i]] > mat[min_row][column[min_row]]:
                if column[i] == 0:
                    return -1
                column[i] -= 1  # Reduce last column index by 1
            else:
                eq_count += 1

        if eq_count == M:
            return mat[min_row][column[min_row]]
    return -1

if __name__ == "__main__":
    M = int(input())
    N = int(input())
    mat = []
    for _ in range(M):
        row_values = list(map(int, input().strip().split()))
        mat.append(row_values)

    result = findCommon(mat)
    if result == -1:
        print("No common element")
    else:
        print("Common element is", result)
