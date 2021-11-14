my_map = [list(map(int, input().split())) for i in range(3)]
my_map_transe = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        my_map_transe[i][j] = my_map[j][i]

# 마방진의 1열 또는 1행 또는 대각선의 합을 x라 하자
# 마방진의 9개 수를 다 더하면 3x이다

# (1) 0의 갯수가 3개인 경우
# 0 x x
# x 0 x
# x x 0
# 또는
# x x 0
# x 0 x
# 0 x x 일 때
# 0을 제외한 마방진 6개의 합은 2x이다
# 따라서 마방진 6개 숫자의 합에 2를 나누면 원하는 x의 값을 구할 수 있다

# (2) 0의 갯수가 2개 이하인 경우
# 0이 없는 열 또는 행의 합을 구하면 x이다
# x를 구한 후 0이 있는 행 또는 합에서 2개의 숫자를 더하고 x에서 그 합을 빼면, 0에 들어가는 숫자를 구할 수 있다


# 먼저 (1) 또는 (2)의 경우를 나눈다

count_zero = 0
my_sum = 0
for i in range(3):
    count_zero += my_map[i].count(0)

if ([my_map[0][1], my_map[1][1], my_map[2][2]].count(0) == 0):
    # print("2")
    my_sum = sum([my_map[0][0], my_map[1][1], my_map[2][2]])

elif ([my_map[2][0], my_map[1][1], my_map[0][2]].count(0) == 0):
    # print("3")
    my_sum = sum([my_map[2][0], my_map[1][1], my_map[0][2]])

elif([my_map[0][0], my_map[1][2], my_map[2][2]].count(0) > 0 or [my_map[2][0], my_map[1][1], my_map[0][2]].count(0) > 0):
    # print("4")
    for i in range(3):
        if(my_map[i].count(0)):
            my_sum = sum(my_map[i])
        if([my_map[0][i], my_map[1][i], my_map[2][i]].count(0) == 0):
            my_sum = sum([my_map[0][i], my_map[1][i], my_map[2][i]])
elif([my_map[0][0], my_map[1][2], my_map[2][2]].count(0) == 3 or [my_map[2][0], my_map[1][1], my_map[0][2]].count(0) == 3):
    my_sum = sum(my_map[0] + my_map[1] + my_map[2])
    my_sum /= 2
print(my_sum)

if((my_map[0][0] + my_map[1][1] + my_map[2][2]) == 0 or (my_map[0][2]+my_map[1][1]+my_map[2][0]) == 0):
    # print("a")

    for i in range(3):
        if(my_map[i].count(0) == 1):
            my_map[i][my_map[i].index(0)] = int(my_sum - sum(my_map[i]))
        if([my_map[0][i], my_map[1][i], my_map[2][i]].count(0) == 1):
            # print([my_map[0][i], my_map[1][i], my_map[2][i]])
            my_map[[my_map[0][i], my_map[1][i], my_map[2][i]].index(0)][i] = int(
                my_sum - sum([my_map[0][i], my_map[1][i], my_map[2][i]]))

else:

    for i in range(3):
        if(my_map[i].count(0) == 1):
            my_map[i][my_map[i].index(0)] = int(my_sum - sum(my_map[i]))
        if([my_map[0][i], my_map[1][i], my_map[2][i]].count(0) == 1):
            # print([my_map[0][i], my_map[1][i], my_map[2][i]])
            my_map[[my_map[0][i], my_map[1][i], my_map[2][i]].index(0)][i] = int(
                my_sum - sum([my_map[0][i], my_map[1][i], my_map[2][i]]))

for i in range(3):
    if(my_map[i].count(0) == 1):
        my_map[i][my_map[i].index(0)] = int(my_sum - sum(my_map[i]))
    if([my_map[0][i], my_map[1][i], my_map[2][i]].count(0) == 1):
        # print([my_map[0][i], my_map[1][i], my_map[2][i]])
        my_map[[my_map[0][i], my_map[1][i], my_map[2][i]].index(0)][i] = int(
            my_sum - sum([my_map[0][i], my_map[1][i], my_map[2][i]]))


for i in range(3):
    for j in range(3):
        print(my_map[i][j], end=' ')
    print()


# count_zero = 0
# my_sum = 0
# for i in range(3):
#     count_zero += my_map[i].count(0)

# if(count_zero) == 3:
#     for i in range(3):
#         my_sum += sum(my_map[i])
#     my_sum /= 2

#     for i in range(3):
#         if(my_map[i].count(0) == 1):
#             my_map[i][my_map[i].index(0)] = int(my_sum - sum(my_map[i]))

#         if(my_map_transe[i].count(0) == 1):
#             my_map_transe[i][my_map_transe[i].index(
#                 0)] = int(my_sum - sum(my_map_transe[i]))

#     for i in range(3):
#         for j in range(3):
#             my_map_transe[i][j], my_map_transe[j][i] = my_map_transe[j][i], my_map_transe[i][j]

#     for i in range(3):
#         for j in range(3):
#             if(my_map[i][j] == 0):
#                 my_map[i][j] = my_map_transe[i][j]

# else:
#     # 0이 없는 행 또는 열을 찾는다
#     for i in range(3):
#         if(my_map[i].count(0) == 0):
#             my_sum += sum(my_map[i])
#             break

#         elif(my_map_transe[i].count(0) == 0):
#             my_sum += sum(my_map_transe[i])
#             break

#     for i in range(3):
#         if(my_map[i].count(0) == 1):
#             my_map[i][my_map[i].index(0)] = int(my_sum - sum(my_map[i]))
#         if(my_map_transe[i].count(0) == 1):
#             my_map_transe[i][my_map_transe[i].index(
#                 0)] = int(my_sum - sum(my_map_transe[i]))
#     for i in range(3):
#         for j in range(3):
#             my_map_transe[i][j], my_map_transe[j][i] = my_map_transe[j][i], my_map_transe[i][j]
#     for i in range(3):
#         for j in range(3):
#             if(my_map[i][j] == 0):
#                 my_map[i][j] = my_map_transe[i][j]

# for i in range(3):
#     for j in range(3):
#         print(my_map[i][j], end=' ')
#     print()
