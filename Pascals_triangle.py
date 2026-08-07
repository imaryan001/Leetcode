from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for r in range(numRows):

            row = []

            for c in range(r + 1):
                if c == 0 or c == r:
                    row.append(1)

                else:
                    value = triangle[r-1][c-1] + triangle[r-1][c]
                    row.append(value)

            triangle.append(row)

        return triangle
obj = Solution()

numRows = 5

print(obj.generate(numRows))