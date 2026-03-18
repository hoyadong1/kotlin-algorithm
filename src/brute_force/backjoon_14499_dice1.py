h, w, x, y, n = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(h)]

dirs = list(map(int, input().split()))

top = 0
bottom = 0
east = 0
west = 0
north = 0
south = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(dir):
   global x, y

   nx, ny = x + dx[dir-1], y + dy[dir-1]

   if nx < 0 or nx >= h or ny < 0 or ny >= w:
       return False
   else:
       x, y = nx, ny
       re_dice(dir -1)
       return True
 
def re_dice(dir):
    global top, bottom, east, west, north, south

    if dir == 0:
        top, bottom, east, west = west, east, top, bottom
    elif dir == 1:
        top, bottom, east, west = east, west, bottom, top
    elif dir == 2:
        top, bottom, north, south = north, south, bottom, top
    elif dir == 3:
        top, bottom, north, south = south, north, top, bottom


for dir in dirs:
    if move(dir):
      if table[x][y] == 0:
          table[x][y] = bottom
      else:
          table[x][y], bottom = 0, table[x][y]
      print(top)
    
