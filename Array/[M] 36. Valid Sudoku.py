# Joshua Hui - 8/26/2019

import collections

class Solution:
    def isValidSudoku(self, board):
        rowHash = collections.defaultdict(list)
        columnHash = collections.defaultdict(list)
        subboxHash = collections.defaultdict(list)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                quadrant = self.determineWhichSubBox(i,j)
                if board[i][j] in rowHash[i] or board[i][j] in columnHash[j] or board[i][j] in subboxHash[quadrant]:
                    return False
                else:
                    rowHash[i].append(board[i][j])
                    columnHash[j].append(board[i][j])
                    subboxHash[quadrant].append(board[i][j])
        return True
                
                
                
    def determineWhichSubBox(self,i,j):
        if i<=2:
            if j<=2:
                return 1
            elif 2<j<=5:
                return 2
            elif 5<j<=8:
                return 3
        elif 2<i<=5:
            if j<=2:
                return 4
            elif 2<j<=5:
                return 5
            elif 5<j<=8:
                return 6
        elif 5<i<=8:
            if j<=2:
                return 7
            elif 2<j<=5:
                return 8
            elif 5<j<=8:
                return 9
        
# Runtime: 108 ms, faster than 77.23% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.9 MB, less than 5.88% of Python3 online submissions for Valid Sudoku.