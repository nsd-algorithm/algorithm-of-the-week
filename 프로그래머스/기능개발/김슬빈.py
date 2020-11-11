def solution(PROGRESS, SPEED):
    len_PROGRESS = len(PROGRESS)

    FINISH_DATES = [0]*len_PROGRESS

    # 1. 각 progress당 완료 날짜 계산
    date = 0
    while min(FINISH_DATES) == 0:
        date += 1
        for n in range(len_PROGRESS):
            if FINISH_DATES[n] == 0:
                PROGRESS[n] += SPEED[n]
                if PROGRESS[n] >= 100: FINISH_DATES[n] = date

    print(FINISH_DATES)

    # 2. 완료 날짜를 stack으로 쌓음
    answer = []
    stack = []
    for n in range(len_PROGRESS):
        stack.append(FINISH_DATES[n])

        # 1) 완성 시간이 더 늦은 기능이 들어올 경우, 그 이전 기능까지 먼저 출시
        #    더 늦은 기능은 기존 스택에 잔류, 나머지는 제거
        if len(stack) >= 2:
            if stack[-1] > stack[0]:
                answer.append(len(stack) - 1)
                stack = [FINISH_DATES[n]]

        # 2) 마지막 인덱스일 경우 answer에 삽입
        if n == len_PROGRESS - 1:
            answer.append(len(stack))
            break

    return answer
