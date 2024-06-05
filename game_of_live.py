import random as rd

board = []
rows = 4
cols = 3


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.living_n_cells = 0
        self.dead_n_cells = 0
        for row in range(len(board)):
            for col in range(len(board)-1):
                    if board[row][col].alive_state == 1: #if is alive
                         board[row][col].check_n_alive()
                    elif board[row][col].alive_state == 0: # is dead
                        board[row][col].check_n_dead()
                         

class Cell:
     def __init__(self, row:int, col:int):
          self.row = row
          self.col = col
          self.alive_state = rd.randint(0, 1)
     def check_n_alive(self):
        self.n_cells = 0
        for row in range(len(board)):
            for col in range(len(board)-1):
                if self.row == 1: #middle row
                    if (self.col == col-1 or self.col == col +1):#horizontal chekc
                        self.n_cells += 1
                    if (self.row == row-1 or self.row == row+1):#vertical check
                        self.n_cells += 1
                    if (self.row == row +1 or self.row == row-1) and (self.col == col + 1 or self.col == col-1):
                        self.n_cells += 1
        print(self.n_cells, "neighboor cells", self.row, self.col)



         
     def check_n_dead(self):
        self.n_cells = 0
          


for _ in range(rows):
    col = [0]*cols
    board.append(col)
for row in range(len(board)):
    for col in range(len(board)-1):
        board[row][col] = Cell(row, col)
        print(board[row][col].alive_state, end=" ")
    print(" ")
s = Solution()
s.gameOfLife(board)