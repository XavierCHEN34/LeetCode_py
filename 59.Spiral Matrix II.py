import numpy as np
def spiralOrder(n):
        if n == 0:
            return []

        l = np.zeros([n,n])
        l_index = [(0,0)]
        i_row,i_col = 0,0
        n_row = n
        n_col = n
        visited = np.zeros([n_row,n_col])
        visited[0,0] = 1

        direction = 0 # 0-1-2-3  = right-down-left-up
        while(np.sum(visited) < n_row * n_col):
            next_row,next_col =  move(i_row,i_col,direction)
            if next_row < n_row and next_row >= 0 and next_col < n_col and next_col >= 0 and visited[next_row,next_col] ==0:

                i_row,i_col = next_row,next_col
                #print(i_row,i_col)
                l_index.append( (i_row,i_col)  )
                visited[i_row,i_col] = 1
            else:
                direction = (direction + 1) % 4


        for i in range(n**2):
            row,col = l_index[i]
            l[row,col] = i+1

        return l

def move(x,y,d):
        if d == 0:
            return x,y+1
        if d == 1:
            return x+1,y
        if d == 2:
            return x,y-1
        if d == 3:
            return x-1,y



print(spiralOrder(3))