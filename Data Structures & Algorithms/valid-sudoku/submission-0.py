class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQUARES = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if value == '.':
                    continue
                if value in ROWS[row]:
                    return False
                else:
                    ROWS[row].add(value)
                if value in COLS[col]:
                    return False
                else:
                    COLS[col].add(value)
                if value in SQUARES[(row//3, col//3)]:
                    return False
                else:
                    SQUARES[(row//3, col//3)].add(value)
        return True