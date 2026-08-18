grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]
]

count = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):   # number of columns
        if grid[i][j] < 0:
            count += 1

print(count)






       
#54spiral matrix 1
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        res = []

        while top <= bottom and left <= right:

            # 1. Left -> Right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. Top -> Bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
    
    
    
#59 spiral matrix 2

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
    
        res = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # 1. Left -> Right
            for col in range(left, right + 1):
                res[top][col] = num
                num += 1
            top += 1

            # 2. Top -> Bottom
            for row in range(top, bottom + 1):
                res[row][right] = num
                num += 1
            right -= 1

            # 3. Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res[bottom][col] = num
                    num += 1
                bottom -= 1

            # 4. Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[row][left] = num
                    num += 1
                left += 1

        return res
            