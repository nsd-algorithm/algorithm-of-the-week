import heapq as hq

num_loop = int(input())

for _ in range(num_loop):
    len_numbers = int(input())

    numbers = []
    for _ in range(len_numbers):
        hq.heappush(numbers,input())

    is_continue = False
    number_prev = ""
    for idx in range(len_numbers):
        number_now = hq.heappop(numbers)

        if idx > 0:
            if len(number_now) >= len(number_prev):
                for idx2 in range(len(number_prev)):
                    if number_now[idx2] != number_prev[idx2]: break

                    if idx2 == len(number_prev) - 1:
                        print("NO")
                        is_continue = True
                        break


            if is_continue: break

        if idx == len_numbers - 1: print("YES")
        number_prev = number_now
