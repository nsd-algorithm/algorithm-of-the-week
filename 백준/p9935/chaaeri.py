# ref. https://mytodays.tistory.com/23
str = input()
pang = input()

stack = []


for i in str:
    stack.append(i)
    # 만약 stack에 들어간 글자가 폭발글자의 마지막이고
    # 폭발글자 수만큼 stack에 글자를 확인했을 때 폭발 글자면
    # 문자열 폭발 실행하기
    if i == pang[-1] and "".join(stack[-len(pang):]) == pang:
        # 폭발 글자 수 만큼 pop하기
        for j in range(len(pang)):
            stack.pop()
result = "".join(stack)

if (len(result) == 0):
    print("FRULA")
else:
    print(result)
    # count = 0
    # while(1):
    #     if len(str) == 0:
    #         print("FRULA")
    #         break
    #     else:
    #         if (pang in str):
    #             # print("str : ", str, "pang : ", pang)
    #             str = str.replace(pang, "")
    #             count += 1
    #         else:
    #             if (count != 0):
    #                 print(str)
    #                 break
    #             else:
    #                 print("FRULA")
    #                 break
