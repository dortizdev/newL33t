class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        q = []
        dir = [[0,1],[0,-1],[1,0],[-1,0]]

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = "x"

        for rq, cq in q:
            for rd, cd in dir:
                curR = rq + rd
                curC = cq + cd
                if 0 <= curR < r and 0 <= curC < c and mat[curR][curC] == "x":
                    mat[curR][curC] = mat[rq][cq] + 1
                    q.append((curR,curC))
        return mat