def check_binary(k, A, answer_tmp):
    sum_tmp = 0
    for a in A:
        sum_tmp += a
        if a > answer_tmp: break

        if sum_tmp > answer_tmp:
            if k == 1: break
            else:
                k -= 1
                sum_tmp = a
    if sum_tmp > answer_tmp: more_flag = 1
    else: more_flag = -1

    return more_flag


def solution(k, m, A):
    answer_min, answer_max = 1, len(A)*max(A)

    answer_tmp_prev = -1
    while True:
        answer_tmp = (answer_min + answer_max) // 2
        if answer_tmp == answer_tmp_prev: break
        # print(answer_tmp, answer_min, answer_max)
        more_flag = check_binary(k, A,answer_tmp)
        if more_flag == 1: # 수가 크다
            answer_min = answer_tmp
        if more_flag == -1:
            answer_max = answer_tmp
        answer_tmp_prev = answer_tmp

    more_flag = check_binary(k, A, answer_tmp)
    if more_flag > 0: answer_tmp += 1
    answer = answer_tmp
    return answer



k, m, A = 52, 1, [0, 0, 0, 0, 0, 0, 0, 0, 0]
print(solution(k, m, A))
