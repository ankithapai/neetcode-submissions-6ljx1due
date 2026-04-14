class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(0, len(board)):
            row_elems = set()
            for c in range (0, len(board[r])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_elems:
                    return False
                
                row_elems.add(board[r][c])
        
        for r in range(0, len(board)):
            col_elems = set()
            for c in range (0, len(board[r])):
                if board[c][r] == ".":
                    continue
                if board[c][r] in col_elems:
                    return False
                
                col_elems.add(board[c][r])
                
        
        for square in range(0, len(board)):
            grid_elems = set()
            for i in range (3):
                for j in range(3):
                    r_grid = (square//3) * 3 + i
                    c_grid = (square % 3) * 3 + j
                    if board[r_grid][c_grid] == ".":
                        continue
                    if board[r_grid][c_grid] in grid_elems:
                        return False
                    
                    grid_elems.add(board[r_grid][c_grid])

        return True