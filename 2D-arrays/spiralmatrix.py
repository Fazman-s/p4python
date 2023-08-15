def spiral(matrix):
    result = []
    
    while matrix:
        result += matrix[0] 
        
        if len(matrix) > 1:
            matrix = list(zip(*matrix[1:]))[::-1] 
        else:
            break
    
    return '-'.join(map(str, result))

m, n = map(int, input().split())
matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)


output = spiral(matrix)
print(output)
