'''
def rotate(belt):
  tmp1 = belt[1].pop(-1)
  belt[0].insert(0, tmp1)
  tmp2 = belt[0].pop(-1)
  belt[1].insert(0,tmp2)




def belt_print(belt):
  for i in range(len(belt[0])):
    print(belt[0][i], end = '')
  print ()

  for i in range(1, len(belt[0]) + 1):
    print(belt[1][-i], end = '')
  print ()


n, k = map(int, input().split())
tmp = list(map(int, input().split()))
my_belt = [tmp[ : n], tmp[n : ]]
print(my_belt)
belt_print(my_belt)
rotate(my_belt)
belt_print(my_belt)


count = 0

robot_map = [0 for i in range(n)]

while(count <= k):
  rotate(my_belt)
  for i in range(n):
    if 

'''



def rotate(belt,robot):
  tmp1 = belt.pop(-1)
  belt.insert(0, tmp1)
  robot.insert(0,0)
  robot.pop()

  return belt, robot

1 2 3 4 5 6

0 0 1
6 1 2 
5 4 3


def move_robot(belt, robot):
  robot[-1] = 0
  for i in range(len(robot)-2, -1, -1):
    if robot[i] != 0:
      if i + 1 < len(robot):
        if belt[i + 1] > 0:
          if robot[i + 1] == 0:
            robot[i + 1] = robot[i]
            robot[i] = 0
            belt[i + 1] -= 1
  return belt, robot
  


def belt_print(belt):
  for i in range(len(belt)//2):
    print(belt[i], end = '')
  print()
  for i in range(1, len(belt)//2 + 1):
    print(belt[-i], end = '')
  print()

def robot_print(robot):
  for i in range(len(robot)):
    print(robot[i], end = '')
  print()

n, k = map(int, input().split())
my_belt = list(map(int, input().split()))


count = 0
result = 0
robot_map = [0 for i in range(n)]

while(1):

  my_belt,robot_map = rotate(my_belt,robot_map)
  my_belt, robot_map = move_robot(my_belt, robot_map)

  if robot_map[0] == 0 :
    if my_belt[0] > 0 :
      robot_map[0] = 1
      my_belt[0] -= 1

  robot_map[-1] = 0

  count = my_belt.count(0)
  result += 1
  if count >= k:
    break

print(result)
