class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(row, col):
            # Check if the column or diagonals are under attack
            return col not in cols and \
                   (row - col) not in diag1 and \
                   (row + col) not in diag2
        
        def place_queens(row):
            if row == n:
                # Convert the board to the required format
                result.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    # Place the queen
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    board[row][col] = 'Q'
                    
                    # Recur to place the rest of the queens
                    place_queens(row + 1)
                    
                    # Remove the queen and backtrack
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)
                    board[row][col] = '.'
        
        result = []
        board = [['.'] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()
        place_queens(0)
        
        return result
