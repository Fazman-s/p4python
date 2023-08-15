# Function to fill alternating rectangles of 0 and X
def fill0X(m, n):
    i, k, l = 0, 0, 0
    r = m
    c = n
    a = [[None] * n for i in range(m)]
    x = 'X'

    while k < m and l < n:
        for i in range(l, n):
            a[k][i] = x
        k += 1

        for i in range(k, m):
            a[i][n - 1] = x
        n -= 1

        if k < m:
            for i in range(n - 1, l - 1, -1):
                a[m - 1][i] = x
            m -= 1

        if l < n:
            for i in range(m - 1, k - 1, -1):
                a[i][l] = x
            l += 1

        x = 'X' if x == '0' else '0'

    for i in range(r):
        for j in range(c):
            print(a[i][j], end=" ")
        print()

m, n = map(int, input().split())
fill0X(m, n)


