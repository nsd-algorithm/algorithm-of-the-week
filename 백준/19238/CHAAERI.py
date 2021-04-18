dx = [-1,1,0,0]
dy = [0,0,1,-1]

from queue import PriorityQueue
from collections import deque
import heapq



def calcul_dis(sx,xy):
  q = deque([[sx,xy]])
  
  visitMap = [[0] * n for i in range(n)]
  visitMap[sx][xy] = 1
  distance[sx][xy] = 0

  while(q):
    x, y = q.popleft()
    for i in range(4):
      cx = x + dx[i]
      cy = y + dy[i]
      if(cx<n and cx>=0 and cy < n and cy >=0):
        if(visitMap[cx][cy] == 0 and myMap[cx][cy] == 0):
          distance[cx][cy] = distance[x][y] + 1
          visitMap[cx][cy] = 1
          q.append([cx,cy])

def cus_desti_dist(cus):
  cus_sx, cus_sy = cus[1], cus[2]
  cus_endx, cus_endy = cus[3], cus[4]
  q = deque([[cus_sx, cus_sy]])
  visit_cus = [[0] * n for i in range(n)]
  distance_cus = [[0] * n for i in range(n)]
  while(q):
    x, y = q.popleft()
    for i in range(4):
      cx = x + dx[i]
      cy = y + dy[i]

      if(cx<n and cx>=0 and cy<n and cy >=0):
        if(visit_cus[cx][cy] == 0 and myMap[cx][cy] == 0):
          distance_cus[cx][cy] = distance_cus[x][y] + 1
          visit_cus[cx][cy] = 1
          q.append([cx,cy])

  return distance_cus[cus_endx][cus_endy]


n, customer, energy = map(int, input().split())
myMap = [list(map(int,input().split())) for i in range(n)]

sx, sy = map(int, input().split())
sx = sx - 1
sy = sy - 1

distance = [[-1] * n for i in range(n)]
cus_check = [[0] for i in  range(customer)]
cus_list = PriorityQueue()
cus_heap = []

for i in range(customer):
  myVisit = [[0] * n for i in range(n)]
  cus_check[i] = list(map(int, input().split()))
  cus_check[i] = [0, cus_check[i][0]-1,cus_check[i][1]-1,cus_check[i][2]-1,cus_check[i][3]-1 ]
  # [택시와 걸리는 거리, 시작위치x, 시작위치y, 목적위치x, 목적위치y]

calcul_dis(sx,sy)

for i in range(customer):
  cus_check[i][0] = distance[cus_check[i][1]][cus_check[i][2]]
  cus_check[i].append(cus_desti_dist(cus_check[i]))
print(cus_check)
heapq.heapify(cus_check)

print(cus_check)

result = -1



for i in range(customer):
  calcul_dis(sx,sy)
  heapq.heapify(cus_check)
  new_customer = heapq.heappop(cus_check)

  if (new_customer[0] == -1 or new_customer[-1] == -1):
    energy = -1
    break
  if (energy <= new_customer[0]):
    energy = -1
    break
  else:
    energy -= new_customer[0]

    sx, sy = new_customer[1], new_customer[2]
    spend_energy = new_customer[-1]

    if(energy<spend_energy):
      energy = -1
      break
    else:
      energy -= spend_energy

      # charging
      energy += spend_energy * 2
      sx, sy = new_customer[3], new_customer[4]

      distance = [[-1] * n for i in range(n)]
      calcul_dis(sx,sy)

      for k in range(len(cus_check)):
        # 택시가 승객 내려준 위치에서부터 다시 다른 손님과의 거리 계산
        cus_check[k][0] = distance[cus_check[k][1]][cus_check[k][2]]

print(energy)