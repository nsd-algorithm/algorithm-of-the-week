import sys

num_town, store_max = list(map(int, input().split(' ')))
loop = int(input())

# 1. 배송정보 마을 순으로 정렬
INPUT = [[0] for n in range(num_town + 1)]
for n in range(loop):
    INP = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    INPUT[INP[0]].append(INP)

# print(INPUT)
# 2. 박스 배송
STORE = [0] * (num_town + 1)

answer = 0
# print(sorted(INPUT))
for town in range(1, num_town + 1):
    # 1) 트럭에서 박스 내리기
    answer += STORE[town]
    STORE[town] = 0

    for input in INPUT[town][1:]:
        s_town, e_town, num_box = input

        # 2) 박스 싣기
        if s_town == town:
            store_reserve = store_max - sum(STORE)
            # print(store_max, sum(STORE), store_reserve)
            if store_reserve > num_box:
                STORE[e_town] += num_box

            else:
                STORE[e_town] += min(num_box, store_reserve)
                store_less = num_box - store_reserve  # 남은 용량
                # print("store_less: ", store_less)
                town_tmp = num_town + 1
                while store_less > 0:
                    town_tmp -= 1
                    if town_tmp == e_town: break

                    if STORE[town_tmp] > 0:
                        # print('good', store_less, STORE)
                        if STORE[town_tmp] >= store_less:

                            STORE[town_tmp] -= store_less
                            STORE[e_town] += store_less
                            break
                        else:
                            STORE[e_town] += STORE[town_tmp]
                            store_less -= STORE[town_tmp]
                            STORE[town_tmp] = 0

    # print(town, STORE[1:], answer)

print(answer)
