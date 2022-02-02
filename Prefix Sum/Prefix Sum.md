# Summary:
https://leetcode-cn.com/circle/discuss/SrePlc/
https://blog.csdn.net/weixin_43206795/article/details/105718567
https://blog.csdn.net/weixin_45629285/article/details/111146240?spm=1001.2101.3001.6650.7&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EOPENSEARCH%7EHighlightScore-7.queryctrv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EOPENSEARCH%7EHighlightScore-7.queryctrv2&utm_relevant_index=13
1. Basic prefix sum:

2d: 
       
        class NumMatrix:
        
            def __init__(self, matrix: List[List[int]]):
                rows, cols = len(matrix), len(matrix[0])
                # sum[i][j] is sum of all elements inside the rectangle [0,0,i,j]
                self.sum = [[0] * (cols + 1) for _ in range(rows + 1)]
                for r in range(1, rows + 1):
                    for c in range(1, cols + 1):
                        self.sum[r][c] = self.sum[r-1][c] + self.sum[r][c-1] - self.sum[r-1][c-1] + matrix[r-1][c-1]
                
        
            def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
                # Since our `sum` starts by 1 so we need to increase r1, c1, r2, c2 by 1
                r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
                return self.sum[r2][c2] - self.sum[r2][c1 - 1] - self.sum[r1 - 1][c2] + self.sum[r1 - 1][c1 - 1]
        

        
leetcode 303, 304

1. hashmap:
leetcode 560, 525, 