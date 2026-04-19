class Solution:

    ENABLE_MEMOIZE = False

    @staticmethod
    def cood_code(i,j):
        return "%d--%d"%(i,j)
    
    @staticmethod
    def memo_code(i,j,w_i):
        return "%d--%d__%d"%(i,j, w_i)

    def exist(self, board: List[List[str]], word: str) -> bool:
        seen_lookup = {}
        memo = {}

        def scramble(board_i,board_j,w_i):
            # Since we are still looking for the word, verify if the bounds are fine
            if board_i < 0 or board_j < 0 or board_i >= len(board) or board_j >= len(board[0]):
                return False
            
            # Verify if the current char is a match
            if board[board_i][board_j] != word[w_i]:
                return False

            # Check if the word is already done
            if w_i == len(word) - 1:
                print("Found word")
                return True # Found the word

            # Verify that we have not evaluated this before
            memo_code = Solution.memo_code(board_i,board_j,w_i)
            if Solution.ENABLE_MEMOIZE:
                if memo_code in memo:
                    return memo[memo_code]

            # Now we have 4 options
            # See the current node and scramble further
            board_code = Solution.cood_code(board_i,board_j)
            seen_lookup[board_code] = True
            found = False
            if not found and Solution.cood_code(board_i,board_j+1) not in seen_lookup:
                found = scramble(board_i,   board_j+1, w_i+1)
            if not found and Solution.cood_code(board_i,board_j-1) not in seen_lookup:
                found = scramble(board_i,   board_j-1, w_i+1)
            if not found and Solution.cood_code(board_i+1,board_j) not in seen_lookup:
                found = scramble(board_i+1, board_j, w_i+1)
            if not found and Solution.cood_code(board_i-1,board_j) not in seen_lookup:
                found = scramble(board_i-1, board_j, w_i+1)
            
            # Unsee it now
            del seen_lookup[board_code]
            # Store the memo data
            memo[memo_code] = found

            return found
            


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # Potential candidate maybe here
                    if scramble(i,j,0):
                        return True
        
        return False