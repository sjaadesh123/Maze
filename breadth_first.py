class Maze:
    def __init__(self,matrix,length,breadth):
        self.length=length
        self.breadth=breadth
        self.matrix=matrix
    def navigator(self,i,j):
        queue=[(i,j)]
        while queue:
           val=queue.pop(0)

           if self.matrix[val[0]][val[1]]=='B':
               for row in self.matrix:
                 print(' '.join(map(str, row)))
               raise SystemExit(0)
           if self.matrix[val[0]][val[1]]!='A':
            self.matrix[val[0]][val[1]]='*'
           if 0<=val[0]+1 and 0<=val[1] and val[0]+1<self.breadth and val[1]<self.length and self.matrix[val[0]+1][val[1]]!='#' and self.matrix[val[0]+1][val[1]]!='*' and self.matrix[val[0]+1][val[1]]!='A':
               queue.append((val[0]+1,val[1]))
           if 0<=val[0]-1 and 0<=val[1]  and val[0]-1<self.breadth and val[1]<self.length  and self.matrix[val[0]-1][val[1]]!='#' and self.matrix[val[0]-1][val[1]]!='*' and self.matrix[val[0]-1][val[1]]!='A':
               queue.append((val[0]-1,val[1]))
           if 0<=val[0] and 0<=val[1]+1 and val[0]<self.breadth and val[1]+1<self.length  and self.matrix[val[0]][val[1]+1]!='#' and self.matrix[val[0]][val[1]+1]!='*' and self.matrix[val[0]][val[1]+1]!='A':
               queue.append((val[0],val[1]+1))
           if 0<=val[0] and 0<=val[1]-1 and val[0]<self.breadth and val[1]-1<self.length  and self.matrix[val[0]][val[1]-1]!='#' and self.matrix[val[0]][val[1]-1]!='*' and self.matrix[val[0]][val[1]-1]!='A':
               queue.append((val[0],val[1]-1))




maze_matrix=[]
breadth=0
with open("maze.txt") as f:
    for x in f:
        length=len(x.split(' '))
        temp=x.split(' ')
        temp[-1]=temp[-1].rstrip('\n')
        maze_matrix.append(temp)
        if 'A' in temp:
            a_index=(temp.index('A'),breadth)

        breadth+=1
m=Maze(maze_matrix,length,breadth)
m.navigator(a_index[1],a_index[0])
