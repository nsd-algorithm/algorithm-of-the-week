def solution(routes):
    answer = 1
    routes.sort()
    end = routes[0][1] # 카메라 끝
    for i in range(len(routes)):
        if routes[i][0] > end: # 현재 차의 시작 부분이 end 범위(카메라 설치의)보다 크면 카메라 설치 해야함
            answer += 1
            end = routes[i][1]
        elif routes[i][1] <= end: # 현재 차의 끝 부분이 end 범위에 들어오기 때문에 end 부분만 갱신하고 끝
            end = routes[i][1]
    return answer

