from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            modified = [x for x in row if x != "."]

            if modified:
                count = Counter(modified)

                mc = count.most_common(1)

                (k, c) = mc[0]

                if c > 1:
                    return False
        
        for column in zip(*board):
            modified = [x for x in column if x != "."]

            if modified:
                count = Counter(modified)

                mc = count.most_common(1)

                (k, c) = mc[0]

                if c > 1:
                    return False
        i = 0
        j = 0
        check = set()
        while i < 9:
            while j < 9:
                if board[i][j] != ".":
                    if (i+1) % 3 == 1:

                        if (j+1) % 3 == 1:
                            check = set([board[i+1][j+1],board[i+1][j+2], board[i+2][j+1], board[i+2][j+2]])
                            
                        elif (j+1) % 3 == 2:
                            check = set([board[i+1][j-1],board[i+1][j+1], board[i+2][j-1], board[i+2][j+1]])
                            
                        elif (j+1) % 3 == 0:
                            check = set([board[i+1][j-2],board[i+1][j-1], board[i+2][j-2], board[i+2][j-1]])
                        
                        
                    elif (i + 1) % 3 == 2:
                        if (j+1) % 3 == 1:
                            check = set([board[i+2][j+1], board[i+2][j+2]])
                        elif (j+1) % 3 == 2:
                            check = set([board[i+2][j-1], board[i+2][j+1]])
                        elif (j+1) % 3 == 2:
                            check = set([board[i+2][j-2], board[i+2][j-1]])
                    
                    if board[i][j] in check:
                                return False
                
                j += 1

            i += 1
        return True
                    





