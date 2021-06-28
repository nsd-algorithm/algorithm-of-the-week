def solution(enroll, referral, seller, amount):
    answer_dict = {}
    enroll_dict = {}
    for idx, name_e in enumerate(enroll):
        answer_dict[name_e] = 0
        enroll_dict[name_e] = referral[idx]

    for idx, name in enumerate(seller):
        money_total = amount[idx] * 100
        # print(name, money_total)

        while name != "-":
            money_tax = int(money_total / 10)
            answer_dict[name] += money_total - money_tax
            name = enroll_dict[name]
            money_total = money_tax
            if money_total == 0: break

    answer = list(answer_dict.values())
    return answer
