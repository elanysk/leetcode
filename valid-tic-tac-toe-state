class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xCount = 0
        oCount = 0
        for row in board:
            for square in row:
                if square == 'X': xCount += 1
                if square == 'O': oCount += 1
        if xCount not in {oCount, oCount+1}:
            return False
        
        xWins = []
        oWins = []
        for row in range(3):
            if board[row][0]==board[row][1]==board[row][2]=='X': xWins.append(((row, 0), (row, 1), (row, 2)))
            if board[0][row]==board[1][row]==board[2][row]=='X': xWins.append(((0, row), (1, row), (2, row)))
            if board[row][0]==board[row][1]==board[row][2]=='O': oWins.append(((row, 0), (row, 1), (row, 2)))
            if board[0][row]==board[1][row]==board[2][row]=='O': oWins.append(((0, row), (1, row), (2, row)))
        if board[0][0]==board[1][1]==board[2][2]=='X': xWins.append(((0, 0), (1, 1), (2, 2)))
        if board[0][2]==board[1][1]==board[2][0]=='X': xWins.append(((0, 2), (1, 1), (2, 0)))
        if board[0][0]==board[1][1]==board[2][2]=='O': oWins.append(((0, 0), (1, 1), (2, 2)))
        if board[0][2]==board[1][1]==board[2][0]=='O': oWins.append(((0, 2), (1, 1), (2, 0)))
            
        if len(xWins) > 0:
            if xCount != oCount + 1:
                return False
            if len(xWins) > 1:
                common = set(xWins[0])
                for win in xWins:
                    common = set(win) & common
                if len(common) != 1:
                    return False
                
        if len(oWins) > 0:
            if oCount != xCount:
                return False
            if len(oWins) > 1:
                common = set(oWins[0])
                for win in oWins:
                    common = set(win) & common
                if len(common) != 1:
                    return False
                    
        return True
