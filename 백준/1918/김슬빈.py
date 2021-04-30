infix = input()
infix_wb = ''

# 1. infix 식에 괄호 추가
is_superior = False
for op in infix:
    # 1) 연산자일 때
    if op == '=' or op =='-' or op == '*' or op == '/':
        infix_wb += op
        if op == '*' or op == '/':
            if infix_wb[-2] != ')':
                # print(infix_wb[-1], op)
                is_superior = True
                infix_wb = infix_wb[:-2] + '(' + infix_wb[-2:]

            else:
                idx_infix, braket_count = -3, -1
                while braket_count != 0:
                    # print(braket_count, idx_infix, infix_wb)
                    idx_infix -= 1
                    if infix_wb[idx_infix] == ')': braket_count -= 1
                    elif infix_wb[idx_infix] == '(': braket_count += 1
                is_superior = True
                infix_wb = infix_wb[:idx_infix] + '(' + infix_wb[idx_infix:]

    # 2) 피연산자일 때
    else:
        infix_wb += op
        if is_superior:
            infix_wb += ')'
            is_superior = False
infix_wb = '(' + infix_wb + ')'
print(infix_wb)

"""
입력 1
A+B*C-D/E

중간 1
(A+(B*C)-(D/E))

출력 1
ABC*+DE/-

입력 2
A+(B+C)*D-E/F


"""

