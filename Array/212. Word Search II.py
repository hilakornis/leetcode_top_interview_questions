class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def inBounds(board, i , j):
            return i >= 0 and j >= 0 and i <= len(board) -1 and j <= len((board[0])) - 1
        
        def check(word_i, board, word, i, j, visited):
            if word_i >= len(word): return True
            if not inBounds(board, i, j) or (i,j) in visited: return False
            if board[i][j] == word[word_i]:
                a = check(word_i+1, board, word, i-1, j, visited.union((i,j)))
                if a:
                    return True
                b = check(word_i+1, board, word, i+1, j, visited.union((i,j)))
                if b:
                    return True
                c = check(word_i+1, board, word, i, j-1, visited.union((i,j)))
                if c:
                    return True
                d = check(word_i+1, board, word, i, j+1, visited.union((i,j)))
                return d
            
        def isIn(word, board, m):
            found = False
            for i,j in m[word[0]]:
                found = check(0, board, word, i, j, set())
                if found: break
            return found
        
        def buildM(board, m):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    m[board[i][j]].append((i,j))
        
        m = collections.defaultdict(list)
        buildM(board, m)
        res = []
        for word in words:
            if isIn(word, board, m):
                res.append(word)
        return res
