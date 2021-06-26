def solution(new_id):
    # new_id = "test"

    # 1단계
    new_id = new_id.lower()

    # 2단계
    answer = ""
    for _chr in new_id:
        if 'a' <= _chr <= 'z'or '0' <= _chr <= '9' or _chr == '-' or _chr == '_' or _chr == '.':
            answer = answer + _chr

    # 3단계
    len_answer = len(answer)
    answer = answer.replace("..", ".")
    while len_answer != len(answer):
        len_answer = len(answer)
        answer = answer.replace("..", ".")

    # 4단계
    if len(answer) > 0 and answer[0] == '.': answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.': answer = answer[:-1]

    # 5단계
    if len(answer) == 0: answer = 'a'

    # 6단계
    if len(answer) >= 16: answer = answer[:15]
    if answer[-1] == '.': answer = answer[:-1]

    # 7단계
    while len(answer) < 3:
        answer += answer[-1]


    return answer
