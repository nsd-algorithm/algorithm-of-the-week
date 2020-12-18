def solution(number, k):
    len_number = len(number)
    i = 0

    while i < len(number) - 1:
        if number[i] < number[i + 1]:
            number = number[:i] + number[i + 1:]
            if i != 0:
                i -= 1
            k -= 1
            if k < 1:
                break
        else:
            i += 1

    number = number[:len_number-k]

    return number
