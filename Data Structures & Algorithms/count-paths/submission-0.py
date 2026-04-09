class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0

        mat = [[0]*n for i in range(m)]

        i = m-1
        j = n-1
        while i >= 0:
            j = n-1
            while j >= 0:
                if i == m-1 and j == n-1:
                    # 1 ways to reach here
                    mat[i][j] = 1
                    j-=1
                    continue
                
                bottom = mat[i+1][j] if (i+1)<m else 0
                right = mat[i][j+1] if (j+1)<n else 0
                mat[i][j] = bottom + right
                j-=1
            i -= 1
        return mat[0][0]





"""
Lets start from bottom right - 0 ways to reach there
from n-1][n-2] and [n-2][n-1] there are 1 way
from [n-2][n-2] there are n-1][n-2]+[n-2][n-1] ways

"""