class Solution:
    def exist(self, board, word):
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

# Example
if __name__ == "__main__":
    solution = Solution()
    rows = int(input())
    cols = int(input())
    board = []
    for _ in range(rows):
        row = list(input().strip().split())
        board.append(row)
    word = input().strip()
    
    result = solution.exist(board, word)
    print("true" if result else "false")
