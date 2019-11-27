class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # -1 -- horizontal
        # -2 -- vertical
        m = set()
        row = len(grid)
        col = len(grid[0])
        count = 0
        def search(i, j):
            
            #go up
            offset = 1
            while(i-offset>=0):
                if(grid[i-offset][j] == 1):
                    m.add((i-offset,j))
                    m.add((i,j))
                    # not_connected = False
                    break
                offset += 1
            offset = 1
            while(i+offset<row):
                if(grid[i+offset][j] == 1):
                    m.add((i+offset,j))
                    m.add((i,j))
                    # not_connected = False
                    break
                offset += 1
            offset = 1
            while(j-offset>=0):
                if(grid[i][j-offset] == 1):
                    m.add((i,j-offset))
                    m.add((i,j))
                    # not_connected = False
                    break
                offset += 1
            
            offset = 1
            while(j+offset<col):
                if(grid[i][j+offset] == 1):
                    m.add((i,j+offset))
                    m.add((i,j))
                    # not_connected = False
                    break
                offset += 1
            
            
                
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in m:
                    search(i,j)
                    
                    
        return len(m)
                