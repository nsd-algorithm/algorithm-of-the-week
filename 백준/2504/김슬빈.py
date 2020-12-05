import sys

_str = sys.stdin.readline().strip()

# 1. 문자열 쪼개기
def devide_str(_str_t):
    STR_TMP = []
    idx_s = 0
    cnt_s, cnt_l = 0, 0
    for n in range(len(_str_t)):
        _s = _str_t[n]
        if _s == "(": cnt_s += 1
        elif _s == ")": cnt_s -= 1

        elif _s == "[": cnt_l += 1
        elif _s == "]": cnt_l -= 1

        if n > 0 and cnt_s == 0 and cnt_l == 0:
            STR_TMP.append(_str_t[idx_s:n+1])
            idx_s = n+1

    if cnt_s != 0 or cnt_l != 0: STR_TMP = []

    return STR_TMP
STR = devide_str(_str)

# 2. 문자열 계산
def calculate_str(_str_t):
    STR_T = devide_str(_str_t)

    if _str_t == "()": return 2
    elif _str_t == "[]": return 3


    elif _str_t[0] == "(" and _str_t[-1] == ")":
        # STR_T = devide_str(_str_t)
        if len(STR_T) == 1: return 2*calculate_str(_str_t[1:-1])
        elif len(STR_T) > 1:
            answer_tmp = 0
            for _str_t in STR_T:
                tmp = calculate_str(_str_t)
                answer_tmp += tmp
                if tmp == 0: return 0
            return answer_tmp

    elif _str_t[0] == "[" and _str_t[-1] == "]":
        # STR_T = devide_str(_str_t)
        if len(STR_T) == 1: return 3*calculate_str(_str_t[1:-1])
        elif len(STR_T) > 1:
            answer_tmp = 0
            for _str_t in STR_T:
                tmp = calculate_str(_str_t)
                answer_tmp += tmp
                if tmp == 0: return 0
            return answer_tmp

    elif len(STR_T) > 1:
        answer_tmp = 0
        for _str_t in STR_T:
            tmp = calculate_str(_str_t)
            answer_tmp += tmp
            if tmp == 0: return 0
        return answer_tmp


    else: return 0

answer = 0
for _str in STR:
    tmp = calculate_str(_str)
    answer += tmp

    if tmp == 0:
        answer = 0
        break


print(answer)
