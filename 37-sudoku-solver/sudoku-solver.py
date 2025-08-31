class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        empties = []

        # initialize sets
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i//3)*3 + j//3].add(val)
                else:
                    empties.append((i, j))

        def backtrack(idx=0):
            if idx == len(empties):
                return True
            
            r, c = empties[idx]
            b = (r//3)*3 + c//3

            for ch in map(str, range(1, 10)):
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[b].add(ch)

                    if backtrack(idx+1):
                        return True

                    # undo
                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[b].remove(ch)

            return False

        backtrack()
