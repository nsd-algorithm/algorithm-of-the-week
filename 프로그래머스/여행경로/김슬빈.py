import copy

def solution(tickets):

    # 여행 결로가 짜지는지 순서대로 확인
    TRV_ROUTE = []
    for n in range(len(tickets)):

        if tickets[n][0] == "ICN":
            tickets_copy = copy.deepcopy(tickets)

            trv_route = []
            trv_route.append(tickets[n][0])
            trv_route.append(tickets[n][1])
            del tickets_copy[n]


            while len(tickets_copy) > 0:
                len_prev = len(tickets_copy)
                for m in range(len(tickets_copy)):
                    if trv_route[-1] == tickets_copy[m][0]:
                        trv_route.append(tickets_copy[m][1])
                        del tickets_copy[m]
                        break

                len_now = len(tickets_copy)
                if len_prev == len_now: break

            if len(tickets_copy) == 0: TRV_ROUTE.append(trv_route)


    answer = sorted(TRV_ROUTE)[0]
    return answer
