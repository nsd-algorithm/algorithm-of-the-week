dx = [-1,1,0,0]
dy = [0,0,1,-1]

from queue import PriorityQueue
from collections import deque
import heapq


# 스타트지점에서부터 다른 모든 곳들까지의 거리를 계산하는 함수
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

#손님의 시작지점과 목적지 지점까지 거리를 계산하는 함수
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
# 조건에서 손님의 거리가 가까운 순으로 부터 손님을 받아야 하기 때문에 heap으로 정렬 후 가장 마지막에 있는(가장 거리가 짧은) 손님을 선택 할 것임
cus_list = PriorityQueue()
cus_heap = []

for i in range(customer):
  myVisit = [[0] * n for i in range(n)]
  cus_check[i] = list(map(int, input().split()))
  cus_check[i] = [0, cus_check[i][0]-1,cus_check[i][1]-1,cus_check[i][2]-1,cus_check[i][3]-1 ]
  # [택시와 걸리는 거리, 시작위치x, 시작위치y, 목적위치x, 목적위치y]


# 현재 위치에서 각 손님들까지 얼마나 걸리는지 계산
calcul_dis(sx,sy)

for i in range(customer):
  cus_check[i][0] = distance[cus_check[i][1]][cus_check[i][2]]
  # 손님 별로 현재 위치에서 얼마나 걸리는지 해당 데이터를 끝에 추가함
  cus_check[i].append(cus_desti_dist(cus_check[i]))
print(cus_check)

# 다시 한 번 heap 정렬(내림차순)
heapq.heapify(cus_check)

print(cus_check)

result = -1



for i in range(customer):
  calcul_dis(sx,sy)
  heapq.heapify(cus_check)
  new_customer = heapq.heappop(cus_check)


  # 손님과의 거리가 -1이거나 손님의 목적지까지의 거리가 -1이면 종료
  if (new_customer[0] == -1 or new_customer[-1] == -1):
    energy = -1
    break

  # 가지고 있는 에너지가 손님에게 가기까지 충분하지 않으면
  if (energy <= new_customer[0]):
    energy = -1
    break
  else:
    #새로운 손님까지의 거리를 에너지로 소모
    energy -= new_customer[0]

    # 새로운 손님의 위치가 현재 택시의 위치로 업데이트
    sx, sy = new_customer[1], new_customer[2]

    # 소모할 에너지
    spend_energy = new_customer[-1]

    # 만약 소모할 에너지가 충분하지 않으면 종료
    if(energy<spend_energy):
      energy = -1
      break
    else:

      #에너지 소모
      energy -= spend_energy

      # charging
      energy += spend_energy * 2

      # 손님을 내려준 위치가 현재 택시의 시작 위치로 업데이트
      sx, sy = new_customer[3], new_customer[4]

      # 현재 택시의 위치에서 다시 다른 손님들간 거리를 계산하기 위해 distance를 초기화

      distance = [[-1] * n for i in range(n)]

      # 다시 택시의 시작 지점에서 모든 곳의 거리 계산
      calcul_dis(sx,sy)

      for k in range(len(cus_check)):
        # 택시가 승객 내려준 위치에서부터 다시 다른 손님과의 거리 계산
        cus_check[k][0] = distance[cus_check[k][1]][cus_check[k][2]]

print(energy)