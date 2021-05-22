
n, g, k = map(int,input().split())
fire_list = []
myMap = [[[] for _ in range(n)] for _ in range(n)]
print("ddd",len(myMap))
for _ in range(g):
  r,c,m,s,d = map(int,input().split())
  myMap[r-1][c-1].append([r,c,m,s,d])
  fire_list.append([r,c,m,s,d])

dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


for _ in range(k):
  for i in range(len(fire_list)):
    r,c,m,s,d = fire_list[i]
    dx, dy = s * dir[d][0], s * dir[d][1]
    nx, ny = (r+dx)%n, (c+dy)%n
    myMap[nx-1][ny-1].append([nx,ny,m,s,d])
    print("1  myMap",myMap)
    #print("add",[nx,ny,m,s,d])
    #print("remove",[r,c,m,s,d])
    #print("fire_list",fire_list)
    myMap[r-1][c-1].remove([r,c,m,s,d])
    print("2 myMap", myMap)

  for i in range(n):
    for j in range(n):
      if( len(myMap[i][j])>1):
        m = 0
        s = 0
        d = []
        for p in range(len(myMap[i][j])):
          m += myMap[i][j][p][2]
          s += myMap[i][j][p][3]
          d.append(myMap[i][j][p][4]%2)
        m //= 5
        if m != 0:
          s //= len(myMap[i][j])
          if(d == [0]*len(myMap[i][j]) or d == [1]*len(myMap[i][j])):
            myMap[i][j] = [[i+1,j+1,m,s,0],[i+1,j+1,m,s,2],[i+1,j+1,m,s,4],[i+1,j+1,m,s,6]]
          else:
            myMap[i][j] = [[i+1,j+1,m,s,1],[i+1,j+1,m,s,3],[i+1,j+1,m,s,5],[i+1,j+1,m,s,7]]
        else:
          myMap[i][j] = []
        print("3 myMap", myMap)

  fire_list = []
  for i in range(n):
    for j in range(n):
      if myMap[i][j] != []:
        fire_list += myMap[i][j]
  g = len(fire_list)
  #print("after",fire_list)
  #print("after myMap",myMap)



a = 0
for i in range(n):
  for k in range(n):
    for k in range(len(myMap[i][j])):
      a += myMap[i][j][k][2]
print(a)

# from queue import PriorityQueue
# from collections import deque
# import heapq

# dx = [0,1,1,1,0,-1,-1,-1]
# dy = [-1,-1,0,1,1,1,0,-1]

# n, m, k = map(int,input().split())
# # [r, c, m, d, s]


# def moving_fire(fire):
#   sx, sy = fire[0], fire[1]
#   ex = sx + dx[fire[3]] * fire[4]
#   ex = ex % n
#   ey = sy + dy[fire[3]] * fire[4]
#   print("sx :",sx,"sy:",sy,"ex:",ex,"ey:",ey)
#   ey = ey % n
#   return ey,ex



# fire_list = [list(map(int,input().split())) for i in range(m)]
# myMap = [[0] * n for i in range(n)]


# for i in range(m):
#   fire_list[i][0] -= 1
#   fire_list[i][1] -= 1
#   myMap[fire_list[i][1]][fire_list[i][0]] = 1


# for i in range(n):
#   for j in range(n):
#     print(myMap[i][j], end=' ')
#   print()
# '''
# 4 2 1
# 1 2 5 2 2
# 1 4 7 1 6
# '''

# print("-----------------")
# print()


# for i in range(n):
#   for j in range(n):
#     print(myMap[i][j], end=' ')
#   print()

# print(fire_list)



# for _ in range(k):
#   for i in range(m):
#     ty, tx = moving_fire(fire_list[i])
#     myMap[ty][tx] += myMap[fire_list[i][1]][fire_list[i][0]]
#     myMap[fire_list[i][1]][fire_list[i][0]] -= 1
#     fire_list[i][1] = ty
#     fire_list[i][0] = tx

#     print("fire_list", fire_list)
#     # for i in range(n):
#     #   for j in range(n):
#     #     print(myMap[i][j], end=' ')
#     #   print()







'''
from queue import PriorityQueue
from collections import deque
import heapq

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

n, m, k = map(int,input().split())
# [r, c, m, d, s]


def moving_fire(fire):
  sx, sy = fire[0], fire[1]
  ex = sx + dx[fire[3]] * fire[4]
  ex = ex % n
  ey = sy + dy[fire[3]] * fire[4]
  print("sx :",sx,"sy:",sy,"ex:",ex,"ey:",ey)
  ey = ey % n
  return ey,ex

def divide_fire(map):
  fire_list_2 = []
  for i in range(n):
    for j in range(n):
      if(map[j][i] >= 2):
        mass = 0
        velocity = 0
        direc = 0
        for lists in fire_list:
          if (j == lists[0] and i == lists[1]):
            mass += lists[2]
            velocity += lists[3]
            direc += lists[4] % 2
        mass = mass/5
        velocity = velocity/map[j][i]
        if(mass <= 0):
          continue
        else:
          if(direc == 0):
            fire_list_2.append([j, i, mass, 0, velocity])
            fire_list_2.append([j, i, mass, 2, velocity])
            fire_list_2.append([j, i, mass, 4, velocity])
            fire_list_2.append([j, i, mass, 6, velocity])
          else:
            fire_list_2.append([j, i, mass, 1, velocity])
            fire_list_2.append([j, i, mass, 3, velocity])
            fire_list_2.append([j, i, mass, 5, velocity])
            fire_list_2.append([j, i, mass, 7, velocity])
  return fire_list_2

fire_list = [list(map(int,input().split())) for i in range(m)]
myMap = [[0] * n for i in range(n)]


for i in range(m):
  fire_list[i][0] -= 1
  fire_list[i][1] -= 1
  myMap[fire_list[i][1]][fire_list[i][0]] = 1


for i in range(n):
  for j in range(n):
    print(myMap[j][i], end=' ')
  print()

print("-----------------")
print()




print(fire_list)



for _ in range(k):
  new_fire = []
  for i in range(m):
    ty, tx = moving_fire(fire_list[i])
    myMap[ty][tx] += myMap[fire_list[i][1]][fire_list[i][0]]
    myMap[fire_list[i][1]][fire_list[i][0]] -= 1
    fire_list[i][1] = ty
    fire_list[i][0] = tx

    new_fire = divide_fire(myMap)
    for i in range(n):
      for j in range(n):
        print(myMap[j][i], end=' ')
      print()
    print(new_fire)
  
  print()
'''